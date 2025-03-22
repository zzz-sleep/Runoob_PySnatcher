# Python 实现简单的字符串替换功能

## 题目描述
Python3 实例
在 Python 中，字符串替换是一个常见的操作。我们可以使用str.replace()方法来实现简单的字符串替换功能。这个方法会将字符串中所有匹配的子字符串替换为指定的新字符串。

## 实例
### 代码
```python
# 原始字符串
 original_string="Hello, world! Hello, Python!"
 # 使用 replace() 方法替换字符串
 new_string=original_string.replace("Hello","Hi")
 # 输出替换后的字符串
 print(new_string)
```
### 输出结果
```
Hi, world! Hi, Python!
```
源链接: [https://www.runoob.com/python3/python-string-replace.html](https://www.runoob.com/python3/python-string-replace.html)