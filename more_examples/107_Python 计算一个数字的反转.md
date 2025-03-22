# Python 计算一个数字的反转

## 题目描述
Python3 实例
在这个例子中，我们将编写一个 Python 函数来反转一个整数。例如，输入 123，输出 321。

## 实例
### 代码
```python
defreverse_number(n):
     reversed_num=0
     whilen>0:
         digit=n %10
         reversed_num=reversed_num *10+ digit
         n=n //10
     returnreversed_num
 # 测试函数
 number=12345
 print("反转后的数字是:",reverse_number(number))
```
### 输出结果
```
反转后的数字是: 54321
```
源链接: [https://www.runoob.com/python3/python-reverse-number.html](https://www.runoob.com/python3/python-reverse-number.html)