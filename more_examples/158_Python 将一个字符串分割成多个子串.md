# Python 将一个字符串分割成多个子串

## 题目描述
Python3 实例
在 Python 中，可以使用split()方法将一个字符串分割成多个子串。split()方法会根据指定的分隔符将字符串分割，并返回一个包含所有子串的列表。如果不指定分隔符，默认会使用空格作为分隔符。

## 实例
### 代码
```python
# 示例字符串
 text="Hello World, this is Python"
 # 使用 split() 方法分割字符串
 result=text.split()
 # 输出结果
 print(result)
```
### 输出结果
```

['Hello', 'World,', 'this', 'is', 'Python']
```
源链接: [https://www.runoob.com/python3/python-split-string.html](https://www.runoob.com/python3/python-split-string.html)