# Python 使用 lambda 表达式进行列表排序

## 题目描述
Python3 实例
在 Python 中，lambda 表达式是一种创建匿名函数的方式，通常用于需要一个简单函数但不想正式定义一个函数的场合。使用 lambda 表达式可以方便地对列表进行排序，尤其是在需要根据某个特定的条件或属性进行排序时。
下面是一个使用 lambda 表达式对列表进行排序的示例：

## 实例
### 代码
```python
# 定义一个包含元组的列表，每个元组包含姓名和年龄
 people=[('Alice',25),('Bob',20),('Charlie',30),('David',22)]
 # 使用 lambda 表达式根据年龄进行排序
 sorted_people=sorted(people,key=lambdax: x[1])
 print(sorted_people)
```
### 输出结果
```

[('Bob', 20), ('David', 22), ('Alice', 25), ('Charlie', 30)]
```
源链接: [https://www.runoob.com/python3/python-lambda-sort.html](https://www.runoob.com/python3/python-lambda-sort.html)