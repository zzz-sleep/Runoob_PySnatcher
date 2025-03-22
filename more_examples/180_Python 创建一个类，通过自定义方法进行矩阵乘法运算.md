# Python 创建一个类，通过自定义方法进行矩阵乘法运算

## 题目描述
Python3 实例
我们将创建一个名为Matrix的类，该类包含一个自定义方法multiply，用于执行矩阵乘法运算。矩阵乘法要求第一个矩阵的列数等于第二个矩阵的行数。

## 实例
### 代码
```python
classMatrix:
     def__init__(self,data):
         self.data=data
         self.rows=len(data)
         self.cols=len(data[0])ifself.rows&gt;0else0
     defmultiply(self,other):
         ifself.cols!=other.rows:
             raiseValueError("The number of columns in the first matrix must be equal to the number of rows in the second matrix.")
         result=[[0for_inrange(other.cols)]for_inrange(self.rows)]
         foriinrange(self.rows):
             forjinrange(other.cols):
                 forkinrange(self.cols):
                     result[i][j]+=self.data[i][k]* other.data[k][j]
         returnMatrix(result)
     def__str__(self):
         return'n'.join([' '.join(map(str,row))forrowinself.data])
 # 示例使用
 matrix1=Matrix([[1,2,3],[4,5,6]])
 matrix2=Matrix([[7,8],[9,10],[11,12]])
 result_matrix=matrix1.multiply(matrix2)
 print(result_matrix)
```
### 输出结果
```
58 64
139 154
```
源链接: [https://www.runoob.com/python3/python-matrix-multiplication-class.html](https://www.runoob.com/python3/python-matrix-multiplication-class.html)