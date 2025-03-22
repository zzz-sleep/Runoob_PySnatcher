# Python 按字母顺序对字符串进行排序

## 题目描述
Python3 实例
在 Python 中，我们可以使用内置的sorted()函数对字符串中的字符按字母顺序进行排序。sorted()函数会返回一个列表，其中包含按升序排列的字符。如果我们想要得到一个排序后的字符串，可以使用join()方法将列表中的字符连接起来。

## 实例
### 代码
```python
# 原始字符串
 original_string="python"
 # 对字符串进行排序
 sorted_string=''.join(sorted(original_string))
 # 输出排序后的字符串
 print(sorted_string)
```
### 输出结果
```
hnopty
```
源链接: [https://www.runoob.com/python3/python-sort-string.html](https://www.runoob.com/python3/python-sort-string.html)