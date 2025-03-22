# Python 实现一个类，表示一个简单的电子书

## 题目描述
Python3 实例
我们将创建一个简单的电子书类EBook，该类包含书名、作者、页数和当前页码等属性。我们还将实现一些方法，如翻页、获取当前页内容等。

## 实例
### 代码
```python
classEBook:
     def__init__(self,title,author,pages):
         self.title=title
         self.author=author
         self.pages=pages
         self.current_page=1
     defnext_page(self):
         ifself.current_page1:
             self.current_page-=1
         else:
             print("You are already at the beginning of the book.")
     defget_current_page_content(self):
         returnf"Page {self.current_page} of {self.pages}"
     def__str__(self):
         returnf"'{self.title}' by {self.author}, {self.pages} pages"
 # 示例使用
 book=EBook("Python Programming","John Doe",300)
 print(book)
 print(book.get_current_page_content())
 book.next_page()
 print(book.get_current_page_content())
 book.previous_page()
 print(book.get_current_page_content())
```
### 输出结果
```
'Python Programming' by John Doe, 300 pages
Page 1 of 300
Page 2 of 300
Page 1 of 300
```
源链接: [https://www.runoob.com/python3/python-ebook-class.html](https://www.runoob.com/python3/python-ebook-class.html)