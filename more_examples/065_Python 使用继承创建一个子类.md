# Python 使用继承创建一个子类

## 题目描述
Python3 实例
在 Python 中，继承是面向对象编程的一个重要特性。通过继承，子类可以继承父类的属性和方法，并且可以在子类中添加新的属性和方法，或者重写父类的方法。下面是一个简单的例子，展示了如何使用继承创建一个子类。

## 实例
### 代码
```python
# 定义一个父类
 classAnimal:
     def__init__(self,name):
         self.name=name
     defspeak(self):
         returnf"{self.name} makes a sound."
 # 定义一个子类，继承自 Animal
 classDog(Animal):
     defspeak(self):
         returnf"{self.name} barks."
 # 创建父类的实例
 animal=Animal("Generic Animal")
 print(animal.speak())
 # 创建子类的实例
 dog=Dog("Buddy")
 print(dog.speak())
```
### 输出结果
```
Generic Animal makes a sound.
Buddy barks.
```
源链接: [https://www.runoob.com/python3/python-subclass-inheritance.html](https://www.runoob.com/python3/python-subclass-inheritance.html)