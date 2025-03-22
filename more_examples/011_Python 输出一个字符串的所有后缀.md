# Python 输出一个字符串的所有后缀

## 题目描述
Python3 实例
在 Python 中，我们可以通过切片操作来获取一个字符串的所有后缀。字符串的后缀是指从字符串的某个位置开始到字符串末尾的子串。我们可以通过遍历字符串的每个字符位置来获取所有可能的后缀。

## 实例
### 代码
```python
defget_all_suffixes(s):
     suffixes=[]
     foriinrange(len(s)):
         suffixes.append(s[i:])
     returnsuffixes
 # 示例字符串
 s="hello"
 print(get_all_suffixes(s))
```
### 输出结果
```
未找到输出结果
```
## 实例
### 代码
```python
['hello','ello','llo','lo','o']
```
### 输出结果
```
未找到输出结果
```
源链接: [https://www.runoob.com/python3/python-string-suffixes.html](https://www.runoob.com/python3/python-string-suffixes.html)