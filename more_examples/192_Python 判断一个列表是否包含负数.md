# Python 判断一个列表是否包含负数

## 题目描述
Python3 实例
我们可以通过遍历列表中的每个元素来判断列表中是否包含负数。如果找到任何一个负数，就可以立即返回True，否则返回False。

## 实例
### 代码
```python
defcontains_negative(numbers):
     fornuminnumbers:
         ifnum<0:
             returnTrue
     returnFalse
 # 测试用例
 numbers=[1,2,3,-4,5]
 result=contains_negative(numbers)
 print(result)
```
### 输出结果
```
True
```
源链接: [https://www.runoob.com/python3/python-negative-check.html](https://www.runoob.com/python3/python-negative-check.html)