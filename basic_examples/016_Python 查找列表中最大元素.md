# Python 查找列表中最大元素

## 题目描述
Python3 实例
定义一个数字列表，并查找列表中的最大元素。
例如：
```

输入 : list1 = [10, 20, 4]
输出 : 20 

```

## 实例 1
### 代码
```python
list1=[10,20,4,45,99]
 list1.sort()
 print("最大元素为:",list1[-1])
```
### 输出结果
```

最大元素为: 99

```
## 实例 2：使用 max() 方法
### 代码
```python
list1=[10,20,1,45,99]
 print("最大元素为:",max(list1))
```
### 输出结果
```

最大元素为: 99

```
源链接: [https://www.runoob.com/python3/python-max-list-element.html](https://www.runoob.com/python3/python-max-list-element.html)