# Python 实现一个 Person 类，支持更新名字和年龄

## 题目描述
Python3 实例
我们将创建一个简单的Person类，该类包含两个属性：name和age。我们将为这个类添加两个方法：update_name和update_age，用于更新name和age属性。

## 实例
### 代码
```python
classPerson:
     def__init__(self,name,age):
         self.name=name
         self.age=age
     defupdate_name(self,new_name):
         self.name=new_name
     defupdate_age(self,new_age):
         self.age=new_age
     def__str__(self):
         returnf"Person(name={self.name}, age={self.age})"
 # 示例使用
 person=Person("Alice",30)
 print(person)
 person.update_name("Bob")
 person.update_age(25)
 print(person)
```
### 输出结果
```
Person(name=Alice, age=30)
Person(name=Bob, age=25)
```
源链接: [https://www.runoob.com/python3/python-update-person.html](https://www.runoob.com/python3/python-update-person.html)