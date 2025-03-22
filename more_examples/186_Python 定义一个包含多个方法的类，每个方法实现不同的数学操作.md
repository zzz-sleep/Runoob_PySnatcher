# Python 定义一个包含多个方法的类，每个方法实现不同的数学操作

## 题目描述
Python3 实例
我们将定义一个名为MathOperations的类，该类包含多个方法，每个方法实现不同的数学操作，如加法、减法、乘法和除法。

## 实例
### 代码
```python
classMathOperations:
     defadd(self,a,b):
         returna + b
     defsubtract(self,a,b):
         returna - b
     defmultiply(self,a,b):
         returna * b
     defdivide(self,a,b):
         ifb==0:
             return"Error: Division by zero is not allowed."
         returna / b
```
### 输出结果
```
未找到输出结果
```
## 实例
### 代码
```python
math_ops=MathOperations()
 print(math_ops.add(10,5))# 输出: 15
 print(math_ops.subtract(10,5))# 输出: 5
 print(math_ops.multiply(10,5))# 输出: 50
 print(math_ops.divide(10,5))# 输出: 2.0
 print(math_ops.divide(10,0))# 输出: Error: Division by zero is not allowed.
```
### 输出结果
```
未找到输出结果
```
源链接: [https://www.runoob.com/python3/python-math-operations.html](https://www.runoob.com/python3/python-math-operations.html)