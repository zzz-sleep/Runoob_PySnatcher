# Python 判断一个数是否为水仙花数

## 题目描述
Python3 实例
水仙花数（Narcissistic number）是指一个 n 位数，它的每个位上的数字的 n 次幂之和等于它本身。例如，153 是一个水仙花数，因为 1^3 + 5^3 + 3^3 = 153。
下面是一个 Python 程序，用于判断一个数是否为水仙花数：

## 实例
### 代码
```python
defis_narcissistic_number(num):
     # 将数字转换为字符串，方便逐位处理
     num_str=str(num)
     # 获取数字的位数
     n=len(num_str)
     # 计算每个位上的数字的 n 次幂之和
     sum_of_powers=sum(int(digit)** nfordigitinnum_str)
     # 判断是否等于原数
     returnsum_of_powers==num
 # 测试
 number=153
 ifis_narcissistic_number(number):
     print(f"{number} 是水仙花数")
 else:
     print(f"{number} 不是水仙花数")
```
### 输出结果
```
153 是水仙花数
```
源链接: [https://www.runoob.com/python3/python-narcissistic-number.html](https://www.runoob.com/python3/python-narcissistic-number.html)