# Python 删除列表中的重复元素

## 题目描述
Python3 实例
在 Python 中，我们可以使用多种方法来删除列表中的重复元素。常见的方法包括使用set数据结构、列表推导式以及dict.fromkeys()方法。下面我们将展示如何使用这些方法来删除列表中的重复元素。

## 实例
### 代码
```python
# 方法1: 使用 set
 original_list=[1,2,2,3,4,4,5]
 unique_list=list(set(original_list))
 print("方法1结果:",unique_list)
 # 方法2: 使用列表推导式
 original_list=[1,2,2,3,4,4,5]
 unique_list=[]
 [unique_list.append(x)forxinoriginal_listifxnotinunique_list]
 print("方法2结果:",unique_list)
 # 方法3: 使用 dict.fromkeys()
 original_list=[1,2,2,3,4,4,5]
 unique_list=list(dict.fromkeys(original_list))
 print("方法3结果:",unique_list)
```
### 输出结果
```
方法1结果: [1, 2, 3, 4, 5]
方法2结果: [1, 2, 3, 4, 5]
方法3结果: [1, 2, 3, 4, 5]
```
源链接: [https://www.runoob.com/python3/python-remove-duplicates.html](https://www.runoob.com/python3/python-remove-duplicates.html)