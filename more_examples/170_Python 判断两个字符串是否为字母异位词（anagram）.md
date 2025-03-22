# Python 判断两个字符串是否为字母异位词（anagram）

## 题目描述
Python3 实例
字母异位词（anagram）是指由相同字母重新排列形成的不同单词或短语。例如，"listen" 和 "silent" 就是字母异位词。我们可以通过比较两个字符串的字母组成来判断它们是否为字母异位词。

## 实例
### 代码
```python
defis_anagram(str1,str2):
     # 去除空格并将字符串转换为小写
     str1=str1.replace(" ","").lower()
     str2=str2.replace(" ","").lower()
     # 如果两个字符串的长度不同，直接返回 False
     iflen(str1)!=len(str2):
         returnFalse
     # 对两个字符串进行排序并比较
     returnsorted(str1)==sorted(str2)
 # 测试
 print(is_anagram("listen","silent"))# True
 print(is_anagram("apple","pale"))# False
```
### 输出结果
```
True
False
```
源链接: [https://www.runoob.com/python3/python-anagram-strings.html](https://www.runoob.com/python3/python-anagram-strings.html)