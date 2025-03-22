# Python  计数排序

## 题目描述
Python3 实例
计数排序的核心在于将输入的数据值转化为键存储在额外开辟的数组空间中。作为一种线性时间复杂度的排序，计数排序要求输入的数据必须是有确定范围的整数。

## 实例
### 代码
```python
defcountSort(arr):output=[0foriinrange(256)]count=[0foriinrange(256)]ans=[""for_inarr]foriinarr:count[ord(i)]+=1foriinrange(256):count[i]+=count[i-1]foriinrange(len(arr)):output[count[ord(arr[i])]-1]=arr[i]count[ord(arr[i])]-=1foriinrange(len(arr)):ans[i]=output[i]returnansarr="wwwrunoobcom"ans=countSort(arr)print("字符数组排序 %s"%("".join(ans)))
```
### 输出结果
```

符数组排序 bcmnoooruwww

```
源链接: [https://www.runoob.com/python3/python-counting-sort.html](https://www.runoob.com/python3/python-counting-sort.html)