# Python 计算列表中所有奇数的和

## 题目描述
Python3 实例
我们将编写一个 Python 程序来计算列表中所有奇数的和。我们将使用一个简单的 for 循环来遍历列表，并使用条件语句来检查每个元素是否为奇数。如果是奇数，则将其加到总和中。

## 实例
### 代码
```python
defsum_of_odds(numbers):
     total=0
     fornuminnumbers:
         ifnum %2!=0:
             total +=num
     returntotal
 # 示例列表
 numbers=[1,2,3,4,5,6,7,8,9]
 result=sum_of_odds(numbers)
 print("列表中所有奇数的和是:",result)
```
### 输出结果
```
列表中所有奇数的和是: 25
```
源链接: [https://www.runoob.com/python3/python-sum-odds.html](https://www.runoob.com/python3/python-sum-odds.html)