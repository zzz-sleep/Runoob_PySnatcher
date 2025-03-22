# Python 反转列表

## 题目描述
Python3 实例
在 Python 中，反转列表可以通过多种方式实现。以下是几种常见的方法：
reverse()方法会直接修改原列表，将其元素顺序反转。

## 实例
### 代码
```python
my_list=[1,2,3,4,5]
 my_list.reverse()
 print(my_list)
```
### 输出结果
```
[5, 4, 3, 2, 1]
```
## 实例
### 代码
```python
my_list=[1,2,3,4,5]
 reversed_list=my_list[::-1]
 print(reversed_list)
```
### 输出结果
```
[5, 4, 3, 2, 1]
```
## 实例
### 代码
```python
my_list=[1,2,3,4,5]
 reversed_list=list(reversed(my_list))
 print(reversed_list)
```
### 输出结果
```
[5, 4, 3, 2, 1]
```
## 实例
### 代码
```python
my_list=[1,2,3,4,5]
 reversed_list=[]
 foriinrange(len(my_list)-1,-1,-1):
     reversed_list.append(my_list[i])
 print(reversed_list)
```
### 输出结果
```
[5, 4, 3, 2, 1]
```
源链接: [https://www.runoob.com/python3/python-reverse-list.html](https://www.runoob.com/python3/python-reverse-list.html)