# Python 将给定列表的元素按大小排序

## 题目描述
Python3 实例
在 Python 中，我们可以使用内置的sort()方法或sorted()函数来对列表中的元素进行排序。sort()方法会直接修改原列表，而sorted()函数会返回一个新的排序后的列表，原列表保持不变。

## 实例
### 代码
```python
# 定义一个列表
 numbers=[3,1,4,1,5,9,2,6,5,3,5]
 # 使用 sort() 方法对列表进行排序（原地排序）
 numbers.sort()
 print("使用 sort() 方法排序后的列表:",numbers)
 # 使用 sorted() 函数对列表进行排序（返回新列表）
 sorted_numbers=sorted(numbers)
 print("使用 sorted() 函数排序后的列表:",sorted_numbers)
```
### 输出结果
```
使用 sort() 方法排序后的列表: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
使用 sorted() 函数排序后的列表: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
```
源链接: [https://www.runoob.com/python3/python-sort-list.html](https://www.runoob.com/python3/python-sort-list.html)