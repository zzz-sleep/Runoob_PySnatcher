# Python 写一个程序打印九九乘法表

## 题目描述
Python3 实例
九九乘法表是一个经典的编程练习，它展示了从1到9的数字相互相乘的结果。我们将使用嵌套的for循环来实现这个功能。

## 实例
### 代码
```python
foriinrange(1,10):
     forjinrange(1,i+1):
         print(f"{j}x{i}={i*j}",end="t")
     print()
```
### 输出结果
```
1x1=1   
1x2=2   2x2=4   
1x3=3   2x3=6   3x3=9   
1x4=4   2x4=8   3x4=12  4x4=16  
1x5=5   2x5=10  3x5=15  4x5=20  5x5=25  
1x6=6   2x6=12  3x6=18  4x6=24  5x6=30  6x6=36  
1x7=7   2x7=14  3x7=21  4x7=28  5x7=35  6x7=42  7x7=49  
1x8=8   2x8=16  3x8=24  4x8=32  5x8=40  6x8=48  7x8=56  8x8=64  
1x9=9   2x9=18  3x9=27  4x9=36  5x9=45  6x9=54  7x9=63  8x9=72  9x9=81  
```
源链接: [https://www.runoob.com/python3/python-multiplication-table.html](https://www.runoob.com/python3/python-multiplication-table.html)