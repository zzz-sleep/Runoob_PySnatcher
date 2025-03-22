# Python 合并字典

## 题目描述
Python3 实例
给定两个字典，然后将它们合并为一个字典。

## 实例 1 : 使用 update() 方法，第二个参数合并第一个参数
### 代码
```python
defMerge(dict1,dict2):return(dict2.update(dict1))# 两个字典dict1= {'a':10,'b':8}dict2= {'d':6,'c':4}# 返回  Noneprint(Merge(dict1,dict2))# dict2 合并了 dict1print(dict2)
```
### 输出结果
```

None
{'d': 6, 'c': 4, 'a': 10, 'b': 8}

```
## 实例 2 : 使用  **，函数将参数以字典的形式导入
### 代码
```python
defMerge(dict1,dict2):res= {**dict1, **dict2}returnres# 两个字典dict1= {'a':10,'b':8}dict2= {'d':6,'c':4}dict3=Merge(dict1,dict2)print(dict3)
```
### 输出结果
```

{'a': 10, 'b': 8, 'd': 6, 'c': 4}

```
源链接: [https://www.runoob.com/python3/python-merging-two-dictionaries.html](https://www.runoob.com/python3/python-merging-two-dictionaries.html)