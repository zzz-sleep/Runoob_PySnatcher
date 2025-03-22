# Python 判断一个数是否是偶数

## 题目描述
Python3 实例
在 Python 中，我们可以使用取模运算符%来判断一个数是否是偶数。如果一个数除以 2 的余数为 0，那么这个数就是偶数。

## 实例
### 代码
```python
defis_even(number):
     returnnumber %2==0
 # 测试
 num=4
 ifis_even(num):
     print(f"{num} 是偶数")
 else:
     print(f"{num} 不是偶数")
```
### 输出结果
```
4 是偶数
```
源链接: [https://www.runoob.com/python3/python-even-check.html](https://www.runoob.com/python3/python-even-check.html)