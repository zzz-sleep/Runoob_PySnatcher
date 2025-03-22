# Python 移除列表中重复的元素

## 题目描述
Python3 实例
本章节我们将学习如何从列表中删除重复的元素。
知识点有：

## 实例
### 代码
```python
list_1=[1,2,1,4,6]
 print(list(set(list_1)))
```
### 输出结果
```

[1, 2, 4, 6]

```
## 实例
### 代码
```python
# 使用辅助集合保持顺序地去重
 defremove_duplicates(lst):
     seen=set()
     unique_list=[]
     foriteminlst:
         ifitemnotinseen:
             seen.add(item)
             unique_list.append(item)
     returnunique_list
 # 示例
 original_list=[1,2,2,3,4,4,5]
 unique_list=remove_duplicates(original_list)
 print(unique_list)# 输出: [1, 2, 3, 4, 5]
```
### 输出结果
```

[1, 2, 3, 4, 5]
```
## 实例
### 代码
```python
# 使用dict.fromkeys()保持顺序地去重
 defremove_duplicates(lst):
     returnlist(dict.fromkeys(lst))
 # 示例
 original_list=[1,2,2,3,4,4,5]
 unique_list=remove_duplicates(original_list)
 print(unique_list)# 输出: [1, 2, 3, 4, 5]
```
### 输出结果
```

[1, 2, 3, 4, 5]
```
## 实例
### 代码
```python
# 使用列表推导式去重
 defremove_duplicates(lst):
     unique_list=[]
     [unique_list.append(item)foriteminlstifitemnotinunique_list]
     returnunique_list
 # 示例
 original_list=[1,2,2,3,4,4,5]
 unique_list=remove_duplicates(original_list)
 print(unique_list)# 输出: [1, 2, 3, 4, 5]
```
### 输出结果
```

[4, 6, 7, 8]

```
## 实例
### 代码
```python
list_1=[1,2,1,4,6]
 list_2=[7,8,2,1]
 print(list(set(list_1)^set(list_2)))
```
### 输出结果
```

[4, 6, 7, 8]

```
源链接: [https://www.runoob.com/python3/python-remove-duplicate-from-list.html](https://www.runoob.com/python3/python-remove-duplicate-from-list.html)