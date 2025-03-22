# 使用 Python 实现一个计数器类，支持加减操作

## 题目描述
Python3 实例
我们将创建一个简单的计数器类Counter，它支持增加和减少计数值的操作。这个类将包含一个内部变量count来存储当前的计数值，并提供increment和decrement方法来分别增加和减少计数值。

## 实例
### 代码
```python
classCounter:
     def__init__(self,initial_count=0):
         self.count=initial_count
     defincrement(self,value=1):
         self.count+=value
     defdecrement(self,value=1):
         self.count-=value
     defget_count(self):
         returnself.count
 # 示例使用
 counter=Counter(10)
 counter.increment(5)
 counter.decrement(3)
 print(counter.get_count())
```
### 输出结果
```
12
```
源链接: [https://www.runoob.com/python3/python-counter-class.html](https://www.runoob.com/python3/python-counter-class.html)