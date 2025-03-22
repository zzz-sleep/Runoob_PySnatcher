# Python 插入排序

## 题目描述
Python3 实例
插入排序（英语：Insertion Sort）是一种简单直观的排序算法。它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。

## 实例
### 代码
```python
definsertionSort(arr):foriinrange(1,len(arr)):key=arr[i]j=i-1whilej>=0andkey<arr[j]:arr[j+1]=arr[j]j-=1arr[j+1]=keyarr=[12,11,13,5,6]insertionSort(arr)print("排序后的数组:")foriinrange(len(arr)):print("%d"%arr[i])
```
### 输出结果
```

排序后的数组:
5
6
11
12
13

```
源链接: [https://www.runoob.com/python3/python-insertion-sort.html](https://www.runoob.com/python3/python-insertion-sort.html)