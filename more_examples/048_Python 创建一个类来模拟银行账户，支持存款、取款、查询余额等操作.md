# Python 创建一个类来模拟银行账户，支持存款、取款、查询余额等操作

## 题目描述
Python3 实例
我们将创建一个名为BankAccount的类，用于模拟银行账户的基本操作。这个类将包含存款、取款和查询余额的功能。我们将使用实例变量来存储账户余额，并提供方法来操作这些变量。

## 实例
### 代码
```python
classBankAccount:
     def__init__(self,owner,balance=0):
         self.owner=owner
         self.balance=balance
     defdeposit(self,amount):
         ifamount &gt;0:
             self.balance+=amount
             print(f"Deposited {amount}. New balance is {self.balance}.")
         else:
             print("Deposit amount must be positive.")
     defwithdraw(self,amount):
         ifamount &gt;self.balance:
             print("Insufficient funds.")
         elifamount &lt;=0:
             print(&quot;Withdrawal amount must be positive.&quot;)
         else:
             self.balance-=amount
             print(f&quot;Withdrew{amount}.Newbalanceis{self.balance}.&quot;)
     defget_balance(self):
         returnself.balance
 # 示例使用
 account=BankAccount(&quot;John Doe&quot;,100)
 account.deposit(50)
 account.withdraw(20)
 print(f&quot;Current balance:{account.get_balance()}&quot;)
```
### 输出结果
```
Deposited 50. New balance is 150.
Withdrew 20. New balance is 130.
Current balance: 130
```
源链接: [https://www.runoob.com/python3/python-bank-account-class.html](https://www.runoob.com/python3/python-bank-account-class.html)