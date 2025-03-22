# Python 判断两个数字是否互为因数

## 题目描述
Python3 实例
在数学中，如果两个数字互为因数，意味着它们可以互相整除，即一个数字除以另一个数字没有余数。我们可以通过编写一个简单的 Python 程序来判断两个数字是否互为因数。

## 实例
### 代码
```python
defare_mutual_factors(a,b):
     ifa % b==0andb % a==0:
         returnTrue
     else:
         returnFalse
 # 测试
 num1=12
 num2=6
 result=are_mutual_factors(num1,num2)
 print(f"{num1} 和 {num2} 是否互为因数: {result}")
```
### 输出结果
```
12 和 6 是否互为因数: True
```
源链接: [https://www.runoob.com/python3/python-factor-check.html](https://www.runoob.com/python3/python-factor-check.html)