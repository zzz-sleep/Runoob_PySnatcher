# Python 判断一个数是否是完全数

## 题目描述
Python3 实例
完全数是指一个数等于它的所有真因子（除了自身以外的因子）之和。例如，6 是一个完全数，因为它的真因子是 1, 2, 3，而 1 + 2 + 3 = 6。
下面是一个 Python 程序，用于判断一个数是否是完全数：

## 实例
### 代码
```python
defis_perfect_number(n):
     ifn<2:
         returnFalse
     sum_of_factors=1
     foriinrange(2,int(n **0.5)+1):
         ifn % i==0:
             sum_of_factors +=i
             ifi!=n // i:
                 sum_of_factors +=n // i
     returnsum_of_factors==n
 # 测试
 number=28
 ifis_perfect_number(number):
     print(f"{number} 是一个完全数")
 else:
     print(f"{number} 不是一个完全数")
```
### 输出结果
```
28 是一个完全数
```
源链接: [https://www.runoob.com/python3/python-perfect-number.html](https://www.runoob.com/python3/python-perfect-number.html)