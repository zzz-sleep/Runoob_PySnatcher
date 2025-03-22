import requests
from bs4 import BeautifulSoup
import os
import time
import random
import logging
import json

# ====================
# 配置参数
# ====================
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Referer": "https://www.runoob.com/"
}
BASE_URL = "https://www.runoob.com/python3/python3-examples.html"
JSON_URL = "https://www.runoob.com/static/data/python_esc.json"
BASIC_DIR = "basic_examples"  # <ul> 中的实例保存目录
MORE_DIR = "more_examples"  # <table> 中的实例保存目录
REQUEST_DELAY = 1
MAX_RETRY = 3
DOMAIN = "https://www.runoob.com"

# 设置日志
logging.basicConfig(level=logging.DEBUG, format="%(message)s")
logger = logging.getLogger(__name__)


# ====================
# 工具函数
# ====================
def create_session():
    session = requests.Session()
    adapter = requests.adapters.HTTPAdapter(max_retries=MAX_RETRY)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session


def safe_request(url, session):
    try:
        response = session.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        response.encoding = 'utf-8'
        return response
    except Exception as e:
        logger.error(f"请求失败: {url} - {str(e)}")
        return None


def validate_link(href):
    return href and ("/python3/" in href) and (href.endswith(".html"))


def download_image(url, save_path):
    if url.startswith('/'):
        url = DOMAIN + url
    elif url.startswith('//'):
        url = "https:" + url
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        with open(save_path, 'wb') as f:
            f.write(response.content)
        logger.info(f"图片下载成功: {save_path}")
        return True
    except Exception as e:
        logger.debug(f"图片下载失败: {url} - {str(e)}")
        return False


def parse_code_from_example_code(example_code):
    lines = []
    current_line = ""
    indent = 0

    hl_main = example_code.find('div', class_='hl-main')
    if hl_main:
        code_container = hl_main
    else:
        code_container = example_code

    for elem in code_container.children:
        if isinstance(elem, str):
            text = elem.strip()
            if text:
                current_line += text
        elif elem.name == 'br':
            if current_line:
                lines.append(" " * indent + current_line)
            current_line = ""
            next_sibling = elem.next_sibling
            if isinstance(next_sibling, str):
                indent = len(next_sibling) - len(next_sibling.lstrip())
            else:
                indent = 0
        elif elem.name == 'span':
            current_line += elem.get_text(strip=True)

    if current_line:
        lines.append(" " * indent + current_line)

    return "\n".join(lines) or "未找到代码"


# ====================
# 核心逻辑
# ====================
def get_example_links(session):
    logger.info("正在获取实例列表...")
    response = safe_request(BASE_URL, session)
    if not response:
        return [], []

    soup = BeautifulSoup(response.text, 'lxml')
    basic_links = []
    more_links = []

    # 从所有 <ul> 中提取基本实例链接
    ul_list = soup.find_all('ul')
    for ul in ul_list:
        links = [
            f"https://www.runoob.com{a['href']}" if not a['href'].startswith('http') else a['href']
            for a in ul.find_all('a', href=True)
            if '/python3/' in a['href'] and a['href'].endswith('.html')
        ]
        basic_links.extend(links)

    # 从 JSON 文件中提取更多实例链接
    json_response = safe_request(JSON_URL, session)
    if json_response:
        try:
            json_data = json.loads(json_response.text)
            more_links = [
                f"https://www.runoob.com/python3/python-{item['slug']}.html"
                for item in json_data.get('questions', [])
            ]
            logger.info(f"从 JSON 提取到 {len(more_links)} 个更多实例链接")
        except Exception as e:
            logger.error(f"解析 JSON 失败: {str(e)}")

    # 去重
    basic_links = list(set(basic_links))
    more_links = list(set(more_links))
    logger.info(f"从 <ul> 提取到 {len(basic_links)} 个基本实例链接")
    logger.info(f"基本实例去重后: {len(basic_links)}, 更多实例去重后: {len(more_links)}")
    return basic_links, more_links


