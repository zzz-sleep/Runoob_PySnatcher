# Python 找到字符串中出现最多的字母

## 题目描述
Python3 实例
在 Python 中，我们可以使用collections.Counter来统计字符串中每个字母出现的次数，然后找到出现次数最多的字母。

## 实例
### 代码
```python
fromcollectionsimportCounter
 defmost_frequent_letter(s):
     # 使用 Counter 统计每个字母的出现次数
     counter=Counter(s)
     # 找到出现次数最多的字母
     most_common=counter.most_common(1)
     returnmost_common[0][0]ifmost_commonelseNone
 # 测试
 s="hello world"
 result=most_frequent_letter(s)
 print(f"The most frequent letter in '{s}' is: {result}")
```
### 输出结果
```
The most frequent letter in 'hello world' is: l
```
源链接: [https://www.runoob.com/python3/python-most-frequent-letter.html](https://www.runoob.com/python3/python-most-frequent-letter.html)