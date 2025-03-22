# Python 交换两个变量的值

## 题目描述
Python3 实例
在 Python 中，交换两个变量的值可以通过多种方式实现。最常见的方法是使用一个临时变量来存储其中一个变量的值，然后再进行交换。此外，Python 还提供了一种更简洁的方式，即使用元组解包来交换变量的值。

## 实例
### 代码
```python
a=5
 b=10
 # 使用临时变量交换
 temp=a
 a=b
 b=temp
 print("交换后 a 的值:",a)
 print("交换后 b 的值:",b)
```
### 输出结果
```
交换后 a 的值: 10
交换后 b 的值: 5
```
## 实例
### 代码
```python
a=5
 b=10
 # 使用元组解包交换
 a,b=b,a
 print("交换后 a 的值:",a)
 print("交换后 b 的值:",b)
```
### 输出结果
```
交换后 a 的值: 10
交换后 b 的值: 5
```
源链接: [https://www.runoob.com/python3/python-swap-variables.html](https://www.runoob.com/python3/python-swap-variables.html)