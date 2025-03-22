# Python 将时间戳转换为指定格式日期

## 题目描述
Python3 实例
给定一个时间戳，将其转换为指定格式的时间。
注意时区的设置。

## 实例 1
### 代码
```python
importtime# 获得当前时间时间戳now=int(time.time())#转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"timeArray=time.localtime(now)otherStyleTime=time.strftime("%Y-%m-%d %H:%M:%S",timeArray)print(otherStyleTime)
```
### 输出结果
```

2019-05-21 18:02:49

```
## 实例 2
### 代码
```python
importdatetime# 获得当前时间now=datetime.datetime.now()# 转换为指定的格式otherStyleTime=now.strftime("%Y-%m-%d %H:%M:%S")print(otherStyleTime)
```
### 输出结果
```

2019-05-21 18:03:48

```
## 实例 3
### 代码
```python
importtimetimeStamp=1557502800timeArray=time.localtime(timeStamp)otherStyleTime=time.strftime("%Y-%m-%d %H:%M:%S",timeArray)print(otherStyleTime)
```
### 输出结果
```

2019-05-10 23:40:00

```
## 实例 4
### 代码
```python
importdatetimetimeStamp=1557502800dateArray=datetime.datetime.utcfromtimestamp(timeStamp)otherStyleTime=dateArray.strftime("%Y-%m-%d %H:%M:%S")print(otherStyleTime)
```
### 输出结果
```

2019-05-10 23:40:00

```
源链接: [https://www.runoob.com/python3/python-timstamp-str.html](https://www.runoob.com/python3/python-timstamp-str.html)