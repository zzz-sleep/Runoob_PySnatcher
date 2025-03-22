# Python 按键(key)或值(value)对字典进行排序

## 题目描述
Python3 实例
给定一个字典，然后按键(key)或值(value)对字典进行排序。

## 实例1：按键(key)排序
### 代码
```python
defdictionairy():# 声明字典key_value={}# 初始化key_value[2]=56key_value[1]=2key_value[5]=12key_value[4]=24key_value[6]=18key_value[3]=323print("按键(key)排序:")# sorted(key_value) 返回重新排序的列表# 字典按键排序foriinsorted(key_value):print((i,key_value[i]),end="")defmain():# 调用函数dictionairy()# 主函数if__name__=="__main__":main()
```
### 输出结果
```

按键(key)排序:
(1, 2) (2, 56) (3, 323) (4, 24) (5, 12) (6, 18) 

```
## 实例2：按值(value)排序
### 代码
```python
defdictionairy():# 声明字典key_value={}# 初始化key_value[2]=56key_value[1]=2key_value[5]=12key_value[4]=24key_value[6]=18key_value[3]=323print("按值(value)排序:")print(sorted(key_value.items(),key=lambdakv:(kv[1],kv[0])))defmain():dictionairy()if__name__=="__main__":main()
```
### 输出结果
```

按值(value)排序:
[(1, 2), (5, 12), (6, 18), (4, 24), (2, 56), (3, 323)]

```
## 实例 3 : 字典列表排序
### 代码
```python
lis=[{"name":"Taobao","age":100},  
{"name":"Runoob","age":7}, 
{"name":"Google","age":100}, 
{"name":"Wiki","age":200}]# 通过 age 升序排序print("列表通过 age 升序排序:")print(sorted(lis,key=lambdai:i['age']))print("\r")# 先按 age 排序，再按 name 排序print("列表通过 age 和 name 排序:")print(sorted(lis,key=lambdai:(i['age'],i['name'])))print("\r")# 按 age 降序排序print("列表通过 age 降序排序:")print(sorted(lis,key=lambdai:i['age'],reverse=True))
```
### 输出结果
```

列表通过 age 升序排序: 
[{'name': 'Runoob', 'age': 7}, {'name': 'Taobao', 'age': 100}, {'name': 'Google', 'age': 100}, {'name': 'Wiki', 'age': 200}]

列表通过 age 和 name 排序: 
[{'name': 'Runoob', 'age': 7}, {'name': 'Google', 'age': 100}, {'name': 'Taobao', 'age': 100}, {'name': 'Wiki', 'age': 200}]

列表通过 age 降序排序: 
[{'name': 'Wiki', 'age': 200}, {'name': 'Taobao', 'age': 100}, {'name': 'Google', 'age': 100}, {'name': 'Runoob', 'age': 7}]

```
源链接: [https://www.runoob.com/python3/python-sort-dictionaries-by-key-or-value.html](https://www.runoob.com/python3/python-sort-dictionaries-by-key-or-value.html)