# Python 计算列表元素之和

## 题目描述
Python3 实例
定义一个数字列表，并计算列表元素之和。

## 实例 1
### 代码
```python
total=0
 list1=[11,5,17,18,23]
 foreleinrange(0,len(list1)):
     total=total + list1[ele]
 print("列表元素之和为: ",total)
```
### 输出结果
```

列表元素之和为:  74

```
## 实例 2: 使用  while() 循环
### 代码
```python
total=0
 ele=0
 list1=[11,5,17,18,23]
 while(ele<len(list1)):
     total=total + list1[ele]
     ele +=1
 print("列表元素之和为: ",total)
```
### 输出结果
```

列表元素之和为:  74

```
## 实例 3: 使用递归
### 代码
```python
list1=[11,5,17,18,23]
 defsumOfList(list,size):
    if(size==0):
      return0
    else:
      returnlist[size -1]+ sumOfList(list,size -1)
 total=sumOfList(list1,len(list1))
 print("列表元素之和为: ",total)
```
### 输出结果
```

列表元素之和为:  74

```
源链接: [https://www.runoob.com/python3/python-sum-list.html](https://www.runoob.com/python3/python-sum-list.html)