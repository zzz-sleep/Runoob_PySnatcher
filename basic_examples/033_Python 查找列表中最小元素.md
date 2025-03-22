# Python 查找列表中最小元素

## 题目描述
Python3 实例
定义一个数字列表，并查找列表中的最小元素。
例如：
```

输入 : list1 = [10, 20, 4]
输出 : 4 

```

## 实例 1
### 代码
```python
list1=[10,20,4,45,99]
 list1.sort()
 print("最小元素为:",*list1[:1])
```
### 输出结果
```

最小元素为: 4

```
## 实例 2：使用 min() 方法
### 代码
```python
list1=[10,20,1,45,99]
 print("最小元素为:",min(list1))
```
### 输出结果
```

最小元素为: 1

```
源链接: [https://www.runoob.com/python3/python-min-list-element.html](https://www.runoob.com/python3/python-min-list-element.html)