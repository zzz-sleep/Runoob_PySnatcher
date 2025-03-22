# Python 创建一个类并实例化它

## 题目描述
Python3 实例
在 Python 中，类是一种用于创建对象的蓝图或模板。通过定义类，我们可以创建具有相同属性和方法的多个对象。下面是一个简单的例子，展示如何创建一个类并实例化它。

## 实例
### 代码
```python
classDog:
     def__init__(self,name,age):
         self.name=name
         self.age=age
     defbark(self):
         returnf"{self.name} says woof!"
 # 实例化类
 my_dog=Dog("Buddy",3)
 # 访问属性和调用方法
 print(my_dog.name)
 print(my_dog.age)
 print(my_dog.bark())
```
### 输出结果
```
Buddy
3
Buddy says woof!
```
源链接: [https://www.runoob.com/python3/python-create-class.html](https://www.runoob.com/python3/python-create-class.html)