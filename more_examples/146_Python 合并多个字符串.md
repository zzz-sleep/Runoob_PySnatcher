# Python 合并多个字符串

## 题目描述
Python3 实例
在 Python 中，合并多个字符串可以通过多种方式实现，包括使用加号+、join()方法或格式化字符串。下面我们将通过一个简单的例子来演示如何合并多个字符串。

## 实例
### 代码
```python
# 定义多个字符串
 str1="Hello"
 str2="World"
 str3="!"
 # 使用加号合并字符串
 combined_str1=str1 +" "+ str2 + str3
 # 使用 join() 方法合并字符串
 combined_str2=" ".join([str1,str2])+ str3
 # 使用格式化字符串合并
 combined_str3=f"{str1} {str2}{str3}"
 # 输出结果
 print(combined_str1)
 print(combined_str2)
 print(combined_str3)
```
### 输出结果
```
Hello World!
Hello World!
Hello World!
```
源链接: [https://www.runoob.com/python3/python-merge-strings.html](https://www.runoob.com/python3/python-merge-strings.html)