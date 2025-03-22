# Python 打印一个倒三角形的星号图案

## 题目描述
Python3 实例
我们将使用 Python 编写一个简单的程序来打印一个倒三角形的星号图案。这个图案将由多行星号组成，每行的星号数量逐渐减少。

## 实例
### 代码
```python
defprint_inverted_triangle(n):
     foriinrange(n,0,-1):
         print('*'* i)
 # 调用函数，打印一个5行的倒三角形
 print_inverted_triangle(5)
```
### 输出结果
```
*****
****
***
**
*
```
源链接: [https://www.runoob.com/python3/python-inverted-triangle.html](https://www.runoob.com/python3/python-inverted-triangle.html)