# 使用 Python 计算两个日期之间的天数差

## 题目描述
Python3 实例
我们将使用 Python 的datetime模块来计算两个日期之间的天数差。datetime模块提供了处理日期和时间的类，我们可以使用date类来表示日期，并通过简单的减法操作来计算两个日期之间的天数差。

## 实例
### 代码
```python
fromdatetimeimportdate
 # 定义两个日期
 date1=date(2023,10,1)
 date2=date(2023,10,15)
 # 计算日期差
 delta=date2 - date1
 # 输出天数差
 print("两个日期之间的天数差是:",delta.days)
```
### 输出结果
```
两个日期之间的天数差是: 14
```
源链接: [https://www.runoob.com/python3/python-date-difference.html](https://www.runoob.com/python3/python-date-difference.html)