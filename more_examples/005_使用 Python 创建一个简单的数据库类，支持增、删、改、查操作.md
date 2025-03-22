# 使用 Python 创建一个简单的数据库类，支持增、删、改、查操作

## 题目描述
Python3 实例
我们将创建一个简单的数据库类SimpleDB，它使用 Python 的字典来模拟数据库表。这个类将支持基本的增、删、改、查操作。

## 实例
### 代码
```python
classSimpleDB:
     def__init__(self):
         self.db={}
     definsert(self,key,value):
         self.db[key]=value
         print(f"Inserted: {key} -> {value}")
     defdelete(self,key):
         ifkeyinself.db:
             delself.db[key]
             print(f"Deleted: {key}")
         else:
             print(f"Key {key} not found.")
     defupdate(self,key,value):
         ifkeyinself.db:
             self.db[key]=value
             print(f"Updated: {key} -> {value}")
         else:
             print(f"Key {key} not found.")
     defselect(self,key):
         ifkeyinself.db:
             print(f"Selected: {key} -> {self.db[key]}")
         else:
             print(f"Key {key} not found.")
     defshow_all(self):
         print("Database Contents:")
         forkey,valueinself.db.items():
             print(f"{key} -> {value}")
 # Example usage
 db=SimpleDB()
 db.insert('name','Alice')
 db.insert('age',30)
 db.show_all()
 db.update('age',31)
 db.select('name')
 db.delete('age')
 db.show_all()
```
### 输出结果
```
Inserted: name -> Alice
Inserted: age -> 30
Database Contents:
name -> Alice
age -> 30
Updated: age -> 31
Selected: name -> Alice
Deleted: age
Database Contents:
name -> Alice
```
源链接: [https://www.runoob.com/python3/python-database-class.html](https://www.runoob.com/python3/python-database-class.html)