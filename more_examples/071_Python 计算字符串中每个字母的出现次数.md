# Python 计算字符串中每个字母的出现次数

## 题目描述
Python3 实例
在 Python 中，我们可以使用字典来统计字符串中每个字母的出现次数。通过遍历字符串中的每个字符，并将其作为字典的键，对应的值则是该字符出现的次数。

## 实例
### 代码
```python
defcount_letters(s):
     letter_count={}
     forcharins:
         ifcharinletter_count:
             letter_count[char]+=1
         else:
             letter_count[char]=1
     returnletter_count
 # 示例字符串
 text="hello world"
 result=count_letters(text)
 print(result)
```
### 输出结果
```
未找到输出结果
```
## 实例
### 代码
```python
{'h':1,'e':1,'l':3,'o':2,' ':1,'w':1,'r':1,'d':1}
```
### 输出结果
```
未找到输出结果
```
源链接: [https://www.runoob.com/python3/python-letter-count.html](https://www.runoob.com/python3/python-letter-count.html)