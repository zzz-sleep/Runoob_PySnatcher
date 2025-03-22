# Python 判断列表中是否包含重复元素

## 题目描述
Python3 实例
在 Python 中，我们可以通过将列表转换为集合（set）来判断列表中是否包含重复元素。因为集合中的元素是唯一的，如果列表中有重复元素，转换为集合后，集合的长度会小于列表的长度。

## 实例
### 代码
```python
defhas_duplicates(lst):
     returnlen(lst)!=len(set(lst))
 # 示例列表
 example_list=[1,2,3,4,5,2]
 # 调用函数
 result=has_duplicates(example_list)
 print(result)
```
### 输出结果
```
True
```
源链接: [https://www.runoob.com/python3/python-list-duplicates-check.html](https://www.runoob.com/python3/python-list-duplicates-check.html)