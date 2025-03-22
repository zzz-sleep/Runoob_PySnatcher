# Python 堆排序

## 题目描述
Python3 实例
堆排序（Heapsort）是指利用堆这种数据结构所设计的一种排序算法。堆积是一个近似完全二叉树的结构，并同时满足堆积的性质：即子结点的键值或索引总是小于（或者大于）它的父节点。堆排序可以说是一种利用堆的概念来排序的选择排序。

## 实例
### 代码
```python
defheapify(arr,n,i):largest=il=2*i+1# left = 2*i + 1r=2*i+2# right = 2*i + 2ifl<nandarr[i]<arr[l]:largest=lifr<nandarr[largest]<arr[r]:largest=riflargest!=i:arr[i],arr[largest]=arr[largest],arr[i]# 交换heapify(arr,n,largest)defheapSort(arr):n=len(arr)# Build a maxheap.foriinrange(n, -1, -1):heapify(arr,n,i)# 一个个交换元素foriinrange(n-1,0, -1):arr[i],arr[0]=arr[0],arr[i]# 交换heapify(arr,i,0)arr=[12,11,13,5,6,7]heapSort(arr)n=len(arr)print("排序后")foriinrange(n):print("%d"%arr[i]),
```
### 输出结果
```

排序后
5
6
7
11
12
13

```
源链接: [https://www.runoob.com/python3/python-heap-sort.html](https://www.runoob.com/python3/python-heap-sort.html)