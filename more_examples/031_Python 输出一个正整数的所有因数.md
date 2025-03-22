# Python 输出一个正整数的所有因数

## 题目描述
Python3 实例
在 Python 中，我们可以编写一个简单的程序来找出一个正整数的所有因数。因数是指能够整除该数的整数。例如，6 的因数有 1, 2, 3, 6。

## 实例
### 代码
```python
deffind_factors(n):
     factors=[]
     foriinrange(1,n +1):
         ifn % i==0:
             factors.append(i)
     returnfactors
 number=28
 print(f"The factors of {number} are: {find_factors(number)}")
```
### 输出结果
```
The factors of 28 are: [1, 2, 4, 7, 14, 28]
```
源链接: [https://www.runoob.com/python3/python-print-factors.html](https://www.runoob.com/python3/python-print-factors.html)