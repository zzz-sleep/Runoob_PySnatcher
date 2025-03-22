# Python 创建一个类来实现数字的加减乘除运算

## 题目描述
Python3 实例
我们将创建一个名为Calculator的类，该类将包含四个方法：add、subtract、multiply和divide，分别用于执行加法、减法、乘法和除法运算。

## 实例
### 代码
```python
classCalculator:
     def__init__(self,num1,num2):
         self.num1=num1
         self.num2=num2
     defadd(self):
         returnself.num1+self.num2
     defsubtract(self):
         returnself.num1-self.num2
     defmultiply(self):
         returnself.num1*self.num2
     defdivide(self):
         ifself.num2==0:
             return"Error: Division by zero is not allowed."
         returnself.num1/self.num2
 # 示例使用
 calc=Calculator(10,5)
 print("Addition:",calc.add())
 print("Subtraction:",calc.subtract())
 print("Multiplication:",calc.multiply())
 print("Division:",calc.divide())
```
### 输出结果
```
Addition: 15
Subtraction: 5
Multiplication: 50
Division: 2.0
```
源链接: [https://www.runoob.com/python3/python-arithmetic-class.html](https://www.runoob.com/python3/python-arithmetic-class.html)