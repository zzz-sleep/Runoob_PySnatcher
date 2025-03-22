# Python 实现一个类，表示复数，并提供加法、减法等操作

## 题目描述
Python3 实例
我们将创建一个名为ComplexNumber的类，用于表示复数。复数由实部和虚部组成，我们将实现加法和减法操作。

## 实例
### 代码
```python
classComplexNumber:
     def__init__(self,real,imaginary):
         self.real=real
         self.imaginary=imaginary
     def__add__(self,other):
         returnComplexNumber(self.real+ other.real,self.imaginary+ other.imaginary)
     def__sub__(self,other):
         returnComplexNumber(self.real- other.real,self.imaginary- other.imaginary)
     def__str__(self):
         returnf"{self.real} + {self.imaginary}i"
 # 示例使用
 c1=ComplexNumber(3,4)
 c2=ComplexNumber(1,2)
 print("c1 + c2 =",c1 + c2)
 print("c1 - c2 =",c1 - c2)
```
### 输出结果
```
c1 + c2 = 4 + 6i
c1 - c2 = 2 + 2i
```
源链接: [https://www.runoob.com/python3/python-complex-number.html](https://www.runoob.com/python3/python-complex-number.html)