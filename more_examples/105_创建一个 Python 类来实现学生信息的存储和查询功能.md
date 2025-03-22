# 创建一个 Python 类来实现学生信息的存储和查询功能

## 题目描述
Python3 实例
我们将创建一个名为Student的 Python 类，用于存储学生的基本信息（如姓名、年龄、学号等），并提供查询这些信息的方法。

## 实例
### 代码
```python
classStudent:
     def__init__(self,name,age,student_id):
         self.name=name
         self.age=age
         self.student_id=student_id
     defget_name(self):
         returnself.name
     defget_age(self):
         returnself.age
     defget_student_id(self):
         returnself.student_id
     defdisplay_info(self):
         print(f"Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}")
 # 示例使用
 student1=Student("Alice",20,"S12345")
 student1.display_info()
```
### 输出结果
```
Name: Alice, Age: 20, Student ID: S12345
```
源链接: [https://www.runoob.com/python3/python-student-info.html](https://www.runoob.com/python3/python-student-info.html)