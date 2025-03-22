# Python 计算一个给定数字的各位数字和

## 题目描述
Python3 实例
我们可以通过将数字转换为字符串，然后遍历字符串中的每个字符，将其转换回整数并累加，来计算一个给定数字的各位数字之和。

## 实例
### 代码
```python
defdigit_sum(number):
     returnsum(int(digit)fordigitinstr(number))
 # 示例使用
 number=12345
 result=digit_sum(number)
 print(f"The sum of digits of {number} is {result}")
```
### 输出结果
```
The sum of digits of 12345 is 15
```
源链接: [https://www.runoob.com/python3/python-digit-sum-number.html](https://www.runoob.com/python3/python-digit-sum-number.html)