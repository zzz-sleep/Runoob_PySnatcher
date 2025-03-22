# Python 实现一个类，通过 __repr__ 法返回自定义对象的描述

## 题目描述
Python3 实例
我们将创建一个简单的类Person，并通过__repr__方法返回该对象的自定义描述。__repr__方法通常用于生成一个对象的"官方"字符串表示，通常用于调试和日志记录。

## 实例
### 代码
```python
classPerson:
     def__init__(self,name,age):
         self.name=name
         self.age=age
     def__repr__(self):
         returnf"Person(name={self.name}, age={self.age})"
 # 创建一个 Person 对象
 person=Person("Alice",30)
 # 打印对象的描述
 print(person)
```
### 输出结果
```
Person(name=Alice, age=30)
```
源链接: [https://www.runoob.com/python3/python-custom-repr.html](https://www.runoob.com/python3/python-custom-repr.html)