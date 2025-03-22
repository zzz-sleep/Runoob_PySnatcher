# Python 找到一个数的所有因子

## 题目描述
Python3 实例
在 Python 中，我们可以编写一个简单的程序来找到一个数的所有因子。因子是指能够整除该数的整数。例如，6 的因子是 1, 2, 3, 6。

## 实例
### 代码
```python
deffind_factors(n):
     factors=[]
     foriinrange(1,n +1):
         ifn % i==0:
             factors.append(i)
     returnfactors
 number=12
 print(f"Factors of {number} are: {find_factors(number)}")
```
### 输出结果
```
Factors of 12 are: [1, 2, 3, 4, 6, 12]
```
源链接: [https://www.runoob.com/python3/python-find-factors.html](https://www.runoob.com/python3/python-find-factors.html)