# 使用 Python 实现一个支持排序和查找功能的链表

## 题目描述
Python3 实例
我们将使用 Python 实现一个简单的链表，并为其添加排序和查找功能。链表是一种常见的数据结构，它由一系列节点组成，每个节点包含数据和指向下一个节点的指针。

## 实例
### 代码
```python
classNode:
     def__init__(self,data):
         self.data=data
         self.next=None
 classLinkedList:
     def__init__(self):
         self.head=None
     defappend(self,data):
         new_node=Node(data)
         ifnotself.head:
             self.head=new_node
             return
         last_node=self.head
         whilelast_node.next:
             last_node=last_node.next
         last_node.next=new_node
     defdisplay(self):
         current=self.head
         whilecurrent:
             print(current.data,end=" -&gt; ")
             current=current.next
         print("None")
     defsort(self):
         ifnotself.head:
             return
         sorted_list=[]
         current=self.head
         whilecurrent:
             sorted_list.append(current.data)
             current=current.next
         sorted_list.sort()
         self.head=None
         foriteminsorted_list:
             self.append(item)
     defsearch(self,key):
         current=self.head
         whilecurrent:
             ifcurrent.data==key:
                 returnTrue
             current=current.next
         returnFalse
 # 示例使用
 ll=LinkedList()
 ll.append(3)
 ll.append(1)
 ll.append(4)
 ll.append(2)
 print("原始链表:")
 ll.display()
 ll.sort()
 print("排序后的链表:")
 ll.display()
 print("查找元素 4:",ll.search(4))
 print("查找元素 5:",ll.search(5))
```
### 输出结果
```
原始链表:
3 -&gt; 1 -&gt; 4 -&gt; 2 -&gt; None
排序后的链表:
1 -&gt; 2 -&gt; 3 -&gt; 4 -&gt; None
查找元素 4: True
查找元素 5: False
```
源链接: [https://www.runoob.com/python3/python-linked-list.html](https://www.runoob.com/python3/python-linked-list.html)