# Python 简单的银行系统

## 题目描述
Python3 实例
以下实例为学习 Python 银行系统的操作：

## 实例
### 代码
```python
means=[0,0,0]
 loan=0
 rate=0
 pay=0
 investment=0
 annual_rate=0
 # 计算定投预期收益
 # 定投收益的计算公式为：M=a(1+x)[-1+(1+x)^n]/x;
 # 其中M代表预期收益，a代表每期定投金额，x代表收益率，而n代表定投期数。
 # 假设用户每月定投金额为300元，一年也就是3600元，年收益率为15%，
 # 定投期限为35年，则可以计算出收益为3600(1+15%)[-1+(1+15%)^35]/15%=3648044元。
 deffixed_investment(inv,a_rate,y):
     globalmeans
     inv=12* inv
     a_rate=a_rate /100
     ifa_rate==0:
         expected=0
     else:
         expected=inv *(1+ a_rate)*(pow((1+ a_rate),y)-1)/ a_rate
     print("定投的预期收入为: %.2f"% expected)
     means[1]=expected
     returnexpected
 defbalance():
     total=0
     foriinmeans:
         total +=i
     print("你的资产总额为：%.2f"% total)
     print("你的资产明细为：\n")
     print("存款：%.2f"% means[0])
     print("理财：%.2f"% means[1])
     print("负债：%.2f"% means[2])
 defsaving(amount):
     globalmeans
     ifamount<0:
         print("存款金额不可小于 0！")
     else:
         means[0]+=amount
         print("已存款：%.2f 元"% amount)
         print("当前余额：%.2f 元"% means[0])
 defdraw_money(drawing):
     globalmeans
     ifdrawing<0:
         print("取款金额不可小于 0！")
     elifdrawing>means[0]:
         print("取款金额不可超过余额！")
     else:
         means[0]-=drawing
         print("已取款： %.2f 元"% drawing)
         print("当前余额： %.2f 元"% means[0])
 defloans(loan,rate,pay,years):
     globalmeans
     ifpay<(loan - pay)* rate:
         print("你是还不完的！！！")
     else:
         ifyears==0:
             count=0
             whileloan>0:
                 loan -=pay
                 loan *=(1+ rate)
                 count +=1
             print("将在 %d 年后还完贷款。"% count)
         else:
             for_inrange(years):
                 loan -=pay
                 ifloan==0:
                     break
                 else:
                     loan *=(1+ rate)
                     print("你现在的负债是: %.2f"% loan)
             # means[2] = loan
             returnloan
 # 未来财务状况
 deffuture(years):
     income=fixed_investment(investment,annual_rate,years)
     debt=loans(loan,rate,pay,years)
     captial=means[0]+ income - debt
     print("你第%i年的总资产有: %.3f"%(years,captial))
 definit():
     print()
     print('''以下为可办理的业务：1. 查询资产2. 存款3. 取款4. 计算复利5. 计算贷款6. 计算未来资产q. 退出''')
 defmain():
     init()
     whileTrue:
         choice=input("请输入您要办理的业务代码: ")
         #  查询余额
         ifchoice=="1":
             balance()
         # 存款
         elifchoice=="2":
             inc=float(input("请输入存款金额: "))
             saving(inc)
         # 取款
         elifchoice=="3":
             dec=float(input("请输入取款金额: "))
             draw_money(dec)
         # 计算定投
         elifchoice=="4":
             investment=float(input("请输入每月定投金额: "))
             annual_rate=float(input("请输入年收益率: "))
             years=int(input("请输入定投期限(年): "))
             ifinvestment<=0orannual_rate<=0oryears<=0:
                 print("输入的数据有误")
             else:
                 money=fixed_investment(investment,annual_rate,years)
             print("最终收获: %.2f 元"% money)
         # 计算贷款
         elifchoice=="5":
             loan=float(input("请输入当前贷款: "))
             rate=float(input("请输入年利率: "))
             pay=float(input("请输入每年还款: "))
             ifloan<=0orrate<=0orpay<=0:
                 print("输入的数据有误")
             else:
                 loans(loan,rate,pay,0)
         elifchoice=="6":
             years=int(input("希望查询多少年后的财务状况? "))
             future(years)
         # 退出
         elifchoice=="q":
             print("欢迎下次光临！再见！")
             break
         else:
             print("你输入的指令有误，请重新输入\n")
 if__name__=='__main__':
     main()
```
### 输出结果
```
未找到输出结果
```
源链接: [https://www.runoob.com/python3/python-bank-system.html](https://www.runoob.com/python3/python-bank-system.html)