# Python 计算一个数字的位数

## 题目描述
Python3 实例
我们可以通过将数字转换为字符串，然后计算字符串的长度来轻松地确定一个数字的位数。这种方法简单且直观。

## 实例
### 代码
```python
defcount_digits(number):
     returnlen(str(number))
 # 示例使用
 number=12345
 print(f"The number {number} has {count_digits(number)} digits.")
```
### 输出结果
```
The number 12345 has 5 digits.
```
源链接: [https://www.runoob.com/python3/python-digit-count.html](https://www.runoob.com/python3/python-digit-count.html)