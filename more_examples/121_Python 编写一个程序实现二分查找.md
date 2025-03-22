# Python 编写一个程序实现二分查找

## 题目描述
Python3 实例
二分查找是一种高效的查找算法，适用于已排序的数组。它通过将数组分成两半来逐步缩小查找范围，直到找到目标元素或确定目标元素不存在。

## 实例
### 代码
```python
defbinary_search(arr,target):
     low=0
     high=len(arr)-1
     whilelow<=high:
         mid=(low + high)//2
         ifarr[mid]==target:
             returnmid
         elifarr[mid]<target:
             low=mid +1
         else:
             high=mid -1
     return-1
 # 示例数组
 arr=[1,3,5,7,9,11,13,15]
 target=7
 # 调用二分查找函数
 result=binary_search(arr,target)
 ifresult!=-1:
     print(f"元素 {target} 在数组中的索引是 {result}")
 else:
     print(f"元素 {target} 不在数组中")
```
### 输出结果
```
元素 7 在数组中的索引是 3
```
源链接: [https://www.runoob.com/python3/python-binary-search2.html](https://www.runoob.com/python3/python-binary-search2.html)