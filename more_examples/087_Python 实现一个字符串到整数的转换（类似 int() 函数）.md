# Python 实现一个字符串到整数的转换（类似 int() 函数）

## 题目描述
Python3 实例
在 Python 中，我们可以通过自定义函数来实现字符串到整数的转换，类似于内置的int()函数。这个函数将处理字符串中的数字字符，并忽略前导空格和符号（+ 或 -），然后将这些字符转换为整数。

## 实例
### 代码
```python
defstr_to_int(s):
     s=s.strip()# 去除前导和尾随空格
     ifnots:
         return0
     sign=1
     ifs[0]=='-'ors[0]=='+':
         ifs[0]=='-':
             sign=-1
         s=s[1:]# 去除符号
     result=0
     forcharins:
         ifnotchar.isdigit():
             break
         result=result *10+(ord(char)-ord('0'))
     returnsign * result
 # 测试
 print(str_to_int("  123"))# 123
 print(str_to_int("  -456"))# -456
 print(str_to_int("  +789"))# 789
 print(str_to_int("  12a34"))# 12
```
### 输出结果
```
123
-456
789
12
```
源链接: [https://www.runoob.com/python3/python-string-to-int.html](https://www.runoob.com/python3/python-string-to-int.html)