# Python 求列表中所有偶数的和

## 题目描述
Python3 实例
我们将编写一个 Python 程序来求列表中所有偶数的和。我们将使用一个简单的 for 循环来遍历列表，并使用条件语句来检查每个元素是否为偶数。

## 实例
### 代码
```python
# 定义一个包含整数的列表
 numbers=[1,2,3,4,5,6,7,8,9,10]
 # 初始化一个变量来存储偶数的和
 even_sum=0
 # 遍历列表中的每个元素
 fornuminnumbers:
     # 检查当前元素是否为偶数
     ifnum %2==0:
         # 如果是偶数，则将其加到 even_sum 中
         even_sum +=num
 # 输出偶数的和
 print("列表中所有偶数的和为:",even_sum)
```
### 输出结果
```
列表中所有偶数的和为: 30
```
源链接: [https://www.runoob.com/python3/python-sum-even-numbers.html](https://www.runoob.com/python3/python-sum-even-numbers.html)