# 使用 Python 实现冒泡排序算法

## 题目描述
Python3 实例
冒泡排序是一种简单的排序算法，它重复地遍历要排序的列表，比较相邻的元素并交换它们的位置，直到整个列表排序完成。这个算法的名字由来是因为越小的元素会经由交换慢慢"浮"到数列的顶端。
代码部分：

## 实例
### 代码
```python
defbubble_sort(arr):
     n=len(arr)
     foriinrange(n):
         forjinrange(0,n-i-1):
             ifarr[j]>arr[j+1]:
                 arr[j],arr[j+1]=arr[j+1],arr[j]
 # 示例数组
 arr=[64,34,25,12,22,11,90]
 bubble_sort(arr)
 print("排序后的数组:",arr)
```
### 输出结果
```
排序后的数组: [11, 12, 22, 25, 34, 64, 90]
```
源链接: [https://www.runoob.com/python3/python-bubble-sort2.html](https://www.runoob.com/python3/python-bubble-sort2.html)