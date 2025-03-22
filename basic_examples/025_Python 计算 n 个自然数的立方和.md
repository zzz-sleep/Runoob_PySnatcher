# Python 计算 n 个自然数的立方和

## 题目描述
Python3 实例
计算公式   13+ 23+ 33+ 43+ …….+ n3
实现要求：
输入 : n = 5
输出 : 225
公式 : 13+ 23+ 33+ 43+ 53= 225
输入 : n = 7
输入 : 784
公式 : 13+ 23+ 33+ 43+ 53+ 63+ 73= 784

## 实例
### 代码
```python
# 定义立方和的函数
 defsumOfSeries(n):
     sum=0
     foriinrange(1,n+1):
         sum+=i*i*i
     returnsum
 # 调用函数
 n=5
 print(sumOfSeries(n))
```
### 输出结果
```
225
```
源链接: [https://www.runoob.com/python3/python-cube-sum.html](https://www.runoob.com/python3/python-cube-sum.html)