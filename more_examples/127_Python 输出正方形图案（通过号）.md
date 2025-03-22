# Python 输出正方形图案（通过*号）

## 题目描述
Python3 实例
在这个例子中，我们将使用 Python 编写一个简单的程序来输出一个由星号（*）组成的正方形图案。用户将输入正方形的边长，程序将根据输入的边长打印出相应的正方形。

## 实例
### 代码
```python
# 获取用户输入的正方形边长
 side_length=int(input("请输入正方形的边长: "))
 # 使用嵌套循环打印正方形
 foriinrange(side_length):
     forjinrange(side_length):
         print("*",end=" ")
     print()
```
### 输出结果
```
* * * * 
* * * * 
* * * * 
* * * * 
```
源链接: [https://www.runoob.com/python3/python-print-square-pattern.html](https://www.runoob.com/python3/python-print-square-pattern.html)