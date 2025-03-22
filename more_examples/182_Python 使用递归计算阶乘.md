# Python 使用递归计算阶乘

## 题目描述
Python3 实例
阶乘是一个数学概念，表示从1乘到某个正整数n的乘积。例如，5的阶乘（记作5!）是12345 = 120。我们可以使用递归的方法来计算阶乘。递归是一种函数调用自身的技术。

## 实例
### 代码
```python
deffactorial(n):
     ifn==1:
         return1
     else:
         returnn * factorial(n -1)
 # 计算5的阶乘
 result=factorial(5)
 print(result)
```
### 输出结果
```
120
```
源链接: [https://www.runoob.com/python3/python-recursive-factorial.html](https://www.runoob.com/python3/python-recursive-factorial.html)