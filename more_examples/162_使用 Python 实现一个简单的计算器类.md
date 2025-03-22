# 使用 Python 实现一个简单的计算器类

## 题目描述
Python3 实例
我们将使用 Python 实现一个简单的计算器类，这个类将包含基本的加、减、乘、除运算方法。

## 实例
### 代码
```python
classCalculator:
     defadd(self,a,b):
         returna + b
     defsubtract(self,a,b):
         returna - b
     defmultiply(self,a,b):
         returna * b
     defdivide(self,a,b):
         ifb==0:
             raiseValueError("Cannot divide by zero!")
         returna / b
 # 示例使用
 calc=Calculator()
 print("Addition: ",calc.add(10,5))
 print("Subtraction: ",calc.subtract(10,5))
 print("Multiplication: ",calc.multiply(10,5))
 print("Division: ",calc.divide(10,5))
```
### 输出结果
```
Addition:  15
Subtraction:  5
Multiplication:  50
Division:  2.0
```
源链接: [https://www.runoob.com/python3/python-calculator-class.html](https://www.runoob.com/python3/python-calculator-class.html)