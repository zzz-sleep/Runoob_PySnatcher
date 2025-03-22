# Python 输出一个等腰三角形

## 题目描述
Python3 实例
我们将使用 Python 编写一个简单的程序来输出一个等腰三角形。这个三角形将由星号（*）组成，用户将输入三角形的高度，程序将根据高度输出相应的等腰三角形。

## 实例
### 代码
```python
defprint_triangle(height):
     foriinrange(height):
         # 打印前面的空格
         print(' '*(height - i -1),end='')
         # 打印星号
         print('*'*(2* i +1))
 # 用户输入三角形的高度
 height=int(input("请输入三角形的高度: "))
 print_triangle(height)
```
### 输出结果
```
    *
   ***
  *****
 *******
*********
```
源链接: [https://www.runoob.com/python3/python-print-triangle.html](https://www.runoob.com/python3/python-print-triangle.html)