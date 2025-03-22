# Python 从字典中获取最大值

## 题目描述
Python3 实例
在 Python 中，我们可以使用内置的max()函数来从字典中获取最大值。max()函数可以接受一个可迭代对象，并返回其中的最大值。对于字典，我们可以通过指定key参数来决定是基于键还是值来获取最大值。
假设我们有一个字典，我们想要获取值最大的键值对。

## 实例
### 代码
```python
my_dict={'a':10,'b':20,'c':5}
 max_key=max(my_dict,key=my_dict.get)
 max_value=my_dict[max_key]
 print(f"Key with maximum value: {max_key}, Maximum value: {max_value}")
```
### 输出结果
```
Key with maximum value: b, Maximum value: 20
```
源链接: [https://www.runoob.com/python3/python-max-dictionary.html](https://www.runoob.com/python3/python-max-dictionary.html)