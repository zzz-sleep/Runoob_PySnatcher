# Python 求数组的中位数

## 题目描述
Python3 实例
中位数是统计学中的一个重要概念，它表示一组数据的中间值。对于一个有序数组，如果数组的长度是奇数，中位数就是中间的那个数；如果数组的长度是偶数，中位数则是中间两个数的平均值。下面是一个用 Python 求数组中位数的示例代码。

## 实例
### 代码
```python
deffind_median(nums):
     nums_sorted=sorted(nums)
     n=len(nums_sorted)
     mid=n //2
     ifn %2==1:
         returnnums_sorted[mid]
     else:
         return(nums_sorted[mid -1]+ nums_sorted[mid])/2
 # 示例数组
 nums=[3,5,1,4,2]
 median=find_median(nums)
 print(f"数组的中位数是: {median}")
```
### 输出结果
```
数组的中位数是: 3
```
源链接: [https://www.runoob.com/python3/python-median-array.html](https://www.runoob.com/python3/python-median-array.html)