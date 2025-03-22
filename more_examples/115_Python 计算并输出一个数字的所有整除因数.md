# Python 计算并输出一个数字的所有整除因数

## 题目描述
Python3 实例
描述内容：我们将编写一个 Python 程序来计算并输出一个给定数字的所有整除因数。整除因数是指能够整除该数字且没有余数的整数。

## 实例
### 代码
```python
deffind_factors(num):
     factors=[]
     foriinrange(1,num +1):
         ifnum % i==0:
             factors.append(i)
     returnfactors
 number=int(input("请输入一个数字: "))
 print(f"{number} 的所有因数是: {find_factors(number)}")
```
### 输出结果
```
请输入一个数字: 28
28 的所有因数是: [1, 2, 4, 7, 14, 28]
```
源链接: [https://www.runoob.com/python3/python-divisible-factors.html](https://www.runoob.com/python3/python-divisible-factors.html)