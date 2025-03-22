# 使用 Python 模块实现 REST API

## 题目描述
Python3 实例
我们将使用 Python 的 Flask 框架来实现一个简单的 REST API。Flask 是一个轻量级的 Web 框架，非常适合用来快速构建 Web 应用程序和 RESTful API。

## 实例
### 代码
```python
fromflaskimportFlask,jsonify,request
 app=Flask(__name__)
 # 示例数据
 books=[
     {"id":1,"title":"1984","author":"George Orwell"},
     {"id":2,"title":"To Kill a Mockingbird","author":"Harper Lee"},
     {"id":3,"title":"The Great Gatsby","author":"F. Scott Fitzgerald"}
 ]
 # 获取所有书籍
 @app.route('/books',methods=['GET'])
 defget_books():
     returnjsonify(books)
 # 获取特定书籍
 @app.route('/books/',methods=['GET'])
 defget_book(book_id):
     book=next((bookforbookinbooksifbook['id']==book_id),None)
     ifbook:
         returnjsonify(book)
     else:
         returnjsonify({"error":"Book not found"}),404
 # 添加新书籍
 @app.route('/books',methods=['POST'])
 defadd_book():
     new_book=request.get_json()
     books.append(new_book)
     returnjsonify(new_book),201
 # 更新书籍信息
 @app.route('/books/',methods=['PUT'])
 defupdate_book(book_id):
     book=next((bookforbookinbooksifbook['id']==book_id),None)
     ifbook:
         updated_data=request.get_json()
         book.update(updated_data)
         returnjsonify(book)
     else:
         returnjsonify({"error":"Book not found"}),404
 # 删除书籍
 @app.route('/books/',methods=['DELETE'])
 defdelete_book(book_id):
     globalbooks
     books=[bookforbookinbooksifbook['id']!=book_id]
     returnjsonify({"result":"Book deleted"})
 if__name__=='__main__':
     app.run(debug=True)
```
### 输出结果
```
未找到输出结果
```
源链接: [https://www.runoob.com/python3/python-rest-api.html](https://www.runoob.com/python3/python-rest-api.html)