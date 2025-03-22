# Python 获取列表中的所有唯一元素

## 题目描述
Python3 实例
在 Python 中，我们可以使用多种方法来获取列表中的所有唯一元素。最常用的方法是使用set，因为集合（set）会自动去除重复的元素。下面是一个简单的示例：

## 实例
### 代码
```python
my_list=[1,2,2,3,4,4,5]
 unique_elements=list(set(my_list))
 print(unique_elements)
```
### 输出结果
```
[1, 2, 3, 4, 5]
```
## 实例
### 代码
```python
my_list=[1,2,2,3,4,4,5]
 unique_elements=list(dict.fromkeys(my_list))
 print(unique_elements)
```
### 输出结果
```
[1, 2, 3, 4, 5]
```
源链接: [https://www.runoob.com/python3/python-unique-elements.html](https://www.runoob.com/python3/python-unique-elements.html)