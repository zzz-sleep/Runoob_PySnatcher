# Python 删除字符串首尾的空格

## 题目描述
Python3 实例
Python 要删除字符串首尾的空格可以使用strip()方法。
以下是如何使用它的实例：

## 实例
### 代码
```python
original_string="   这是一个带有空格的字符串   "
 stripped_string=original_string.strip()
 print(stripped_string)
```
### 输出结果
```
这是一个带有空格的字符串
```
## 实例
### 代码
```python
my_string="\nPython "
 print(my_string.strip(" "))
```
### 输出结果
```


Python
```
## 实例
### 代码
```python
importre
 my_string=" Hello Python "
 output=re.sub(r'^\s+|\s+$','',my_string)
 print(output)
```
### 输出结果
```
Hello python
```
## 实例
### 代码
```python
original_string="   这是一个带有空格的字符串   "
 left_stripped_string=original_string.lstrip()# 删除开头的空格
 right_stripped_string=original_string.rstrip()# 删除结尾的空格
 print(left_stripped_string)
 print(right_stripped_string)
```
### 输出结果
```
这是一个带有空格的字符串   
   这是一个带有空格的字符串
```
源链接: [https://www.runoob.com/python3/python-trim-whitespace-from-a-string.html](https://www.runoob.com/python3/python-trim-whitespace-from-a-string.html)