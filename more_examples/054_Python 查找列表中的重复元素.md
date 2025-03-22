# Python 查找列表中的重复元素

## 题目描述
Python3 实例
在 Python 中，查找列表中的重复元素可以通过多种方式实现。一种常见的方法是使用集合（set）来存储已经出现过的元素，然后遍历列表，检查每个元素是否已经存在于集合中。如果存在，则该元素是重复的。

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
 my_list=[1,2,3,2,4,5,3,6,7,8,5]
 print(find_duplicates(my_list))
```
### 输出结果
```
未找到输出结果
```
## 实例
### 代码
```python
[2,3,5]
```
### 输出结果
```
未找到输出结果
```
源链接: [https://www.runoob.com/python3/python-find-duplicates-list.html](https://www.runoob.com/python3/python-find-duplicates-list.html)