# Python 查找列表中的最小值及其位置

## 题目描述
Python3 实例
在 Python 中，我们可以使用内置的min()函数来查找列表中的最小值。为了找到最小值的位置，我们可以使用index()方法。以下是一个示例代码，展示了如何查找列表中的最小值及其位置。

## 实例
### 代码
```python
# 定义一个列表
 numbers=[34,12,56,78,23,9]
 # 查找最小值
 min_value=min(numbers)
 # 查找最小值的位置
 min_index=numbers.index(min_value)
 # 输出结果
 print(f"列表中的最小值是: {min_value}")
 print(f"最小值的位置是: {min_index}")
```
### 输出结果
```
列表中的最小值是: 9
最小值的位置是: 5
```
源链接: [https://www.runoob.com/python3/python-min-value-position.html](https://www.runoob.com/python3/python-min-value-position.html)