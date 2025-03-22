# Python 将字符串中的所有数字替换为星号

## 题目描述
Python3 实例
在 Python 中，我们可以使用正则表达式模块re来查找字符串中的所有数字，并将其替换为星号*。以下是一个简单的示例代码，展示了如何实现这一功能。

## 实例
### 代码
```python
importre
 defreplace_numbers_with_stars(input_string):
     # 使用正则表达式替换所有数字为星号
     result=re.sub(r'd','*',input_string)
     returnresult
 # 示例字符串
 input_string="Hello 123 World 456"
 output_string=replace_numbers_with_stars(input_string)
 print(output_string)
```
### 输出结果
```
Hello *** World ***
```
源链接: [https://www.runoob.com/python3/python-replace-numbers.html](https://www.runoob.com/python3/python-replace-numbers.html)