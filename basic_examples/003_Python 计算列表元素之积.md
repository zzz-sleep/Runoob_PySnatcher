# Python 计算列表元素之积

## 题目描述
Python3 实例
定义一个数字列表，并计算列表元素之积。
例如：
```

输入 : list1 = [1, 2, 3] 
输出 : 6 
计算：1 * 2 * 3

```

## 实例 1
### 代码
```python
defmultiplyList(myList):
     result=1
     forxinmyList:
          result=result * x
     returnresult
 list1=[1,2,3]
 list2=[3,2,4]
 print(multiplyList(list1))
 print(multiplyList(list2))
```
### 输出结果
```
6
24
```
源链接: [https://www.runoob.com/python3/python-multiply-list.html](https://www.runoob.com/python3/python-multiply-list.html)