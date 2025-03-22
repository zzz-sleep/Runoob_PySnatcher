# Python 求两个字符串的最长公共子串

## 题目描述
Python3 实例
最长公共子串问题是指给定两个字符串，找到它们之间最长的公共子串。子串是指字符串中连续的字符序列。我们可以使用动态规划的方法来解决这个问题。

## 实例
### 代码
```python
deflongest_common_substring(s1,s2):
     m=len(s1)
     n=len(s2)
     # 创建一个二维数组来存储最长公共子串的长度
     dp=[[0]*(n +1)for_inrange(m +1)]
     max_length=0# 记录最长公共子串的长度
     end_pos=0# 记录最长公共子串的结束位置
     foriinrange(1,m +1):
         forjinrange(1,n +1):
             ifs1[i -1]==s2[j -1]:
                 dp[i][j]=dp[i -1][j -1]+1
                 ifdp[i][j]>max_length:
                     max_length=dp[i][j]
                     end_pos=i
             else:
                 dp[i][j]=0
     # 返回最长公共子串
     returns1[end_pos - max_length:end_pos]
 # 测试
 s1="abcdef"
 s2="zbcdf"
 result=longest_common_substring(s1,s2)
 print("最长公共子串是:",result)
```
### 输出结果
```
最长公共子串是: bcd
```
源链接: [https://www.runoob.com/python3/python-longest-substring.html](https://www.runoob.com/python3/python-longest-substring.html)