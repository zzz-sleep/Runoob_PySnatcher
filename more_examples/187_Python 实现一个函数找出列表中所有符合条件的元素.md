# Python 实现一个函数找出列表中所有符合条件的元素

## 题目描述
Python3 实例
我们将编写一个 Python 函数，该函数接受一个列表和一个条件函数作为参数，并返回列表中所有符合条件的元素。条件函数将用于判断列表中的每个元素是否满足特定条件。

## 实例
### 代码
```python
deffind_elements(lst,condition):
     return[xforxinlstifcondition(x)]
 # 示例条件函数
 defis_even(n):
     returnn %2==0
 # 示例列表
 numbers=[1,2,3,4,5,6,7,8,9,10]
 # 使用函数找出所有偶数
 even_numbers=find_elements(numbers,is_even)
 print(even_numbers)
```
### 输出结果
```
[2, 4, 6, 8, 10]
```
源链接: [https://www.runoob.com/python3/python-filter-elements.html](https://www.runoob.com/python3/python-filter-elements.html)