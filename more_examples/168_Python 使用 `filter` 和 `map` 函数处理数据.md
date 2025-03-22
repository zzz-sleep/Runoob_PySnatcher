# Python 使用 `filter` 和 `map` 函数处理数据

## 题目描述
Python3 实例
在 Python 中，filter和map是两个非常有用的内置函数，它们可以帮助我们以函数式编程的方式处理数据。filter函数用于过滤序列中的元素，而map函数用于对序列中的每个元素应用一个函数。
假设我们有一个包含数字的列表，我们想要过滤出所有的偶数，并将这些偶数乘以 2。我们可以使用filter和map函数来实现这个目标。

## 实例
### 代码
```python
# 定义一个包含数字的列表
 numbers=[1,2,3,4,5,6,7,8,9,10]
 # 使用 filter 函数过滤出偶数
 even_numbers=filter(lambdax: x %2==0,numbers)
 # 使用 map 函数将偶数乘以 2
 doubled_even_numbers=map(lambdax: x *2,even_numbers)
 # 将结果转换为列表并打印
 result=list(doubled_even_numbers)
 print(result)
```
### 输出结果
```
未找到输出结果
```
## 实例
### 代码
```python
[4,8,12,16,20]
```
### 输出结果
```
未找到输出结果
```
源链接: [https://www.runoob.com/python3/python-filter-map.html](https://www.runoob.com/python3/python-filter-map.html)