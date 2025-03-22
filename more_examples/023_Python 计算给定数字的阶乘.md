# Python 计算给定数字的阶乘

## 题目描述
Python3 实例
阶乘是一个数学概念，表示一个正整数 n 的阶乘是所有小于及等于 n 的正整数的乘积，记作 n!。例如，5! = 5 × 4 × 3 × 2 × 1 = 120。下面是一个用 Python 编写的计算阶乘的函数。

## 实例
### 代码
```python
deffactorial(n):
     ifn==0orn==1:
         return1
     else:
         returnn * factorial(n -1)
 # 测试函数
 number=5
 print(f"The factorial of {number} is {factorial(number)}")
```
### 输出结果
```
The factorial of 5 is 120
```
源链接: [https://www.runoob.com/python3/python-factorial-calculation.html](https://www.runoob.com/python3/python-factorial-calculation.html)