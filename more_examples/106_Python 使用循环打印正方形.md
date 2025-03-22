# Python 使用循环打印正方形

## 题目描述
Python3 实例
我们可以使用 Python 的循环结构来打印一个正方形。假设我们要打印一个边长为 5 的正方形，可以使用嵌套循环来实现。外层循环控制行数，内层循环控制每行的星号数量。

## 实例
### 代码
```python
size=5
 foriinrange(size):
     forjinrange(size):
         print("*",end=" ")
     print()
```
### 输出结果
```
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
```
源链接: [https://www.runoob.com/python3/python-print-square.html](https://www.runoob.com/python3/python-print-square.html)