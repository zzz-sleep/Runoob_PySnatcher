# Python 实现一个函数，输出一个数字列表中的两个最大值

## 题目描述
Python3 实例
我们将编写一个 Python 函数，该函数接收一个数字列表作为输入，并返回该列表中的两个最大值。我们将使用简单的逻辑来实现这个功能。

## 实例
### 代码
```python
deffind_two_max(numbers):
     iflen(numbers)first_max:
             second_max=first_max
             first_max=number
         elifnumber &gt;second_max:
             second_max=number
     returnfirst_max,second_max
 # 示例使用
 numbers=[10,20,4,45,99,99]
 print(find_two_max(numbers))
```
### 输出结果
```
未找到输出结果
```
## 实例
### 代码
```python
(99,99)
```
### 输出结果
```
未找到输出结果
```
源链接: [https://www.runoob.com/python3/python-two-max-values.html](https://www.runoob.com/python3/python-two-max-values.html)