# Python 输出字符串中大写字母的个数

## 题目描述
Python3 实例
这个程序将计算并输出给定字符串中大写字母的数量。

## 实例
### 代码
```python
defcount_uppercase_letters(s):
     count=0
     forcharins:
         ifchar.isupper():
             count +=1
     returncount
 # 示例字符串
 sample_string="Hello World! This is a Test."
 uppercase_count=count_uppercase_letters(sample_string)
 print(f"The number of uppercase letters in the string is: {uppercase_count}")
```
### 输出结果
```
The number of uppercase letters in the string is: 4
```
源链接: [https://www.runoob.com/python3/python-uppercase-count.html](https://www.runoob.com/python3/python-uppercase-count.html)