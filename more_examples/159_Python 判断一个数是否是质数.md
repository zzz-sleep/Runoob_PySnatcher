# Python 判断一个数是否是质数

## 题目描述
Python3 实例
质数是指大于1的自然数，且只能被1和它本身整除的数。我们可以通过编写一个Python函数来判断一个数是否是质数。

## 实例
### 代码
```python
defis_prime(n):
     ifn<=1:
         returnFalse
     foriinrange(2,int(n**0.5)+1):
         ifn % i==0:
             returnFalse
     returnTrue
 # 测试函数
 number=29
 ifis_prime(number):
     print(f"{number} 是质数")
 else:
     print(f"{number} 不是质数")
```
### 输出结果
```
29 是质数
```
源链接: [https://www.runoob.com/python3/python-prime-check.html](https://www.runoob.com/python3/python-prime-check.html)