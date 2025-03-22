# Python 判断一个数字是否为完全平方数

## 题目描述
Python3 实例
要判断一个数字是否为完全平方数，我们可以使用数学方法。一个完全平方数是指可以表示为某个整数的平方的数。例如，16 是完全平方数，因为它是 4 的平方。

## 实例
### 代码
```python
importmath
 defis_perfect_square(n):
     ifn<0:
         returnFalse
     sqrt=math.isqrt(n)
     returnsqrt * sqrt==n
 # 测试
 number=16
 ifis_perfect_square(number):
     print(f"{number} 是完全平方数")
 else:
     print(f"{number} 不是完全平方数")
```
### 输出结果
```
16 是完全平方数
```
源链接: [https://www.runoob.com/python3/python-perfect-square-check.html](https://www.runoob.com/python3/python-perfect-square-check.html)