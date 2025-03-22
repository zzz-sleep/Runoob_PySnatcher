# Python 归并排序

## 题目描述
Python3 实例
归并排序（英语：Merge sort，或mergesort），是创建在归并操作上的一种有效的排序算法。该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。
分治法:

## 实例
### 代码
```python
defmerge(arr,l,m,r):n1=m-l+1n2=r-m# 创建临时数组L=[0]*(n1)R=[0]*(n2)# 拷贝数据到临时数组 arrays L[] 和 R[]foriinrange(0,n1):L[i]=arr[l+i]forjinrange(0,n2):R[j]=arr[m+1+j]# 归并临时数组到 arr[l..r]i=0# 初始化第一个子数组的索引j=0# 初始化第二个子数组的索引k=l# 初始归并子数组的索引whilei<n1andj<n2:ifL[i]<=R[j]:arr[k]=L[i]i+=1else:arr[k]=R[j]j+=1k+=1# 拷贝 L[] 的保留元素whilei<n1:arr[k]=L[i]i+=1k+=1# 拷贝 R[] 的保留元素whilej<n2:arr[k]=R[j]j+=1k+=1defmergeSort(arr,l,r):ifl<r:m=int((l+(r-1))/2)mergeSort(arr,l,m)mergeSort(arr,m+1,r)merge(arr,l,m,r)arr=[12,11,13,5,6,7]n=len(arr)print("给定的数组")foriinrange(n):print("%d"%arr[i]),mergeSort(arr,0,n-1)print("\n\n排序后的数组")foriinrange(n):print("%d"%arr[i]),
```
### 输出结果
```

给定的数组
12
11
13
5
6
7


排序后的数组
5
6
7
11
12
13

```
源链接: [https://www.runoob.com/python3/python-merge-sort.html](https://www.runoob.com/python3/python-merge-sort.html)