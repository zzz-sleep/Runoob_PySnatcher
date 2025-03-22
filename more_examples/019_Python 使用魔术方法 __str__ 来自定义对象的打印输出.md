# Python 使用魔术方法 __str__ 来自定义对象的打印输出

## 题目描述
Python3 实例
在 Python 中，魔术方法__str__用于定义对象的字符串表示形式。当你使用print()函数打印对象时，或者使用str()函数将对象转换为字符串时，Python 会自动调用这个方法来获取对象的字符串表示。
下面是一个简单的例子，展示如何使用__str__方法来自定义对象的打印输出。

## 实例
### 代码
```python
classPerson:
     def__init__(self,name,age):
         self.name=name
         self.age=age
     def__str__(self):
         returnf"Person(name={self.name}, age={self.age})"
 # 创建一个 Person 对象
 person=Person("Alice",30)
 # 打印对象
 print(person)
```
### 输出结果
```
Person(name=Alice, age=30)
```
源链接: [https://www.runoob.com/python3/python-custom-str.html](https://www.runoob.com/python3/python-custom-str.html)