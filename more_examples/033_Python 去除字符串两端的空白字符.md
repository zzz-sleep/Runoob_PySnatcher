# Python 去除字符串两端的空白字符

## 题目描述
Python3 实例
在 Python 中，可以使用strip()方法来去除字符串两端的空白字符（包括空格、制表符、换行符等）。这个方法会返回一个新的字符串，原字符串不会被修改。

## 实例
### 代码
```python
text="   Hello, World!   "
 trimmed_text=text.strip()
 print(f"Original: '{text}'")
 print(f"Trimmed: '{trimmed_text}'")
```
### 输出结果
```
Original: '   Hello, World!   '
Trimmed: 'Hello, World!'
```
源链接: [https://www.runoob.com/python3/python-trim-string.html](https://www.runoob.com/python3/python-trim-string.html)