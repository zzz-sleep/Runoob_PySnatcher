# Python 将字符串作为代码执行

## 题目描述
Python3 实例
给定一个字符串代码，然后使用  exec()  来执行字符串代码。

## 实例 1：使用内置方法 exec()
### 代码
```python
defexec_code():LOC="""def factorial(num): 
    fact=1 
    for i in range(1,num+1): 
        fact = fact*i 
    return fact 
print(factorial(5))"""exec(LOC)exec_code()
```
### 输出结果
```

120

```
源链接: [https://www.runoob.com/python3/python-execute-string-code.html](https://www.runoob.com/python3/python-execute-string-code.html)