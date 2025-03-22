# Python 希尔排序

## 题目描述
Python3 实例
希尔排序，也称递减增量排序算法，是插入排序的一种更高效的改进版本。但希尔排序是非稳定排序算法。
希尔排序的基本思想是：先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，待整个序列中的记录"基本有序"时，再对全体记录进行依次直接插入排序。

## 实例
### 代码
```python
defshellSort(arr):n=len(arr)gap=int(n/2)whilegap>0:foriinrange(gap,n):temp=arr[i]j=iwhilej>=gapandarr[j-gap]>temp:arr[j]=arr[j-gap]j-=gaparr[j]=tempgap=int(gap/2)arr=[12,34,54,2,3]n=len(arr)print("排序前:")foriinrange(n):print(arr[i]),shellSort(arr)print("\n排序后:")foriinrange(n):print(arr[i]),
```
### 输出结果
```

排序前:
12
34
54
2
3

排序后:
2
3
12
34
54

```
源链接: [https://www.runoob.com/python3/python-shellsort.html](https://www.runoob.com/python3/python-shellsort.html)