# Python 冒泡排序

## 题目描述
Python3 实例
冒泡排序（Bubble Sort）也是一种简单直观的排序算法。它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。这个算法的名字由来是因为越小的元素会经由交换慢慢"浮"到数列的顶端。

## 实例
### 代码
```python
defbubbleSort(arr):n=len(arr)# 遍历所有数组元素foriinrange(n):# Last i elements are already in placeforjinrange(0,n-i-1):ifarr[j]>arr[j+1]:arr[j],arr[j+1]=arr[j+1],arr[j]arr=[64,34,25,12,22,11,90]bubbleSort(arr)print("排序后的数组:")foriinrange(len(arr)):print("%d"%arr[i]),
```
### 输出结果
```

排序后的数组:
11
12
22
25
34
64
90

```
源链接: [https://www.runoob.com/python3/python-bubble-sort.html](https://www.runoob.com/python3/python-bubble-sort.html)