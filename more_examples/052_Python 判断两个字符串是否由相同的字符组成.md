# Python 判断两个字符串是否由相同的字符组成

## 题目描述
Python3 实例
描述内容：在 Python 中，我们可以通过比较两个字符串的排序结果来判断它们是否由相同的字符组成。如果两个字符串的排序结果相同，那么它们包含的字符是相同的，只是顺序可能不同。

## 实例
### 代码
```python
defare_anagrams(str1,str2):
     returnsorted(str1)==sorted(str2)
 # 测试
 str1="listen"
 str2="silent"
 print(are_anagrams(str1,str2))
```
### 输出结果
```
True
```
源链接: [https://www.runoob.com/python3/python-same-characters.html](https://www.runoob.com/python3/python-same-characters.html)