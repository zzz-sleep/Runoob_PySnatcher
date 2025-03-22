# Python 实现一个基于类的矩阵类

## 题目描述
Python3 实例
我们将创建一个基于类的矩阵类，这个类将支持矩阵的初始化、矩阵的加法、矩阵的乘法以及矩阵的转置操作。这个类将帮助我们理解如何在 Python 中使用类来封装数据和操作。

## 实例
### 代码
```python
classMatrix:
     def__init__(self,data):
         self.data=data
         self.rows=len(data)
         self.cols=len(data[0])ifself.rows>0else0
     def__add__(self,other):
         ifself.rows!=other.rowsorself.cols!=other.cols:
             raiseValueError("Matrices must have the same dimensions for addition.")
         result=[[self.data[i][j]+ other.data[i][j]forjinrange(self.cols)]foriinrange(self.rows)]
         returnMatrix(result)
     def__mul__(self,other):
         ifself.cols!=other.rows:
             raiseValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix.")
         result=[[sum(self.data[i][k]* other.data[k][j]forkinrange(self.cols))forjinrange(other.cols)]foriinrange(self.rows)]
         returnMatrix(result)
     deftranspose(self):
         result=[[self.data[j][i]forjinrange(self.rows)]foriinrange(self.cols)]
         returnMatrix(result)
     def__str__(self):
         return'n'.join([' '.join(map(str,row))forrowinself.data])
 # 示例使用
 m1=Matrix([[1,2],[3,4]])
 m2=Matrix([[5,6],[7,8]])
 print("Matrix 1:")
 print(m1)
 print("Matrix 2:")
 print(m2)
 print("Matrix 1 + Matrix 2:")
 print(m1 + m2)
 print("Matrix 1 * Matrix 2:")
 print(m1 * m2)
 print("Transpose of Matrix 1:")
 print(m1.transpose())
```
### 输出结果
```
Matrix 1:
1 2
3 4
Matrix 2:
5 6
7 8
Matrix 1 + Matrix 2:
6 8
10 12
Matrix 1 * Matrix 2:
19 22
43 50
Transpose of Matrix 1:
1 3
2 4
```
源链接: [https://www.runoob.com/python3/python-matrix-class.html](https://www.runoob.com/python3/python-matrix-class.html)