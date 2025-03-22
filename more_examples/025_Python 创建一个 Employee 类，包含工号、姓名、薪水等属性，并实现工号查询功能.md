# Python 创建一个 Employee 类，包含工号、姓名、薪水等属性，并实现工号查询功能

## 题目描述
Python3 实例
我们将创建一个名为Employee的类，该类包含工号（id）、姓名（name）和薪水（salary）三个属性。此外，我们还将实现一个方法get_employee_by_id，用于根据工号查询员工信息。

## 实例
### 代码
```python
classEmployee:
     def__init__(self,id,name,salary):
         self.id=id
         self.name=name
         self.salary=salary
     defget_employee_by_id(self,id):
         ifself.id==id:
             returnself
         else:
             returnNone
 # 创建几个 Employee 对象
 employee1=Employee(1,"Alice",50000)
 employee2=Employee(2,"Bob",60000)
 employee3=Employee(3,"Charlie",70000)
 # 查询工号为 2 的员工
 result=employee1.get_employee_by_id(2)
 ifresult:
     print(f"Employee found: {result.name}, Salary: {result.salary}")
 else:
     print("Employee not found")
```
### 输出结果
```
Employee found: Bob, Salary: 60000
```
源链接: [https://www.runoob.com/python3/python-employee-class.html](https://www.runoob.com/python3/python-employee-class.html)