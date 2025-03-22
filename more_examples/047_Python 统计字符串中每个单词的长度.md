# Python 统计字符串中每个单词的长度

## 题目描述
Python3 实例
我们将编写一个 Python 程序来统计字符串中每个单词的长度。这个程序将首先将字符串分割成单词列表，然后遍历每个单词并计算其长度。

## 实例
### 代码
```python
defword_lengths(s):
     words=s.split()
     lengths=[len(word)forwordinwords]
     returndict(zip(words,lengths))
 # 示例字符串
 text="Hello world this is a test"
 result=word_lengths(text)
 print(result)
```
### 输出结果
```
未找到输出结果
```
## 实例
### 代码
```python
{'Hello':5,'world':5,'this':4,'is':2,'a':1,'test':4}
```
### 输出结果
```
未找到输出结果
```
源链接: [https://www.runoob.com/python3/python-word-length.html](https://www.runoob.com/python3/python-word-length.html)