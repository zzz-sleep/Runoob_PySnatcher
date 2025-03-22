# Python 在字符串中查找一个子字符串的位置

## 题目描述
Python3 实例
在 Python 中，你可以使用find()方法来查找一个子字符串在字符串中的位置。如果找到子字符串，find()方法会返回子字符串第一次出现的索引；如果没有找到，则返回 -1。

## 实例
### 代码
```python
# 定义一个字符串
 text="Hello, welcome to the world of Python."
 # 查找子字符串 "welcome" 的位置
 position=text.find("welcome")
 # 输出结果
 print("子字符串的位置是:",position)
```
### 输出结果
```
子字符串的位置是: 7
```
源链接: [https://www.runoob.com/python3/python-substring-position.html](https://www.runoob.com/python3/python-substring-position.html)