# Python 创建一个简单的任务清单（to-do list）

## 题目描述
Python3 实例
一个简单的练习可以是创建一个简单的任务清单（to-do list）程序。

## 实例
### 代码
```python
# 简单的任务清单程序
 # 创建一个空的任务列表
 tasks=[]
 # 定义函数来添加任务
 defadd_task(task):
     tasks.append(task)
     print(f"任务 '{task}' 已添加.")
 # 定义函数来显示任务列表
 defshow_tasks():
     ifnottasks:
         print("任务清单是空的.")
     else:
         print("任务清单:")
         forindex,taskinenumerate(tasks,start=1):
             print(f"{index}. {task}")
 # 主程序循环
 whileTrue:
     print("\n选择一个选项:")
     print("1. 添加任务")
     print("2. 显示任务清单")
     print("3. 退出")
     choice=input("输入选项编号: ")
     ifchoice=="1":
         new_task=input("输入新任务: ")
         add_task(new_task)
     elifchoice=="2":
         show_tasks()
     elifchoice=="3":
         print("退出程序.")
         break
     else:
         print("无效的选项，请重新输入.")
```
### 输出结果
```
未找到输出结果
```
源链接: [https://www.runoob.com/python3/python-to-do-list.html](https://www.runoob.com/python3/python-to-do-list.html)