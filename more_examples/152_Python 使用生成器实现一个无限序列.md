# Python 使用生成器实现一个无限序列

## 题目描述
Python3 实例
在 Python 中，生成器是一种特殊的迭代器，它允许你按需生成值，而不是一次性生成所有值。生成器非常适合用于处理无限序列，因为它们只在需要时生成值，从而节省内存。
下面是一个使用生成器实现无限序列的示例，该序列从 0 开始，每次递增 1。

## 实例
### 代码
```python
definfinite_sequence():
     num=0
     whileTrue:
         yieldnum
         num +=1
```
### 输出结果
```
gen = infinite_sequence()
print(next(gen))  # 输出: 0
print(next(gen))  # 输出: 1
print(next(gen))  # 输出: 2
# 以此类推...
```
源链接: [https://www.runoob.com/python3/python-infinite-sequence.html](https://www.runoob.com/python3/python-infinite-sequence.html)