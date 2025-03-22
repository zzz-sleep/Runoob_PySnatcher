# Python 将列表中的指定位置的两个元素对调

## 题目描述
Python3 实例
定义一个列表，并将列表中的指定位置的两个元素对调。
例如，对调第一个和第三个元素：
```

对调前 : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
对调后 : [19, 65, 23, 90]

```

## 实例 1
### 代码
```python
defswapPositions(list,pos1,pos2):
     list[pos1],list[pos2]=list[pos2],list[pos1]
     returnlist
 List=[23,65,19,90]
 pos1,pos2=1,3
 print(swapPositions(List,pos1-1,pos2-1))
```
### 输出结果
```

[19, 65, 23, 90]

```
## 实例 2
### 代码
```python
defswapPositions(list,pos1,pos2):
     first_ele=list.pop(pos1)
     second_ele=list.pop(pos2-1)
     list.insert(pos1,second_ele)
     list.insert(pos2,first_ele)
     returnlist
 List=[23,65,19,90]
 pos1,pos2=1,3
 print(swapPositions(List,pos1-1,pos2-1))
```
### 输出结果
```

[19, 65, 23, 90]

```
## 实例 3
### 代码
```python
defswapPositions(list,pos1,pos2):
     get=list[pos1],list[pos2]
     list[pos2],list[pos1]=get
     returnlist
 List=[23,65,19,90]
 pos1,pos2=1,3
 print(swapPositions(List,pos1-1,pos2-1))
```
### 输出结果
```

[19, 65, 23, 90]

```
源链接: [https://www.runoob.com/python3/python3-list-swap-two-elements.html](https://www.runoob.com/python3/python3-list-swap-two-elements.html)