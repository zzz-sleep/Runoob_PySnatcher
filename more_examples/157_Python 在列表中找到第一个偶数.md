# Python 在列表中找到第一个偶数

## 题目描述
Python3 实例
在 Python 中，我们可以使用循环来遍历列表，找到第一个偶数并返回它。如果列表中没有偶数，我们可以返回一个提示信息。

## 实例
### 代码
```python
deffind_first_even(numbers):
     fornuminnumbers:
         ifnum %2==0:
             returnnum
     return"No even number found"
 # 示例列表
 numbers=[1,3,5,7,8,9]
 result=find_first_even(numbers)
 print(result)
```
### 输出结果
```
8
```
源链接: [https://www.runoob.com/python3/python-first-even.html](https://www.runoob.com/python3/python-first-even.html)