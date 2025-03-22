# Python 判断一个年份是否是闰年

## 题目描述
Python3 实例
判断一个年份是否是闰年，需要遵循以下规则：

## 实例
### 代码
```python
defis_leap_year(year):
     if(year %4==0andyear %100!=0)or(year %400==0):
         returnTrue
     else:
         returnFalse
 # 测试
 year=2024
 ifis_leap_year(year):
     print(f"{year} 是闰年")
 else:
     print(f"{year} 不是闰年")
```
### 输出结果
```
2024 是闰年
```
源链接: [https://www.runoob.com/python3/python-leap-year.html](https://www.runoob.com/python3/python-leap-year.html)