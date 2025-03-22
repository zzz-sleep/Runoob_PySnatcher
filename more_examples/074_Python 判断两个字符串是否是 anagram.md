# Python 判断两个字符串是否是 anagram

## 题目描述
Python3 实例
Anagram 是指由相同字母重新排列而成的单词或短语。例如，"listen" 和 "silent" 就是一对 anagram。我们可以通过比较两个字符串的字母组成来判断它们是否是 anagram。

## 实例
### 代码
```python
defis_anagram(str1,str2):
     # 移除空格并将字符串转换为小写
     str1=str1.replace(" ","").lower()
     str2=str2.replace(" ","").lower()
     # 检查两个字符串的长度是否相同
     iflen(str1)!=len(str2):
         returnFalse
     # 对字符串进行排序并比较
     returnsorted(str1)==sorted(str2)
 # 测试
 print(is_anagram("listen","silent"))# True
 print(is_anagram("triangle","integral"))# True
 print(is_anagram("apple","pale"))# False
```
### 输出结果
```
True
True
False
```
源链接: [https://www.runoob.com/python3/python-anagram-check.html](https://www.runoob.com/python3/python-anagram-check.html)