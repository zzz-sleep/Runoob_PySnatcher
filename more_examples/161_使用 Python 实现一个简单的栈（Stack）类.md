# 使用 Python 实现一个简单的栈（Stack）类

## 题目描述
Python3 实例
栈（Stack）是一种遵循后进先出（LIFO）原则的数据结构。我们可以使用 Python 的列表来实现一个简单的栈类。这个类将包含以下几个基本操作：

## 实例
### 代码
```python
classStack:
     def__init__(self):
         self.items=[]
     defis_empty(self):
         returnself.items==[]
     defpush(self,item):
         self.items.append(item)
     defpop(self):
         ifself.is_empty():
             raiseIndexError("pop from empty stack")
         returnself.items.pop()
     defpeek(self):
         ifself.is_empty():
             raiseIndexError("peek from empty stack")
         returnself.items[-1]
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
 stack=Stack()
 stack.push(1)
 stack.push(2)
 stack.push(3)
 print(stack.peek())# 输出: 3
 print(stack.pop())# 输出: 3
 print(stack.size())# 输出: 2
 print(stack.is_empty())# 输出: False
 stack.pop()
 stack.pop()
 print(stack.is_empty())# 输出: True
```
### 输出结果
```
未找到输出结果
```
源链接: [https://www.runoob.com/python3/python-stack-class.html](https://www.runoob.com/python3/python-stack-class.html)