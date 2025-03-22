# Python 将列表中的头尾两个元素对调

## 题目描述
Python3 实例
定义一个列表，并将列表中的头尾两个元素对调。
例如：
```
对调前 : [1, 2, 3]
对调后 : [3, 2, 1]
```

## 实例 1
### 代码
```python
defswapList(newList):
     size=len(newList)
     temp=newList[0]
     newList[0]=newList[size -1]
     newList[size -1]=temp
     returnnewList
 newList=[1,2,3]
 print(swapList(newList))
```
### 输出结果
```

[3, 2, 1]

```
## 实例 2
### 代码
```python
defswapList(newList):
     newList[0],newList[-1]=newList[-1],newList[0]
     returnnewList
 newList=[1,2,3]
 print(swapList(newList))
```
### 输出结果
```

[3, 2, 1]

```
## 实例 3
### 代码
```python
defswapList(list):
     get=list[-1],list[0]
     list[0],list[-1]=get
     returnlist
 newList=[1,2,3]
 print(swapList(newList))
```
### 输出结果
```

[3, 2, 1]

```
源链接: [https://www.runoob.com/python3/python-list-interchange.html](https://www.runoob.com/python3/python-list-interchange.html)