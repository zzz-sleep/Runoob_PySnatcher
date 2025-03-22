# Python 判断一个字符串是否包含数字

## 题目描述
Python3 实例
在 Python 中，我们可以使用多种方法来判断一个字符串是否包含数字。下面是一个简单的示例，使用any()函数和isdigit()方法来实现这个功能。

## 实例
### 代码
```python
defcontains_number(s):
     returnany(char.isdigit()forcharins)
 # 测试
 test_string="Hello123"
 ifcontains_number(test_string):
     print("字符串包含数字")
 else:
     print("字符串不包含数字")
```
### 输出结果
```
字符串包含数字
```
源链接: [https://www.runoob.com/python3/python-contains-digit.html](https://www.runoob.com/python3/python-contains-digit.html)