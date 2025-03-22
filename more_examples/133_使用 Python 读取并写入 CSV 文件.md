# 使用 Python 读取并写入 CSV 文件

## 题目描述
Python3 实例
在 Python 中，我们可以使用内置的csv模块来读取和写入 CSV 文件。CSV 文件是一种常见的文件格式，用于存储表格数据。下面是一个简单的示例，展示如何读取一个 CSV 文件并将其内容写入另一个 CSV 文件。

## 实例
### 代码
```python
importcsv
 # 读取 CSV 文件
 withopen('input.csv',mode='r',newline='',encoding='utf-8')asinfile:
     reader=csv.reader(infile)
     data=[rowforrowinreader]
 # 写入 CSV 文件
 withopen('output.csv',mode='w',newline='',encoding='utf-8')asoutfile:
     writer=csv.writer(outfile)
     writer.writerows(data)
```
### 输出结果
```
Name,Age,City
Alice,30,New York
Bob,25,Los Angeles
Charlie,35,Chicago
```
源链接: [https://www.runoob.com/python3/python-csv-read-write.html](https://www.runoob.com/python3/python-csv-read-write.html)