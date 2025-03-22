# Python 快速排序

## 题目描述
Python3 实例
快速排序使用分治法（Divide and conquer）策略来把一个序列（list）分为较小和较大的2个子序列，然后递归地排序两个子序列。
步骤为：
递归到最底部的判断条件是数列的大小是零或一，此时该数列显然已经有序。
选取基准值有数种具体方法，此选取方法对排序的时间性能有决定性影响。

## 实例
### 代码
```python
defpartition(arr,low,high):i=(low-1)# 最小元素索引pivot=arr[high]forjinrange(low,high):# 当前元素小于或等于 pivotifarr[j]<=pivot:i=i+1arr[i],arr[j]=arr[j],arr[i]arr[i+1],arr[high]=arr[high],arr[i+1]return(i+1)# arr[] --> 排序数组# low  --> 起始索引# high  --> 结束索引# 快速排序函数defquickSort(arr,low,high):iflow<high:pi=partition(arr,low,high)quickSort(arr,low,pi-1)quickSort(arr,pi+1,high)arr=[10,7,8,9,1,5]n=len(arr)quickSort(arr,0,n-1)print("排序后的数组:")foriinrange(n):print("%d"%arr[i]),
```
### 输出结果
```

排序后的数组:
1
5
7
8
9
10

```
源链接: [https://www.runoob.com/python3/python-quicksort.html](https://www.runoob.com/python3/python-quicksort.html)