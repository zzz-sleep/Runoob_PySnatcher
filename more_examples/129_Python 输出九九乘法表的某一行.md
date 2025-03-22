# Python 输出九九乘法表的某一行

## 题目描述
Python3 实例
我们可以编写一个 Python 函数来输出九九乘法表的某一行。这个函数将接受一个参数n，表示要输出的行数（1 到 9 之间）。函数将输出该行的乘法表内容。

## 实例
### 代码
```python
defprint_multiplication_row(n):
     foriinrange(1,10):
         print(f"{n} * {i} = {n * i}")
```
### 输出结果
```
3 * 1 = 3
3 * 2 = 6
3 * 3 = 9
3 * 4 = 12
3 * 5 = 15
3 * 6 = 18
3 * 7 = 21
3 * 8 = 24
3 * 9 = 27
```
源链接: [https://www.runoob.com/python3/python-multiplication-row.html](https://www.runoob.com/python3/python-multiplication-row.html)