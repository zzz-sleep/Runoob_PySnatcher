# Python 二分查找

## 题目描述
Python3 实例
二分搜索是一种在有序数组中查找某一特定元素的搜索算法。搜索过程从数组的中间元素开始，如果中间元素正好是要查找的元素，则搜索过程结束；如果某一特定元素大于或者小于中间元素，则在数组大于或小于中间元素的那一半中查找，而且跟开始一样从中间元素开始比较。如果在某一步骤数组为空，则代表找不到。这种搜索算法每一次比较都使搜索范围缩小一半。

## 示例图片
![Python 二分查找_Binary_search_into_array.png](Python 二分查找_Binary_search_into_array.png)

## 实例 : 递归
### 代码
```python
# 返回 x 在 arr 中的索引，如果不存在返回 -1defbinarySearch(arr,l,r,x):# 基本判断ifr>=l:mid=int(l+(r-l)/2)# 元素整好的中间位置ifarr[mid]==x:returnmid# 元素小于中间位置的元素，只需要再比较左边的元素elifarr[mid]>x:returnbinarySearch(arr,l,mid-1,x)# 元素大于中间位置的元素，只需要再比较右边的元素else:returnbinarySearch(arr,mid+1,r,x)else:# 不存在return-1# 测试数组arr=[2,3,4,10,40]x=10# 函数调用result=binarySearch(arr,0,len(arr)-1,x)ifresult!= -1:print("元素在数组中的索引为 %d"%result)else:print("元素不在数组中")
```
### 输出结果
```

元素在数组中的索引为 3

```
源链接: [https://www.runoob.com/python3/python-binary-search.html](https://www.runoob.com/python3/python-binary-search.html)