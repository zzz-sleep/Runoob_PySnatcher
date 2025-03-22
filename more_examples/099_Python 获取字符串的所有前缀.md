# Python 获取字符串的所有前缀

## 题目描述
Python3 实例
在 Python 中，我们可以通过简单的循环来获取一个字符串的所有前缀。前缀是指从字符串开头到任意位置的子字符串。例如，字符串 "hello" 的所有前缀是 "h", "he", "hel", "hell", "hello"。

## 实例
### 代码
```python
defget_all_prefixes(s):
     prefixes=[]
     foriinrange(1,len(s)+1):
         prefixes.append(s[:i])
     returnprefixes
 # 示例
 s="hello"
 print(get_all_prefixes(s))
```
### 输出结果
```
未找到输出结果
```
## 实例
### 代码
```python
['h','he','hel','hell','hello']
```
### 输出结果
```
未找到输出结果
```
源链接: [https://www.runoob.com/python3/python-string-prefixes.html](https://www.runoob.com/python3/python-string-prefixes.html)