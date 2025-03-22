# Python 约瑟夫生者死者小游戏

## 题目描述
Python3 实例
30 个人在一条船上，超载，需要 15 人下船。
于是人们排成一队，排队的位置即为他们的编号。
报数，从 1 开始，数到 9 的人下船。
如此循环，直到船上仅剩 15 人为止，问都有哪些编号的人下船了呢？

## 实例
### 代码
```python
people={}forxinrange(1,31):people[x]=1#print(people)check=0i=1j=0whilei<=31:ifi==31:i=1elifj==15:breakelse:ifpeople[i]==0:i+=1continueelse:check+=1ifcheck==9:people[i]=0check=0print("{}号下船了".format(i))j+=1else:i+=1continue
```
### 输出结果
```
9号下船了
18号下船了
27号下船了
6号下船了
16号下船了
26号下船了
7号下船了
19号下船了
30号下船了
12号下船了
24号下船了
8号下船了
22号下船了
5号下船了
23号下船了
```
源链接: [https://www.runoob.com/python3/python-joseph-life-dead-game.html](https://www.runoob.com/python3/python-joseph-life-dead-game.html)