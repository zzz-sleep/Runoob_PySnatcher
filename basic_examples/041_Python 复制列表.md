# Python 复制列表

## 题目描述
Python3 实例
定义一个列表，并将该列表元素复制到另外一个列表上。

## 实例 1
### 代码
```python
defclone_runoob(li1):
     li_copy=li1[:]
     returnli_copy
 li1=[4,8,2,10,15,18]
 li2=clone_runoob(li1)
 print("原始列表:",li1)
 print("复制后列表:",li2)
```
### 输出结果
```

原始列表: [4, 8, 2, 10, 15, 18]
复制后列表: [4, 8, 2, 10, 15, 18]

```
## 实例 2: 使用 extend() 方法
### 代码
```python
defclone_runoob(li1):
     li_copy=[]
     li_copy.extend(li1)
     returnli_copy
 li1=[4,8,2,10,15,18]
 li2=clone_runoob(li1)
 print("原始列表:",li1)
 print("复制后列表:",li2)
```
### 输出结果
```

原始列表: [4, 8, 2, 10, 15, 18]
复制后列表: [4, 8, 2, 10, 15, 18]

```
## 实例 3: 使用 list() 方法
### 代码
```python
defclone_runoob(li1):
     li_copy=list(li1)
     returnli_copy
 li1=[4,8,2,10,15,18]
 li2=clone_runoob(li1)
 print("原始列表:",li1)
 print("复制后列表:",li2)
```
### 输出结果
```

原始列表: [4, 8, 2, 10, 15, 18]
复制后列表: [4, 8, 2, 10, 15, 18]

```
源链接: [https://www.runoob.com/python3/python-copy-list.html](https://www.runoob.com/python3/python-copy-list.html)