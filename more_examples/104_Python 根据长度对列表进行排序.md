# Python 根据长度对列表进行排序

## 题目描述
Python3 实例
在 Python 中，我们可以使用sorted()函数或list.sort()方法对列表进行排序。如果我们想根据列表中元素的长度进行排序，可以通过指定key参数来实现。key参数接受一个函数，该函数会作用于列表中的每个元素，并根据函数的返回值进行排序。

## 实例
### 代码
```python
# 定义一个包含字符串的列表
 words=["apple","banana","kiwi","cherry","mango"]
 # 使用 sorted() 函数根据字符串长度对列表进行排序
 sorted_words=sorted(words,key=len)
 # 输出排序后的列表
 print(sorted_words)
```
### 输出结果
```

['kiwi', 'mango', 'apple', 'cherry', 'banana']
```
源链接: [https://www.runoob.com/python3/python-sort-by-length.html](https://www.runoob.com/python3/python-sort-by-length.html)