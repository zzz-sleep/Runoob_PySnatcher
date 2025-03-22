# Python 使用正则表达式从字符串中提取所有数字

## 题目描述
Python3 实例
在 Python 中，我们可以使用re模块来处理正则表达式。要从字符串中提取所有数字，可以使用re.findall()函数，它能够返回所有匹配正则表达式的子串。

## 实例
### 代码
```python
importre
 # 示例字符串
 text="The price is 45 dollars and 30 cents."
 # 使用正则表达式提取所有数字
 numbers=re.findall(r'd+',text)
 print(numbers)
```
### 输出结果
```
['45', '30']
```
源链接: [https://www.runoob.com/python3/python-extract-numbers.html](https://www.runoob.com/python3/python-extract-numbers.html)