# Python 使用集合找出两个列表的交集

## 题目描述
Python3 实例
在 Python 中，集合（set）是一种无序且不重复的数据结构。我们可以利用集合的特性来找出两个列表的交集。交集指的是两个列表中共同存在的元素。

## 实例
### 代码
```python
list1=[1,2,3,4,5]
 list2=[4,5,6,7,8]
 # 将列表转换为集合
 set1=set(list1)
 set2=set(list2)
 # 使用集合的交集操作
 intersection=set1 &amp;set2
 # 将结果转换回列表
 result=list(intersection)
 print(result)
```
### 输出结果
```
[4, 5]
```
源链接: [https://www.runoob.com/python3/python-list-intersection.html](https://www.runoob.com/python3/python-list-intersection.html)