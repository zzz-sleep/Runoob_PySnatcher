# Python 创建一个 Flask 或 Django 应用

## 题目描述
Python3 实例
我们将创建一个简单的 Flask 应用，这个应用将有一个主页，当用户访问主页时，会显示 "Hello, World!"。

## 实例
### 代码
```python
fromflaskimportFlask
 app=Flask(__name__)
 @app.route('/')
 defhome():
     return"Hello, World!"
 if__name__=='__main__':
     app.run(debug=True)
```
### 输出结果
```
未找到输出结果
```
源链接: [https://www.runoob.com/python3/python-flask-django.html](https://www.runoob.com/python3/python-flask-django.html)