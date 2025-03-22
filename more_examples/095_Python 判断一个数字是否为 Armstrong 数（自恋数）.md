# Python 判断一个数字是否为 Armstrong 数（自恋数）

## 题目描述
Python3 实例
Armstrong 数（自恋数）是指一个 n 位数，其每个位上的数字的 n 次幂之和等于它本身。例如，153 是一个 Armstrong 数，因为 1^3 + 5^3 + 3^3 = 153。

## 实例
### 代码
```python
defis_armstrong_number(num):
     # 将数字转换为字符串以方便计算位数
     num_str=str(num)
     n=len(num_str)
     # 计算每个位上的数字的 n 次幂之和
     sum_of_powers=sum(int(digit)** nfordigitinnum_str)
     # 判断是否为 Armstrong 数
     returnsum_of_powers==num
 # 测试
 number=153
 ifis_armstrong_number(number):
     print(f"{number} 是一个 Armstrong 数")
 else:
     print(f"{number} 不是一个 Armstrong 数")
```
### 输出结果
```
153 是一个 Armstrong 数
```
源链接: [https://www.runoob.com/python3/python-armstrong-number.html](https://www.runoob.com/python3/python-armstrong-number.html)