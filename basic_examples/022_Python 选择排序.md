# Python 选择排序

## 题目描述
Python3 实例
选择排序（Selection sort）是一种简单直观的排序算法。它的工作原理如下。首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。

## 实例
### 代码
```python
importsysA=[64,25,12,22,11]foriinrange(len(A)):min_idx=iforjinrange(i+1,len(A)):ifA[min_idx]>A[j]:min_idx=jA[i],A[min_idx]=A[min_idx],A[i]print("排序后的数组：")foriinrange(len(A)):print("%d"%A[i]),
```
### 输出结果
```

排序后的数组：
11
12
22
25
64

```
源链接: [https://www.runoob.com/python3/python-selection-sort.html](https://www.runoob.com/python3/python-selection-sort.html)