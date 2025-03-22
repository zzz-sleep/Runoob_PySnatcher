# Python 将字符串的时间转换为时间戳

## 题目描述
Python3 实例
给定一个字符串的时间，将其转换为时间戳。

## 实例
### 代码
```python
importtimea1="2019-5-10 23:40:00"# 先转换为时间数组timeArray=time.strptime(a1,"%Y-%m-%d %H:%M:%S")# 转换为时间戳timeStamp=int(time.mktime(timeArray))print(timeStamp)# 格式转换 - 转为 /a2="2019/5/10 23:40:00"# 先转换为时间数组,然后转换为其他格式timeArray=time.strptime(a2,"%Y/%m/%d %H:%M:%S")otherStyleTime=time.strftime("%Y/%m/%d %H:%M:%S",timeArray)print(otherStyleTime)
```
### 输出结果
```

1557502800
2019/05/10 23:40:00

```
源链接: [https://www.runoob.com/python3/python-str-timestamp.html](https://www.runoob.com/python3/python-str-timestamp.html)