# 使用 Python 实现一个密码管理器类

## 题目描述
Python3 实例
我们将使用 Python 实现一个简单的密码管理器类。这个类将允许用户存储、检索和删除密码。密码将存储在一个字典中，其中键是账户名称，值是密码。为了简单起见，密码将以明文形式存储，但在实际应用中，应该使用加密技术来保护密码。

## 实例
### 代码
```python
classPasswordManager:
     def__init__(self):
         self.passwords={}
     defadd_password(self,account,password):
         self.passwords[account]=password
         print(f"Password for {account} added successfully.")
     defget_password(self,account):
         ifaccountinself.passwords:
             returnself.passwords[account]
         else:
             returnf"No password found for {account}."
     defdelete_password(self,account):
         ifaccountinself.passwords:
             delself.passwords[account]
             print(f"Password for {account} deleted successfully.")
         else:
             print(f"No password found for {account}.")
     deflist_accounts(self):
         ifself.passwords:
             print("Accounts with stored passwords:")
             foraccountinself.passwords:
                 print(account)
         else:
             print("No accounts with stored passwords.")
```
### 输出结果
```
未找到输出结果
```
## 实例
### 代码
```python
# 示例使用
 pm=PasswordManager()
 pm.add_password("email","myemailpassword")
 pm.add_password("bank","mybankpassword")
 print(pm.get_password("email"))# 输出: myemailpassword
 pm.delete_password("bank")
 pm.list_accounts()# 输出: Accounts with stored passwords: email
```
### 输出结果
```
未找到输出结果
```
源链接: [https://www.runoob.com/python3/python-password-manager.html](https://www.runoob.com/python3/python-password-manager.html)