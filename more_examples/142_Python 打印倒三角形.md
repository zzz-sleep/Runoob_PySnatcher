# Python 打印倒三角形

## 题目描述
Python3 实例
在 Python 中，我们可以使用嵌套循环来打印一个倒三角形。外层循环控制行数，内层循环控制每行打印的星号数量。随着行数的增加，每行的星号数量逐渐减少。

## 实例
### 代码
```python
n=5# 定义倒三角形的高度
 foriinrange(n,0,-1):
     forjinrange(i):
         print("*",end=" ")
     print()
```
### 输出结果
```
* * * * * 
* * * * 
* * * 
* * 
* 
```
源链接: [https://www.runoob.com/python3/python-print-inverted-triangle.html](https://www.runoob.com/python3/python-print-inverted-triangle.html)