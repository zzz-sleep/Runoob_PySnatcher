# Python 定义一个子类继承父类，并在子类中重写一个方法

## 题目描述
Python3 实例
在 Python 中，我们可以通过定义一个子类来继承父类，并在子类中重写父类的方法。子类可以继承父类的所有属性和方法，同时可以根据需要重写父类的方法来实现不同的功能。

## 实例
### 代码
```python
# 定义一个父类
 classAnimal:
     defspeak(self):
         print("Animal speaks")
 # 定义一个子类继承父类
 classDog(Animal):
     # 重写父类的 speak 方法
     defspeak(self):
         print("Dog barks")
 # 创建父类对象
 animal=Animal()
 animal.speak()
 # 创建子类对象
 dog=Dog()
 dog.speak()
```
### 输出结果
```
Animal speaks
Dog barks
```
源链接: [https://www.runoob.com/python3/python-method-override.html](https://www.runoob.com/python3/python-method-override.html)