def parse_example_page(url, session):
    logger.info(f"正在处理: {url}")
    response = safe_request(url, session)
    if not response:
        return None

    soup = BeautifulSoup(response.text, 'lxml')

    # 限定范围提取标题
    content = soup.find('div', class_='article-intro') or soup.find('div', id='content')
    if content:
        h1_tag = content.find('h1')
        if h1_tag:
            title = h1_tag.get_text(strip=True)
            logger.debug(f"从 <h1> 提取到的标题: {title}")
        else:
            title_tag = soup.find('title')
            title = title_tag.get_text(strip=True).replace(' | 菜鸟教程', '') if title_tag else url.split('/')[
                -1].replace('.html', '')
            logger.warning(f"在 article-intro 未找到 <h1>，使用 <title> 或 URL 回退标题: {title}")
    else:
        title = url.split('/')[-1].replace('.html', '')
        logger.warning(f"未找到 article-intro，使用 URL 回退标题: {title}")

    # 提取题目描述
    description = []
    if content:
        for elem in content.children:
            if elem.name == 'div' and 'example' in elem.get('class', []):
                break
            if elem.name == 'p':
                text = elem.get_text(strip=True)
                if text and not text.startswith(('以上实例', '执行以上代码', '点击')):
                    description.append(text)
            elif elem.name == 'pre':
                description.append(f"```\n{elem.get_text(separator='\n')}\n```")

    # 提取代码和输出结果
    examples = []
    example_divs = soup.find_all('div', class_='example')
    for ex in example_divs:
        ex_title = ex.find('h2', class_='example').get_text(strip=True) if ex.find('h2', class_='example') else "实例"

        code_button = ex.find('button', class_='copy-code-button')
        if code_button and 'data-clipboard-text' in code_button.attrs:
            code = code_button['data-clipboard-text']
        else:
            code_div = ex.find('div', class_='example_code')
            code = parse_code_from_example_code(code_div) if code_div else "未找到代码"

        output = None
        next_p = ex.find_next('p')
        if next_p and "输出结果为" in next_p.get_text():
            next_pre = next_p.find_next('pre')
            if next_pre:
                output = next_pre.get_text(separator='\n')
        if not output:
            next_pre = ex.find_next('pre')
            if next_pre and next_pre.get_text(strip=True) != code.strip():
                output = next_pre.get_text(separator='\n')
            else:
                output = "未找到输出结果"

        examples.append({"title": ex_title, "code": code, "output": output})

    if not examples:
        code_blocks = []
        example_code = soup.find('div', class_='example_code')
        if example_code:
            code_blocks.append(parse_code_from_example_code(example_code))
        output = None
        for p in soup.find_all('p'):
            if "输出结果为" in p.get_text():
                next_pre = p.find_next('pre')
                if next_pre:
                    output = next_pre.get_text(separator='\n')
                break
        examples.append(
            {"title": "实例", "code": '\n\n'.join(code_blocks) or "未找到代码", "output": output or "未找到输出结果"})

    # 提取相关图片
    images = []
    if content:
        for img in content.find_all('img', src=lambda x: x and ('.gif' in x or '.png' in x)):
            img_url = img['src']
            if 'up.gif' in img_url or 'qrcode.png' in img_url:
                continue
            img_name = img_url.split('/')[-1]
            save_path = os.path.join(BASIC_DIR if url in basic_links else MORE_DIR,
                                     f"{sanitize_filename(title)}_{img_name}")
            if download_image(img_url, save_path):
                images.append({"url": img_url, "path": f"{sanitize_filename(title)}_{img_name}"})

    return {
        "title": title,
        "description": '\n'.join(description),
        "examples": examples,
        "images": images,
        "url": url
    }


# ====================
# 文件保存
# ====================
def sanitize_filename(title):
    invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    return ''.join(c for c in title if c not in invalid_chars)[:50]


def save_to_markdown(data, index, is_basic=True):
    save_dir = BASIC_DIR if is_basic else MORE_DIR
    os.makedirs(save_dir, exist_ok=True)
    filename = f"{index:03d}_{sanitize_filename(data['title'])}.md"
    filepath = os.path.join(save_dir, filename)
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"# {data['title']}\n\n")
            f.write(f"## 题目描述\n{data['description']}\n\n")
            if data['images']:
                f.write("## 示例图片\n")
                for img in data['images']:
                    f.write(f"![{img['path']}]({img['path']})\n")
                f.write("\n")
            for i, example in enumerate(data['examples'], 1):
                f.write(f"## {example['title']}\n")
                f.write(f"### 代码\n```python\n{example['code']}\n```\n")
                f.write(f"### 输出结果\n```\n{example['output']}\n```\n")
            f.write(f"源链接: [{data['url']}]({data['url']})")
        return True
    except Exception as e:
        logger.error(f"保存失败: {str(e)}")
        return False


# ====================
# 主程序
# ====================
def main():
    global basic_links
    session = create_session()

    basic_links, more_links = get_example_links(session)
    if not basic_links and not more_links:
        logger.info("未找到任何示例链接!")
        return

    logger.info(f"共发现 {len(basic_links)} 个基本实例和 {len(more_links)} 个更多实例")

    success_count = 0
    failed_links = []

    # 处理基本实例
    for idx, url in enumerate(basic_links, 1):
        time.sleep(REQUEST_DELAY * (0.8 + 0.4 * random.random()))
        data = parse_example_page(url, session)
        if not data:
            failed_links.append(url)
            continue
        if save_to_markdown(data, idx, is_basic=True):
            success_count += 1
            logger.info(f"已保存基本实例: {data['title']}")
        else:
            failed_links.append(url)
            logger.info(f"保存基本实例失败: {data['title']}")

    # 处理更多实例
    for idx, url in enumerate(more_links, 1):
        time.sleep(REQUEST_DELAY * (0.8 + 0.4 * random.random()))
        data = parse_example_page(url, session)
        if not data:
            failed_links.append(url)
            continue
        if save_to_markdown(data, idx, is_basic=False):
            success_count += 1
            logger.info(f"已保存更多实例: {data['title']}")
        else:
            failed_links.append(url)
            logger.info(f"保存更多实例失败: {data['title']}")

    logger.info(f"\n完成! 成功保存 {success_count}/{len(basic_links) + len(more_links)} 个示例")
    if failed_links:
        logger.info("以下链接保存失败:")
        for link in failed_links:
            logger.info(f"  - {link}")


if __name__ == "__main__":
    main()