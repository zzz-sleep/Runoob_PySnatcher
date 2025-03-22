# Python 合并两个列表为一个

## 题目描述
Python3 实例
在 Python 中，合并两个列表为一个可以通过多种方式实现。最常见的方法是使用+运算符或extend()方法。下面是一个简单的示例，展示如何将两个列表合并为一个。

## 实例
### 代码
```python
list1=[1,2,3]
 list2=[4,5,6]
 # 使用 + 运算符合并列表
 merged_list=list1 + list2
 print("合并后的列表:",merged_list)
```
### 输出结果
```
合并后的列表: [1, 2, 3, 4, 5, 6]
```
## 实例
### 代码
```python
list1=[1,2,3]
 list2=[4,5,6]
 # 使用 extend() 方法合并列表
 list1.extend(list2)
 print("合并后的列表:",list1)
```
### 输出结果
```
合并后的列表: [1, 2, 3, 4, 5, 6]
```
源链接: [https://www.runoob.com/python3/python-merge-lists.html](https://www.runoob.com/python3/python-merge-lists.html)