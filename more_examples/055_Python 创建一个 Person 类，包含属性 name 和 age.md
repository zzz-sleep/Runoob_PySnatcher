# Python 创建一个 Person 类，包含属性 name 和 age

## 题目描述
Python3 实例
我们将创建一个简单的Person类，该类包含两个属性：name和age。我们将为这个类定义一个构造函数来初始化这些属性，并添加一个方法来打印这些属性。

## 实例
### 代码
```python
classPerson:
     def__init__(self,name,age):
         self.name=name
         self.age=age
     defdisplay_info(self):
         print(f"Name: {self.name}, Age: {self.age}")
 # 创建一个 Person 对象
 person=Person("Alice",30)
 person.display_info()
```
### 输出结果
```
Name: Alice, Age: 30
```
源链接: [https://www.runoob.com/python3/python-person-class.html](https://www.runoob.com/python3/python-person-class.html)