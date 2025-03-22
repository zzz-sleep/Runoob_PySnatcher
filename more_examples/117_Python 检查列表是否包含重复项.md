# Python 检查列表是否包含重复项

## 题目描述
Python3 实例
在 Python 中，我们可以通过将列表转换为集合来检查列表中是否包含重复项。集合是一种不允许重复元素的数据结构，因此如果列表的长度与集合的长度不同，则说明列表中包含重复项。

## 实例
### 代码
```python
defhas_duplicates(lst):
     returnlen(lst)!=len(set(lst))
 # 示例列表
 example_list=[1,2,3,4,5,2]
 # 检查是否有重复项
 ifhas_duplicates(example_list):
     print("列表包含重复项")
 else:
     print("列表不包含重复项")
```
### 输出结果
```
列表包含重复项
```
源链接: [https://www.runoob.com/python3/python-duplicate-check.html](https://www.runoob.com/python3/python-duplicate-check.html)