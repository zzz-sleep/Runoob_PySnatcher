# Python 判断数字是否为"快乐数"

## 题目描述
Python3 实例
快乐数是指一个数字，将其每个位上的数字平方后相加，得到一个新的数字，重复这个过程直到最后结果为1，或者进入一个不包含1的循环。如果最终结果为1，则这个数字就是快乐数。

## 实例
### 代码
```python
defis_happy_number(n):
     defget_next(number):
         returnsum(int(char)**2forcharinstr(number))
     seen=set()
     whilen!=1andnnotinseen:
         seen.add(n)
         n=get_next(n)
     returnn==1
 # 测试
 print(is_happy_number(19))# 输出 True
 print(is_happy_number(20))# 输出 False
```
### 输出结果
```
True
False
```
源链接: [https://www.runoob.com/python3/python-happy-number.html](https://www.runoob.com/python3/python-happy-number.html)