# Python 使用列表切片提取子列表

## 题目描述
Python3 实例
在 Python 中，列表切片是一种非常强大的功能，它允许你从一个列表中提取一部分元素，形成一个新的子列表。切片操作使用方括号[]和冒号:来指定起始索引、结束索引和步长。
假设我们有一个列表my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]，我们想要提取其中的一部分元素，可以使用切片操作。

## 实例
### 代码
```python
my_list=[0,1,2,3,4,5,6,7,8,9]
 # 提取索引 2 到 5 的元素（不包括索引 5）
 sub_list=my_list[2:5]
 print(sub_list)
```
### 输出结果
```

[2, 3, 4]
```
源链接: [https://www.runoob.com/python3/python-list-slicing.html](https://www.runoob.com/python3/python-list-slicing.html)