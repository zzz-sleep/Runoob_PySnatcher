# Python 实现一个类来模拟排队系统

## 题目描述
Python3 实例
我们将使用 Python 实现一个简单的排队系统类。这个类将允许用户添加顾客到队列中，移除顾客，以及查看当前队列的状态。

## 实例
### 代码
```python
classQueueSystem:
     def__init__(self):
         self.queue=[]
     defadd_customer(self,name):
         self.queue.append(name)
         print(f"{name} has been added to the queue.")
     defremove_customer(self):
         ifself.queue:
             removed_customer=self.queue.pop(0)
             print(f"{removed_customer} has been removed from the queue.")
         else:
             print("The queue is empty.")
     defshow_queue(self):
         ifself.queue:
             print("Current queue:")
             fori,customerinenumerate(self.queue,1):
                 print(f"{i}. {customer}")
         else:
             print("The queue is empty.")
 # Example usage
 queue_system=QueueSystem()
 queue_system.add_customer("Alice")
 queue_system.add_customer("Bob")
 queue_system.show_queue()
 queue_system.remove_customer()
 queue_system.show_queue()
```
### 输出结果
```
Alice has been added to the queue.
Bob has been added to the queue.
Current queue:
1. Alice
2. Bob
Alice has been removed from the queue.
Current queue:
1. Bob
```
源链接: [https://www.runoob.com/python3/python-queue-system.html](https://www.runoob.com/python3/python-queue-system.html)