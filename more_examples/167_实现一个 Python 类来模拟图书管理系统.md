# 实现一个 Python 类来模拟图书管理系统

## 题目描述
Python3 实例
我们将创建一个简单的 Python 类来模拟图书管理系统。这个系统将允许用户添加书籍、删除书籍、查找书籍以及列出所有书籍。每本书将包含书名和作者两个属性。

## 实例
### 代码
```python
classBook:
     def__init__(self,title,author):
         self.title=title
         self.author=author
     def__str__(self):
         returnf"{self.title} by {self.author}"
 classLibrary:
     def__init__(self):
         self.books=[]
     defadd_book(self,title,author):
         new_book=Book(title,author)
         self.books.append(new_book)
         print(f"Added: {new_book}")
     defremove_book(self,title):
         forbookinself.books:
             ifbook.title==title:
                 self.books.remove(book)
                 print(f"Removed: {book}")
                 return
         print(f"Book with title '{title}' not found.")
     deffind_book(self,title):
         forbookinself.books:
             ifbook.title==title:
                 print(f"Found: {book}")
                 returnbook
         print(f"Book with title '{title}' not found.")
         returnNone
     deflist_books(self):
         ifnotself.books:
             print("No books in the library.")
         else:
             print("Books in the library:")
             forbookinself.books:
                 print(book)
 # Example usage
 library=Library()
 library.add_book("1984","George Orwell")
 library.add_book("To Kill a Mockingbird","Harper Lee")
 library.list_books()
 library.find_book("1984")
 library.remove_book("1984")
 library.list_books()
```
### 输出结果
```
Added: 1984 by George Orwell
Added: To Kill a Mockingbird by Harper Lee
Books in the library:
1984 by George Orwell
To Kill a Mockingbird by Harper Lee
Found: 1984 by George Orwell
Removed: 1984 by George Orwell
Books in the library:
To Kill a Mockingbird by Harper Lee
```
源链接: [https://www.runoob.com/python3/python-library-system.html](https://www.runoob.com/python3/python-library-system.html)