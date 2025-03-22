# Python 获取字符串的最后一个单词

## 题目描述
Python3 实例
在 Python 中，我们可以使用字符串的split()方法将字符串分割成单词列表，然后通过索引获取最后一个单词。

## 实例
### 代码
```python
defget_last_word(text):
     words=text.split()
     returnwords[-1]ifwordselse""
 # 示例
 text="Hello, this is a test string"
 last_word=get_last_word(text)
 print(last_word)
```
### 输出结果
```
string
```
源链接: [https://www.runoob.com/python3/python-last-word.html](https://www.runoob.com/python3/python-last-word.html)