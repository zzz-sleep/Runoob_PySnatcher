# Python 移除字符串中的指定位置字符

## 题目描述
Python3 实例
给定一个字符串，然后移除指定位置的字符：

## 实例
### 代码
```python
test_str="Runoob"
 # 输出原始字符串
 print("原始字符串为 : "+ test_str)
 # 移除第三个字符 n
 new_str=""
 foriinrange(0,len(test_str)):
     ifi!=2:
         new_str=new_str + test_str[i]
 print("字符串移除后为 : "+ new_str)
```
### 输出结果
```
原始字符串为 : Runoob
字符串移除后为 : Ruoob
```
源链接: [https://www.runoob.com/python3/pyhton-remove-ith-character-from-string.html](https://www.runoob.com/python3/pyhton-remove-ith-character-from-string.html)