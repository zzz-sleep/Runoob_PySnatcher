# Python 打印斐波那契数列

## 题目描述
Python3 实例
斐波那契数列是一个经典的数学问题，其中每个数字是前两个数字的和。数列的前两个数字通常定义为 0 和 1。我们可以使用 Python 编写一个简单的程序来打印斐波那契数列的前 n 项。

## 实例
### 代码
```python
deffibonacci(n):
     fib_sequence=[]
     a,b=0,1
     for_inrange(n):
         fib_sequence.append(a)
         a,b=b,a + b
     returnfib_sequence
 n=10# 打印前10项
 print(fibonacci(n))
```
### 输出结果
```
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```
源链接: [https://www.runoob.com/python3/python-fibonacci-sequence.html](https://www.runoob.com/python3/python-fibonacci-sequence.html)