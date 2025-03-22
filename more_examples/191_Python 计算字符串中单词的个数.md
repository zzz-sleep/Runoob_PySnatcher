# Python 计算字符串中单词的个数

## 题目描述
Python3 实例
在 Python 中，我们可以通过将字符串分割成单词列表，然后计算列表的长度来得到字符串中单词的个数。下面是一个简单的示例代码。

## 实例
### 代码
```python
defcount_words(text):
     words=text.split()
     returnlen(words)
 # 示例字符串
 text="Hello world, this is a test."
 word_count=count_words(text)
 print(f"The number of words in the text is: {word_count}")
```
### 输出结果
```
The number of words in the text is: 6
```
源链接: [https://www.runoob.com/python3/python-word-count.html](https://www.runoob.com/python3/python-word-count.html)