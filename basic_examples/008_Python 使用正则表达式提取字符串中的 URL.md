# Python 使用正则表达式提取字符串中的 URL

## 题目描述
Python3 实例
给定一个字符串，里面包含 URL 地址，需要我们使用正则表达式来获取字符串的 URL。

## 实例
### 代码
```python
importredefFind(string):# findall() 查找匹配正则表达式的字符串url=re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+',string)returnurlstring='Runoob 的网页地址为：https://www.runoob.com，Google 的网页地址为：https://www.google.com'print("Urls:",Find(string))
```
### 输出结果
```
(?:x)
```
源链接: [https://www.runoob.com/python3/python-find-url-string.html](https://www.runoob.com/python3/python-find-url-string.html)