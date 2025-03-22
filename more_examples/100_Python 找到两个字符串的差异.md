# Python 找到两个字符串的差异

## 题目描述
Python3 实例
在 Python 中，我们可以使用difflib模块来比较两个字符串并找出它们之间的差异。difflib模块提供了一个Differ类，它可以逐行比较两个字符串，并生成一个差异报告。
下面是一个示例代码，展示如何使用difflib来找到两个字符串的差异：

## 实例
### 代码
```python
importdifflib
 deffind_string_differences(str1,str2):
     differ=difflib.Differ()
     diff=differ.compare(str1.splitlines(),str2.splitlines())
     return'n'.join(diff)
 str1="""Hello world!This is a test.Python is fun."""
 str2="""Hello world!This is a test.Python is awesome."""
 differences=find_string_differences(str1,str2)
 print(differences)
```
### 输出结果
```
  Hello world!
  This is a test.
- Python is fun.
+ Python is awesome.
```
源链接: [https://www.runoob.com/python3/python-string-difference.html](https://www.runoob.com/python3/python-string-difference.html)