# Python 判断字符串中是否包含某个子字符串

## 题目描述
Python3 实例
在 Python 中，我们可以使用in关键字来判断一个字符串是否包含某个子字符串。这个方法非常简单且直观。

## 实例
### 代码
```python
# 定义一个字符串
 main_string="Hello, welcome to the world of Python programming."
 # 定义要查找的子字符串
 sub_string="Python"
 # 使用 in 关键字判断子字符串是否存在于主字符串中
 ifsub_stringinmain_string:
     print(f"'{sub_string}' is found in the main string.")
 else:
     print(f"'{sub_string}' is not found in the main string.")
```
### 输出结果
```
'Python' is found in the main string.
```
源链接: [https://www.runoob.com/python3/python-substring-check.html](https://www.runoob.com/python3/python-substring-check.html)