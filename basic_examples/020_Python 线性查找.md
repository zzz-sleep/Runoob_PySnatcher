# Python 线性查找

## 题目描述
Python3 实例
线性查找指按一定的顺序检查数组中每一个元素，直到找到所要寻找的特定值为止。

## 示例图片
![Python 线性查找_Linear.png](Python 线性查找_Linear.png)

## 实例
### 代码
```python
defsearch(arr,n,x):foriinrange(0,n):if(arr[i]==x):returnireturn-1# 在数组 arr 中查找字符 Darr=['A','B','C','D','E']x='D'n=len(arr)result=search(arr,n,x)if(result== -1):print("元素不在数组中")else:print("元素在数组中的索引为",result)
```
### 输出结果
```

元素在数组中的索引为 3

```
源链接: [https://www.runoob.com/python3/python-linear-search.html](https://www.runoob.com/python3/python-linear-search.html)