# Python 计算数组元素之和

## 题目描述
Python3 实例
定义一个整型数组，并计算元素之和。
实现要求：
输入 : arr[] = {1, 2, 3}
输出 : 6
计算: 1 + 2 + 3 = 6

## 实例
### 代码
```python
# 定义函数，arr 为数组，n 为数组长度，可作为备用参数，这里没有用到
 def_sum(arr,n):
     # 使用内置的 sum 函数计算
     return(sum(arr))
 # 调用函数
 arr=[]
 # 数组元素
 arr=[12,3,4,15]
 # 计算数组元素的长度
 n=len(arr)
 ans=_sum(arr,n)
 # 输出结果
 print('数组元素之和为',ans)
```
### 输出结果
```

数组元素之和为 34

```
源链接: [https://www.runoob.com/python3/python3-sum-array.html](https://www.runoob.com/python3/python3-sum-array.html)