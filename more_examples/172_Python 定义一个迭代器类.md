# Python 定义一个迭代器类

## 题目描述
Python3 实例
在 Python 中，迭代器是一个可以记住遍历的位置的对象。迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。要创建一个迭代器类，我们需要实现__iter__()和__next__()方法。

## 实例
### 代码
```python
classMyIterator:
     def__init__(self,start,end):
         self.current=start
         self.end=end
     def__iter__(self):
         returnself
     def__next__(self):
         ifself.current<self.end:
             num=self.current
             self.current+=1
             returnnum
         else:
             raiseStopIteration
 # 使用迭代器
 my_iter=MyIterator(1,5)
 fornuminmy_iter:
     print(num)
```
### 输出结果
```
1
2
3
4
```
源链接: [https://www.runoob.com/python3/python-iterator-class.html](https://www.runoob.com/python3/python-iterator-class.html)