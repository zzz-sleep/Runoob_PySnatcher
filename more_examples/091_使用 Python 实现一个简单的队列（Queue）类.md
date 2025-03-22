# 使用 Python 实现一个简单的队列（Queue）类

## 题目描述
Python3 实例
队列（Queue）是一种先进先出（FIFO）的数据结构。我们可以使用 Python 的列表来实现一个简单的队列类。这个类将包含以下几个基本操作：

## 实例
### 代码
```python
classQueue:
     def__init__(self):
         self.items=[]
     defis_empty(self):
         returnself.items==[]
     defenqueue(self,item):
         self.items.append(item)
     defdequeue(self):
         ifself.is_empty():
             returnNone
         returnself.items.pop(0)
     defsize(self):
         returnlen(self.items)
```
### 输出结果
```
未找到输出结果
```
## 实例
### 代码
```python
# 示例使用
 q=Queue()
 q.enqueue(1)
 q.enqueue(2)
 q.enqueue(3)
 print(q.dequeue())# 输出: 1
 print(q.size())# 输出: 2
 print(q.is_empty())# 输出: False
```
### 输出结果
```
未找到输出结果
```
源链接: [https://www.runoob.com/python3/python-queue-class.html](https://www.runoob.com/python3/python-queue-class.html)