# Python 创建一个多继承的类

## 题目描述
Python3 实例
在 Python 中，多继承是指一个类可以继承多个父类。通过多继承，子类可以继承多个父类的属性和方法。下面是一个简单的例子，展示了如何创建一个多继承的类。

## 实例
### 代码
```python
classParent1:
     defmethod1(self):
         print("This is method1 from Parent1")
 classParent2:
     defmethod2(self):
         print("This is method2 from Parent2")
 classChild(Parent1,Parent2):
     defmethod3(self):
         print("This is method3 from Child")
 # 创建 Child 类的实例
 child=Child()
 # 调用继承自 Parent1 的方法
 child.method1()
 # 调用继承自 Parent2 的方法
 child.method2()
 # 调用 Child 类自己的方法
 child.method3()
```
### 输出结果
```
This is method1 from Parent1
This is method2 from Parent2
This is method3 from Child
```
源链接: [https://www.runoob.com/python3/python-multiple-inheritance.html](https://www.runoob.com/python3/python-multiple-inheritance.html)