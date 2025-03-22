# Python 使用类实现一个计算矩阵加法的程序

## 题目描述
Python3 实例
我们将使用 Python 的类来实现一个简单的矩阵加法程序。矩阵加法要求两个矩阵具有相同的维度，我们将创建一个Matrix类，并在其中实现矩阵加法的方法。

## 实例
### 代码
```python
classMatrix:
     def__init__(self,data):
         self.data=data
         self.rows=len(data)
         self.cols=len(data[0])ifself.rows&gt;0else0
     def__add__(self,other):
         ifself.rows!=other.rowsorself.cols!=other.cols:
             raiseValueError("Matrices must have the same dimensions for addition.")
         result=[
             [self.data[i][j]+ other.data[i][j]forjinrange(self.cols)]
             foriinrange(self.rows)
         ]
         returnMatrix(result)
     def__str__(self):
         return'n'.join([' '.join(map(str,row))forrowinself.data])
 # 示例使用
 matrix1=Matrix([[1,2,3],[4,5,6],[7,8,9]])
 matrix2=Matrix([[9,8,7],[6,5,4],[3,2,1]])
 result_matrix=matrix1 + matrix2
 print(result_matrix)
```
### 输出结果
```
10 10 10
10 10 10
10 10 10
```
源链接: [https://www.runoob.com/python3/python-matrix-addition.html](https://www.runoob.com/python3/python-matrix-addition.html)