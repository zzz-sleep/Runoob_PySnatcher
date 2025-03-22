# Python 实现一个银行账户类，支持存款和取款

## 题目描述
Python3 实例
我们将创建一个简单的银行账户类，这个类将包含账户的基本信息，如账户名和余额，并且支持存款和取款操作。

## 实例
### 代码
```python
classBankAccount:
     def__init__(self,account_name,initial_balance=0):
         self.account_name=account_name
         self.balance=initial_balance
     defdeposit(self,amount):
         ifamount>0:
             self.balance+=amount
             print(f"Deposited {amount}. New balance is {self.balance}.")
         else:
             print("Deposit amount must be positive.")
     defwithdraw(self,amount):
         ifamount>0andamount<=self.balance:
             self.balance-=amount
             print(f"Withdrew {amount}. New balance is {self.balance}.")
         else:
             print("Invalid withdrawal amount.")
     defget_balance(self):
         returnself.balance
 # 示例使用
 account=BankAccount("John Doe",100)
 account.deposit(50)
 account.withdraw(20)
 print(f"Final balance is {account.get_balance()}.")
```
### 输出结果
```
Deposited 50. New balance is 150.
Withdrew 20. New balance is 130.
Final balance is 130.
```
源链接: [https://www.runoob.com/python3/python-bank-account.html](https://www.runoob.com/python3/python-bank-account.html)