# 使用 Python 实现一个简单的在线聊天室类

## 题目描述
Python3 实例
我们将使用 Python 实现一个简单的在线聊天室类。这个聊天室类将允许用户加入聊天室、发送消息以及查看聊天记录。我们将使用一个列表来存储聊天记录，并使用类方法来管理用户和消息。

## 实例
### 代码
```python
classChatRoom:
     def__init__(self,name):
         self.name=name
         self.users=[]
         self.messages=[]
     defjoin(self,user):
         self.users.append(user)
         self.messages.append(f"{user} 加入了聊天室。")
     defleave(self,user):
         self.users.remove(user)
         self.messages.append(f"{user} 离开了聊天室。")
     defsend_message(self,user,message):
         self.messages.append(f"{user}: {message}")
     defshow_messages(self):
         formessageinself.messages:
             print(message)
 # 示例使用
 chat_room=ChatRoom("Python 聊天室")
 chat_room.join("Alice")
 chat_room.join("Bob")
 chat_room.send_message("Alice","大家好！")
 chat_room.send_message("Bob","你好 Alice！")
 chat_room.leave("Alice")
 chat_room.show_messages()
```
### 输出结果
```
Alice 加入了聊天室。
Bob 加入了聊天室。
Alice: 大家好！
Bob: 你好 Alice！
Alice 离开了聊天室。
```
源链接: [https://www.runoob.com/python3/python-chat-room.html](https://www.runoob.com/python3/python-chat-room.html)