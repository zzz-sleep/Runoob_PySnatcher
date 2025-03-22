# Python 使用递归打印斐波那契数列

## 题目描述
Python3 实例
斐波那契数列是一个经典的递归问题，其中每个数字是前两个数字的和。数列的前两个数字通常是 0 和 1。我们可以使用递归函数来生成斐波那契数列。

## 实例
### 代码
```python
deffibonacci(n):
     ifn<=0:
         return[]
     elifn==1:
         return[0]
     elifn==2:
         return[0,1]
     else:
         fib_sequence=fibonacci(n -1)
         fib_sequence.append(fib_sequence[-1]+ fib_sequence[-2])
         returnfib_sequence
 # 打印前 10 个斐波那契数列
 print(fibonacci(10))
```
### 输出结果
```
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```
源链接: [https://www.runoob.com/python3/python-recursive-fibonacci.html](https://www.runoob.com/python3/python-recursive-fibonacci.html)