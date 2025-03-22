# Python 用字符串连接列表元素

## 题目描述
Python3 实例
在 Python 中，我们可以使用join()方法来连接列表中的字符串元素。join()方法会将列表中的所有字符串元素连接成一个单一的字符串，并且可以在元素之间插入指定的分隔符。

## 实例
### 代码
```python
# 定义一个包含字符串的列表
 my_list=['Hello','World','Python']
 # 使用 join() 方法连接列表中的元素，并用空格作为分隔符
 result=' '.join(my_list)
 # 打印结果
 print(result)
```
### 输出结果
```
Hello World Python
```
源链接: [https://www.runoob.com/python3/python-join-list.html](https://www.runoob.com/python3/python-join-list.html)