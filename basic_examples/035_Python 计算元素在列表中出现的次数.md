# Python 计算元素在列表中出现的次数

## 题目描述
Python3 实例
定义一个列表，并计算某个元素在列表中出现的次数。
例如：
```
输入 : lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
       x = 10
输出 : 3 
```

## 实例 1
### 代码
```python
defcountX(lst,x):
     count=0
     foreleinlst:
         if(ele==x):
             count=count +1
     returncount
 lst=[8,6,8,10,8,20,10,8,8]
 x=8
 print(countX(lst,x))
```
### 输出结果
```

5

```
## 实例 2: 使用 count() 方法
### 代码
```python
defcountX(lst,x):
     returnlst.count(x)
 lst=[8,6,8,10,8,20,10,8,8]
 x=8
 print(countX(lst,x))
```
### 输出结果
```
5

```
源链接: [https://www.runoob.com/python3/python-count-occurrences-element-list.html](https://www.runoob.com/python3/python-count-occurrences-element-list.html)