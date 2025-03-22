# Python 对字符串切片及翻转

## 题目描述
Python3 实例
给定一个字符串，从头部或尾部截取指定数量的字符串，然后将其翻转拼接。

## 实例
### 代码
```python
defrotate(input,d):Lfirst=input[0:d]Lsecond=input[d:]Rfirst=input[0:len(input)-d]Rsecond=input[len(input)-d:]print("头部切片翻转 :",(Lsecond+Lfirst))print("尾部切片翻转 :",(Rsecond+Rfirst))if__name__=="__main__":input='Runoob'd=2# 截取两个字符rotate(input,d)
```
### 输出结果
```

头部切片翻转 :  noobRu
尾部切片翻转 :  obRuno

```
源链接: [https://www.runoob.com/python3/python-slicing-rotate-string.html](https://www.runoob.com/python3/python-slicing-rotate-string.html)