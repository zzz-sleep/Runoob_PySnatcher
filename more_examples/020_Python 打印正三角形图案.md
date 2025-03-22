# Python 打印正三角形图案

## 题目描述
Python3 实例
我们将使用 Python 编写一个简单的程序来打印一个正三角形图案。这个图案由星号（*）组成，每一行的星号数量逐渐增加，形成一个正三角形。

## 实例
### 代码
```python
defprint_triangle(n):
     foriinrange(n):
         print(' '*(n - i -1)+'*'*(2* i +1))
 # 调用函数打印一个高度为5的正三角形
 print_triangle(5)
```
### 输出结果
```
    *
   ***
  *****
 *******
*********
```
源链接: [https://www.runoob.com/python3/python-print-triangle-pattern.html](https://www.runoob.com/python3/python-print-triangle-pattern.html)