# Python 实现一个装饰器函数

## 题目描述
Python3 实例
装饰器是 Python 中一种强大的工具，它允许你在不修改原函数代码的情况下，增加额外的功能。装饰器本质上是一个函数，它接受一个函数作为参数，并返回一个新的函数。

## 实例
### 代码
```python
defmy_decorator(func):
     defwrapper():
         print("Something is happening before the function is called.")
         func()
         print("Something is happening after the function is called.")
     returnwrapper
 @my_decorator
 defsay_hello():
     print("Hello!")
 say_hello()
```
### 输出结果
```
Something is happening before the function is called.
Hello!
Something is happening after the function is called.
```
源链接: [https://www.runoob.com/python3/python-decorator-function.html](https://www.runoob.com/python3/python-decorator-function.html)