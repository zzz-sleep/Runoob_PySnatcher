# 使用 Python 实现一个图书馆管理系统

## 题目描述
Python3 实例
我们将使用 Python 实现一个简单的图书馆管理系统。该系统允许用户添加书籍、删除书籍、查找书籍以及显示所有书籍。我们将使用字典来存储书籍信息，其中键是书籍的 ISBN 号，值是书籍的详细信息（如书名、作者等）。

## 实例
### 代码
```python
classLibrary:
     def__init__(self):
         self.books={}
     defadd_book(self,isbn,title,author):
         ifisbninself.books:
             print("Book already exists!")
         else:
             self.books[isbn]={'title': title,'author': author}
             print("Book added successfully!")
     defdelete_book(self,isbn):
         ifisbninself.books:
             delself.books[isbn]
             print("Book deleted successfully!")
         else:
             print("Book not found!")
     deffind_book(self,isbn):
         ifisbninself.books:
             print(f"Book found: {self.books[isbn]}")
         else:
             print("Book not found!")
     defdisplay_books(self):
         ifnotself.books:
             print("No books in the library!")
         else:
             forisbn,detailsinself.books.items():
                 print(f"ISBN: {isbn}, Title: {details['title']}, Author: {details['author']}")
 # Example usage
 library=Library()
 library.add_book("1234567890","Python Programming","John Doe")
 library.add_book("0987654321","Advanced Python","Jane Smith")
 library.display_books()
 library.find_book("1234567890")
 library.delete_book("0987654321")
 library.display_books()
```
### 输出结果
```
Book added successfully!
Book added successfully!
ISBN: 1234567890, Title: Python Programming, Author: John Doe
ISBN: 0987654321, Title: Advanced Python, Author: Jane Smith
Book found: {'title': 'Python Programming', 'author': 'John Doe'}
Book deleted successfully!
ISBN: 1234567890, Title: Python Programming, Author: John Doe
```
源链接: [https://www.runoob.com/python3/python-library-management.html](https://www.runoob.com/python3/python-library-management.html)