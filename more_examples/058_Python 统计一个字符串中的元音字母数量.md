# Python 统计一个字符串中的元音字母数量

## 题目描述
Python3 实例
在 Python 中，我们可以通过遍历字符串中的每个字符，并检查它是否是元音字母（a, e, i, o, u）来统计字符串中元音字母的数量。以下是一个简单的示例代码。

## 实例
### 代码
```python
defcount_vowels(s):
     vowels="aeiouAEIOU"
     count=0
     forcharins:
         ifcharinvowels:
             count +=1
     returncount
 # 示例字符串
 text="Hello, World!"
 print(f"元音字母的数量是: {count_vowels(text)}")
```
### 输出结果
```
元音字母的数量是: 3
```
源链接: [https://www.runoob.com/python3/python-vowel-count.html](https://www.runoob.com/python3/python-vowel-count.html)