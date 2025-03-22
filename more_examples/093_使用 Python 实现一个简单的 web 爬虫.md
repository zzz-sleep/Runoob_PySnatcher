# 使用 Python 实现一个简单的 web 爬虫

## 题目描述
Python3 实例
我们将使用 Python 的requests库来发送 HTTP 请求，并使用BeautifulSoup库来解析 HTML 内容。这个简单的 web 爬虫将从一个网页中提取所有的链接。

## 实例
### 代码
```python
importrequests
 frombs4importBeautifulSoup
 defsimple_web_crawler(url):
     # 发送 HTTP 请求
     response=requests.get(url)
     # 检查请求是否成功
     ifresponse.status_code==200:
         # 解析 HTML 内容
         soup=BeautifulSoup(response.text,'html.parser')
         # 查找所有的链接
         links=soup.find_all('a')
         # 提取并打印链接
         forlinkinlinks:
             href=link.get('href')
             ifhref:
                 print(href)
     else:
         print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
 # 使用示例
 simple_web_crawler('https://www.example.com')
```
### 输出结果
```
https://www.iana.org/domains/example
```
源链接: [https://www.runoob.com/python3/python-web-crawler.html](https://www.runoob.com/python3/python-web-crawler.html)