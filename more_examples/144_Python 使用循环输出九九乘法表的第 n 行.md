# Python 使用循环输出九九乘法表的第 n 行

## 题目描述
Python3 实例
我们可以使用 Python 编写一个简单的循环来输出九九乘法表的第 n 行。假设 n 是一个整数，表示乘法表的行号（1 到 9），我们可以通过循环来生成该行的乘法结果。

## 实例
### 代码
```python
defprint_multiplication_table_row(n):
     foriinrange(1,10):
         print(f"{n} * {i} = {n * i}")
 # 示例：输出第 3 行
 print_multiplication_table_row(3)
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
源链接: [https://www.runoob.com/python3/python-multiplication-row-n.html](https://www.runoob.com/python3/python-multiplication-row-n.html)