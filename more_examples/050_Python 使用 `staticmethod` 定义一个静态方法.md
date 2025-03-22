# Python 使用 `staticmethod` 定义一个静态方法

## 题目描述
Python3 实例
在 Python 中，staticmethod是一个装饰器，用于定义一个静态方法。静态方法不依赖于类的实例，也不依赖于类本身。它们通常用于执行与类相关但不依赖于类或实例状态的操作。
下面是一个使用staticmethod定义静态方法的示例：

## 实例
### 代码
```python
classMyClass:
     @staticmethod
     defmy_static_method():
         return"This is a static method."
 # 调用静态方法
 result=MyClass.my_static_method()
 print(result)
```
### 输出结果
```
This is a static method.
```
源链接: [https://www.runoob.com/python3/python-staticmethod.html](https://www.runoob.com/python3/python-staticmethod.html)