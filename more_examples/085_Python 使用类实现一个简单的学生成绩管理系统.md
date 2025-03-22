# Python 使用类实现一个简单的学生成绩管理系统

## 题目描述
Python3 实例
我们将使用 Python 类来实现一个简单的学生成绩管理系统。这个系统将允许我们添加学生、记录他们的成绩，并计算每个学生的平均成绩。

## 实例
### 代码
```python
classStudent:
     def__init__(self,name):
         self.name=name
         self.grades=[]
     defadd_grade(self,grade):
         self.grades.append(grade)
     defaverage_grade(self):
         returnsum(self.grades)/len(self.grades)ifself.gradeselse0
 classGradeManager:
     def__init__(self):
         self.students=[]
     defadd_student(self,name):
         self.students.append(Student(name))
     defget_student(self,name):
         forstudentinself.students:
             ifstudent.name==name:
                 returnstudent
         returnNone
     defadd_grade_to_student(self,name,grade):
         student=self.get_student(name)
         ifstudent:
             student.add_grade(grade)
         else:
             print(f"Student {name} not found.")
     defshow_average_grades(self):
         forstudentinself.students:
             print(f"{student.name}'s average grade is {student.average_grade():.2f}")
 # 示例使用
 manager=GradeManager()
 manager.add_student("Alice")
 manager.add_student("Bob")
 manager.add_grade_to_student("Alice",90)
 manager.add_grade_to_student("Alice",85)
 manager.add_grade_to_student("Bob",78)
 manager.add_grade_to_student("Bob",82)
 manager.show_average_grades()
```
### 输出结果
```
Alice's average grade is 87.50
Bob's average grade is 80.00
```
源链接: [https://www.runoob.com/python3/python-student-grades.html](https://www.runoob.com/python3/python-student-grades.html)