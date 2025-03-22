# Python 编写一个程序实现矩阵乘法

## 题目描述
Python3 实例
矩阵乘法是线性代数中的一个基本操作。给定两个矩阵 A 和 B，矩阵乘法的结果是一个新的矩阵 C，其中 C 的每个元素是 A 的对应行与 B 的对应列的点积。假设 A 是一个 m×n 的矩阵，B 是一个 n×p 的矩阵，那么结果矩阵 C 将是一个 m×p 的矩阵。

## 实例
### 代码
```python
defmatrix_multiply(A,B):
     # 获取矩阵 A 和 B 的维度
     rows_A=len(A)
     cols_A=len(A[0])
     rows_B=len(B)
     cols_B=len(B[0])
     # 检查矩阵 A 的列数是否等于矩阵 B 的行数
     ifcols_A!=rows_B:
         raiseValueError("矩阵 A 的列数必须等于矩阵 B 的行数")
     # 初始化结果矩阵 C，大小为 rows_A x cols_B
     C=[[0for_inrange(cols_B)]for_inrange(rows_A)]
     # 进行矩阵乘法
     foriinrange(rows_A):
         forjinrange(cols_B):
             forkinrange(cols_A):
                 C[i][j]+=A[i][k]* B[k][j]
     returnC
 # 示例矩阵
 A=[[1,2,3],
      [4,5,6]]
 B=[[7,8],
      [9,10],
      [11,12]]
 # 调用矩阵乘法函数
 result=matrix_multiply(A,B)
 # 输出结果
 forrowinresult:
     print(row)
```
### 输出结果
```
[58, 64]
[139, 154]
```
源链接: [https://www.runoob.com/python3/python-matrix-multiplication.html](https://www.runoob.com/python3/python-matrix-multiplication.html)