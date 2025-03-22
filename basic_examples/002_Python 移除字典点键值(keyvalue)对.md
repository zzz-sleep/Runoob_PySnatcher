# Python 移除字典点键值(key/value)对

## 题目描述
Python3 实例
给定一个字典， 移除字典点键值(key/value)对。

## 实例 1 : 使用 del 移除
### 代码
```python
test_dict= {"Runoob":1,"Google":2,"Taobao":3,"Zhihu":4}# 输出原始的字典print("字典移除前 :"+str(test_dict))# 使用 del 移除 Zhihudeltest_dict['Zhihu']# 输出移除后的字典print("字典移除后 :"+str(test_dict))# 移除没有的 key 会报错#del test_dict['Baidu']
```
### 输出结果
```

字典移除前 : {'Runoob': 1, 'Google': 2, 'Taobao': 3, 'Zhihu': 4}
字典移除后 : {'Runoob': 1, 'Google': 2, 'Taobao': 3}

```
## 实例 2 : 使用 pop() 移除
### 代码
```python
test_dict= {"Runoob":1,"Google":2,"Taobao":3,"Zhihu":4}# 输出原始的字典print("字典移除前 :"+str(test_dict))# 使用 pop 移除 Zhihuremoved_value=test_dict.pop('Zhihu')# 输出移除后的字典print("字典移除后 :"+str(test_dict))print("移除的 key 对应的 value 为 :"+str(removed_value))print('\r')# 使用 pop() 移除没有的 key 不会发生异常，我们可以自定义提示信息removed_value=test_dict.pop('Baidu','没有该键(key)')# 输出移除后的字典print("字典移除后 :"+str(test_dict))print("移除的值为 :"+str(removed_value))
```
### 输出结果
```

字典移除前 : {'Runoob': 1, 'Google': 2, 'Taobao': 3, 'Zhihu': 4}
字典移除后 : {'Runoob': 1, 'Google': 2, 'Taobao': 3}
移除的 key 对应的 value 为 : 4

字典移除后 : {'Runoob': 1, 'Google': 2, 'Taobao': 3}
移除的值为 : 没有该键(key)

```
## 实例 3 : 使用 items() 移除
### 代码
```python
test_dict= {"Runoob":1,"Google":2,"Taobao":3,"Zhihu":4}# 输出原始的字典print("字典移除前 :"+str(test_dict))# 使用 pop 移除 Zhihunew_dict= {key:valforkey,valintest_dict.items()ifkey!='Zhihu'}# 输出移除后的字典print("字典移除后 :"+str(new_dict))
```
### 输出结果
```

字典移除前 : {'Runoob': 1, 'Google': 2, 'Taobao': 3, 'Zhihu': 4}
字典移除后 : {'Runoob': 1, 'Google': 2, 'Taobao': 3}

```
源链接: [https://www.runoob.com/python3/python-remove-a-key-from-dictionary.html](https://www.runoob.com/python3/python-remove-a-key-from-dictionary.html)