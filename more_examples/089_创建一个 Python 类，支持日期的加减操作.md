# 创建一个 Python 类，支持日期的加减操作

## 题目描述
Python3 实例
我们将创建一个 Python 类Date，该类支持日期的加减操作。我们将使用datetime模块来处理日期的加减操作，并确保日期的格式正确。

## 实例
### 代码
```python
fromdatetimeimportdatetime,timedelta
 classDate:
     def__init__(self,year,month,day):
         self.date=datetime(year,month,day)
     def__add__(self,days):
         new_date=self.date+ timedelta(days=days)
         returnDate(new_date.year,new_date.month,new_date.day)
     def__sub__(self,days):
         new_date=self.date- timedelta(days=days)
         returnDate(new_date.year,new_date.month,new_date.day)
     def__str__(self):
         returnself.date.strftime('%Y-%m-%d')
 # 示例使用
 date=Date(2023,10,1)
 print("初始日期:",date)
 date_plus_10=date +10
 print("加 10 天后的日期:",date_plus_10)
 date_minus_5=date -5
 print("减 5 天后的日期:",date_minus_5)
```
### 输出结果
```
初始日期: 2023-10-01
加 10 天后的日期: 2023-10-11
减 5 天后的日期: 2023-09-26
```
源链接: [https://www.runoob.com/python3/python-date-operations.html](https://www.runoob.com/python3/python-date-operations.html)