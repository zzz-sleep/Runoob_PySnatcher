# Python 判断一个数是否为完全平方数

## 题目描述
Python3 实例
完全平方数是指一个整数可以表示为另一个整数的平方。例如，1, 4, 9, 16 等都是完全平方数。我们可以通过数学方法来判断一个数是否为完全平方数。

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
     print(f"{number} 是一个完全平方数")
 else:
     print(f"{number} 不是一个完全平方数")
```
### 输出结果
```
16 是一个完全平方数
```
源链接: [https://www.runoob.com/python3/python-perfect-square.html](https://www.runoob.com/python3/python-perfect-square.html)