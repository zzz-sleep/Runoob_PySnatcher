# Python 判断一个字符串是否为字母数字字符串

## 题目描述
Python3 实例
在 Python 中，我们可以使用字符串的isalnum()方法来判断一个字符串是否只包含字母和数字。如果字符串中的所有字符都是字母或数字，则返回True，否则返回False。

## 实例
### 代码
```python
defis_alphanumeric(s):
     returns.isalnum()
 # 测试
 test_string1="Hello123"
 test_string2="Hello 123"
 test_string3="Hello@123"
 print(is_alphanumeric(test_string1))# 输出 True
 print(is_alphanumeric(test_string2))# 输出 False
 print(is_alphanumeric(test_string3))# 输出 False
```
### 输出结果
```
True
False
False
```
源链接: [https://www.runoob.com/python3/python-alphanumeric-check.html](https://www.runoob.com/python3/python-alphanumeric-check.html)