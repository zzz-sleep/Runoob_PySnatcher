# Python 将两个列表合并成一个字典

## 题目描述
Python3 实例
假设我们有两个列表，一个包含键（keys），另一个包含值（values）。我们可以使用 Python 的zip函数将这两个列表合并成一个字典。

## 实例
### 代码
```python
keys=['name','age','city']
 values=['Alice',25,'New York']
 # 使用 zip 函数将两个列表合并成字典
 my_dict=dict(zip(keys,values))
 print(my_dict)
```
### 输出结果
```
未找到输出结果
```
## 实例
### 代码
```python
{'name':'Alice','age':25,'city':'New York'}
```
### 输出结果
```
未找到输出结果
```
源链接: [https://www.runoob.com/python3/python-list-to-dict.html](https://www.runoob.com/python3/python-list-to-dict.html)