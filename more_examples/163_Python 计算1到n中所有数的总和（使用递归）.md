# Python 计算1到n中所有数的总和（使用递归）

## 题目描述
Python3 实例
我们将使用递归的方法来计算从1到n的所有整数的总和。递归是一种通过函数调用自身来解决问题的方法。在这个例子中，我们将定义一个函数，该函数会不断地调用自身，直到达到基本情况（即n等于1），然后开始返回结果。

## 实例
### 代码
```python
defsum_recursive(n):
     ifn==1:
         return1
     else:
         returnn + sum_recursive(n -1)
 # 测试函数
 n=10
 print(f"1 到 {n} 的总和是: {sum_recursive(n)}")
```
### 输出结果
```
1 到 10 的总和是: 55
```
源链接: [https://www.runoob.com/python3/python-recursive-sum.html](https://www.runoob.com/python3/python-recursive-sum.html)