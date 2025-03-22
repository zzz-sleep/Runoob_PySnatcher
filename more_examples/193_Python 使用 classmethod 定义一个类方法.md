# Python 使用 classmethod 定义一个类方法

## 题目描述
Python3 实例
在 Python 中，classmethod是一个装饰器，用于定义类方法。类方法是绑定到类而不是实例的方法，可以通过类本身或类的实例来调用。类方法的第一个参数通常是cls，它代表类本身。
下面是一个使用classmethod定义类方法的示例：

## 实例
### 代码
```python
classMyClass:
     class_variable="This is a class variable"
     @classmethod
     defclass_method(cls):
         returnf"Class method called. Class variable: {cls.class_variable}"
 # 通过类调用类方法
 print(MyClass.class_method())
 # 通过实例调用类方法
 obj=MyClass()
 print(obj.class_method())
```
### 输出结果
```
Class method called. Class variable: This is a class variable
Class method called. Class variable: This is a class variable
```
源链接: [https://www.runoob.com/python3/python-classmethod.html](https://www.runoob.com/python3/python-classmethod.html)