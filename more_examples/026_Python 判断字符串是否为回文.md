# Python 判断字符串是否为回文

## 题目描述
Python3 实例
回文是指正读和反读都相同的字符串，例如 "madam" 或 "racecar"。我们可以通过比较字符串和它的反转字符串来判断一个字符串是否是回文。

## 实例
### 代码
```python
defis_palindrome(s):
     # 将字符串转换为小写并移除空格
     s=s.lower().replace(" ","")
     # 比较字符串和它的反转
     returns==s[::-1]
 # 测试
 test_string="A man a plan a canal Panama"
 print(is_palindrome(test_string))
```
### 输出结果
```
True
```
源链接: [https://www.runoob.com/python3/python-palindrome-check.html](https://www.runoob.com/python3/python-palindrome-check.html)