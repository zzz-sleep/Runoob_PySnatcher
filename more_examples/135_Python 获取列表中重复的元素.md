# Python 获取列表中重复的元素

## 题目描述
Python3 实例
我们可以通过使用 Python 的集合（set）和列表（list）来获取列表中重复的元素。集合是一个无序且不重复的元素集，因此我们可以利用集合的特性来找出列表中的重复元素。

## 实例
### 代码
```python
deffind_duplicates(lst):
     seen=set()
     duplicates=set()
     foriteminlst:
         ifiteminseen:
             duplicates.add(item)
         else:
             seen.add(item)
     returnlist(duplicates)
 # 示例列表
 my_list=[1,2,3,2,4,5,3,6,7,8,7]
 print(find_duplicates(my_list))
```
### 输出结果
```
未找到输出结果
```
## 实例
### 代码
```python
[2,3,7]
```
### 输出结果
```
未找到输出结果
```
源链接: [https://www.runoob.com/python3/python-find-duplicates.html](https://www.runoob.com/python3/python-find-duplicates.html)