# Python 获取几天前的时间

## 题目描述
Python3 实例
计算几天前并转换为指定格式。

## 实例 1
### 代码
```python
importtimeimportdatetime# 先获得时间数组格式的日期threeDayAgo=(datetime.datetime.now()-datetime.timedelta(days=3))# 转换为时间戳timeStamp=int(time.mktime(threeDayAgo.timetuple()))# 转换为其他字符串格式otherStyleTime=threeDayAgo.strftime("%Y-%m-%d %H:%M:%S")print(otherStyleTime)
```
### 输出结果
```

2019-05-18 18:06:08

```
## 实例 2
### 代码
```python
importtimeimportdatetime#给定时间戳timeStamp=1557502800dateArray=datetime.datetime.utcfromtimestamp(timeStamp)threeDayAgo=dateArray-datetime.timedelta(days=3)print(threeDayAgo)
```
### 输出结果
```

2019-05-07 15:40:00

```
源链接: [https://www.runoob.com/python3/python-get-dayago.html](https://www.runoob.com/python3/python-get-dayago.html)