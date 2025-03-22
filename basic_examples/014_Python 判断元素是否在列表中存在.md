# Python 判断元素是否在列表中存在

## 题目描述
Python3 实例
定义一个列表，并判断元素是否在列表中。

## 实例 1
### 代码
```python
test_list=[1,6,3,5,3,4]
 print("查看 4 是否在列表中 ( 使用循环 ) : ")
 foriintest_list:
     if(i==4):
         print("存在")
 print("查看 4 是否在列表中 ( 使用 in 关键字 ) : ")
 if(4intest_list):
     print("存在")
```
### 输出结果
```

查看 4 是否在列表中 ( 使用循环 ) : 
存在
查看 4 是否在列表中 ( 使用 in 关键字 ) : 
存在

```
## 实例 2
### 代码
```python
# 初始化列表
 test_list_set=[1,6,3,5,3,4]
 test_list_bisect=[1,6,3,5,3,4]
 print("查看 4 是否在列表中 ( 使用 set() + in) : ")
 test_list_set=set(test_list_set)
 if4intest_list_set :
     print("存在")
 print("查看 4 是否在列表中 ( 使用 count()) : ")
 iftest_list_bisect.count(4)>0:
     print("存在")
```
### 输出结果
```

查看 4 是否在列表中 ( 使用 set() + in) : 
存在
查看 4 是否在列表中 ( 使用 count()) : 
存在

```
源链接: [https://www.runoob.com/python3/python-check-element-exists-in-list.html](https://www.runoob.com/python3/python-check-element-exists-in-list.html)