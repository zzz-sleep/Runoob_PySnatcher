# 使用 Python 创建一个时间类，支持时间加减操作

## 题目描述
Python3 实例
我们将创建一个名为Time的类，该类可以表示时间（小时、分钟、秒），并支持时间的加减操作。我们将实现__add__和__sub__方法来支持时间的加减操作。

## 实例
### 代码
```python
classTime:
     def__init__(self,hours,minutes,seconds):
         self.hours=hours
         self.minutes=minutes
         self.seconds=seconds
         self.normalize()
     defnormalize(self):
         extra_minutes,self.seconds=divmod(self.seconds,60)
         self.minutes+=extra_minutes
         extra_hours,self.minutes=divmod(self.minutes,60)
         self.hours+=extra_hours
     def__add__(self,other):
         total_seconds=self.hours*3600+self.minutes*60+self.seconds
         total_seconds +=other.hours*3600+ other.minutes*60+ other.seconds
         hours,remainder=divmod(total_seconds,3600)
         minutes,seconds=divmod(remainder,60)
         returnTime(hours,minutes,seconds)
     def__sub__(self,other):
         total_seconds=self.hours*3600+self.minutes*60+self.seconds
         total_seconds -=other.hours*3600+ other.minutes*60+ other.seconds
         hours,remainder=divmod(total_seconds,3600)
         minutes,seconds=divmod(remainder,60)
         returnTime(hours,minutes,seconds)
     def__str__(self):
         returnf"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"
 # 示例使用
 time1=Time(2,30,45)
 time2=Time(1,15,20)
 print("Time 1:",time1)
 print("Time 2:",time2)
 time_sum=time1 + time2
 print("Time 1 + Time 2:",time_sum)
 time_diff=time1 - time2
 print("Time 1 - Time 2:",time_diff)
```
### 输出结果
```
Time 1: 02:30:45
Time 2: 01:15:20
Time 1 + Time 2: 03:46:05
Time 1 - Time 2: 01:15:25
```
源链接: [https://www.runoob.com/python3/python-time-class.html](https://www.runoob.com/python3/python-time-class.html)