# Python 实现一个类，支持文本文件的读取和写入功能

## 题目描述
Python3 实例
我们将创建一个名为TextFileHandler的类，该类将支持文本文件的读取和写入功能。这个类将包含两个主要方法：read_file用于读取文件内容，write_file用于将内容写入文件。

## 实例
### 代码
```python
classTextFileHandler:
     def__init__(self,filename):
         self.filename=filename
     defread_file(self):
         try:
             withopen(self.filename,'r')asfile:
                 content=file.read()
             returncontent
         exceptFileNotFoundError:
             return"File not found."
     defwrite_file(self,content):
         withopen(self.filename,'w')asfile:
             file.write(content)
         return"File written successfully."
 # 示例使用
 handler=TextFileHandler('example.txt')
 handler.write_file("Hello, World!")
 print(handler.read_file())
```
### 输出结果
```
Hello, World!
```
源链接: [https://www.runoob.com/python3/python-file-read-write.html](https://www.runoob.com/python3/python-file-read-write.html)