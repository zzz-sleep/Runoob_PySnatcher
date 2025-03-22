# Python 使用类模拟一个在线购物车，支持添加商品、删除商品等操作

## 题目描述
Python3 实例
我们将使用 Python 类来模拟一个在线购物车。购物车将支持添加商品、删除商品、查看购物车内容以及计算总价等功能。

## 实例
### 代码
```python
classShoppingCart:
     def__init__(self):
         self.items=[]
     defadd_item(self,name,price,quantity=1):
         self.items.append({'name': name,'price': price,'quantity': quantity})
     defremove_item(self,name):
         self.items=[itemforiteminself.itemsifitem['name']!=name]
     defview_cart(self):
         ifnotself.items:
             print("Your shopping cart is empty.")
         else:
             foriteminself.items:
                 print(f"{item['name']} - ${item['price']} x {item['quantity']}")
     defcalculate_total(self):
         returnsum(item['price']* item['quantity']foriteminself.items)
 # 示例使用
 cart=ShoppingCart()
 cart.add_item("Apple",0.5,3)
 cart.add_item("Banana",0.3,5)
 cart.view_cart()
 print(f"Total: ${cart.calculate_total()}")
 cart.remove_item("Banana")
 cart.view_cart()
 print(f"Total: ${cart.calculate_total()}")
```
### 输出结果
```
Apple - $0.5 x 3
Banana - $0.3 x 5
Total: $2.4
Apple - $0.5 x 3
Total: $1.5
```
源链接: [https://www.runoob.com/python3/python-shopping-cart.html](https://www.runoob.com/python3/python-shopping-cart.html)