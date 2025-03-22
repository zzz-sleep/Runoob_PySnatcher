# Python 删除列表中的指定元素

## 题目描述
Python3 实例
在 Python 中，如果你想删除列表中的指定元素，可以使用remove()方法。这个方法会删除列表中第一个匹配的元素。如果列表中有多个相同的元素，只有第一个会被删除。

## 实例
### 代码
```python
# 创建一个包含多个元素的列表
 my_list=[1,2,3,4,3,5]
 # 删除列表中的元素 3
 my_list.remove(3)
 # 打印修改后的列表
 print(my_list)
```
### 输出结果
```

[1, 2, 4, 3, 5]
```
源链接: [https://www.runoob.com/python3/python-remove-element.html](https://www.runoob.com/python3/python-remove-element.html)