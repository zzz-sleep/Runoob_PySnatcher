# Python 创建一个简单的 Tic-Tac-Toe 游戏类

## 题目描述
Python3 实例
Tic-Tac-Toe（井字棋）是一个经典的双人游戏，玩家轮流在 3x3 的网格上放置自己的标记（通常是 "X" 和 "O"）。游戏的目标是在水平、垂直或对角线上先形成一条连续的三个相同标记的线。下面我们将创建一个简单的 Tic-Tac-Toe 游戏类，包含基本的游戏逻辑和显示功能。

## 实例
### 代码
```python
classTicTacToe:
     def__init__(self):
         self.board=[[' 'for_inrange(3)]for_inrange(3)]
         self.current_player='X'
     defprint_board(self):
         forrowinself.board:
             print('|'.join(row))
             print('-'*5)
     defmake_move(self,row,col):
         ifself.board[row][col]==' ':
             self.board[row][col]=self.current_player
             self.current_player='O'ifself.current_player=='X'else'X'
         else:
             print("Invalid move! The cell is already occupied.")
     defcheck_winner(self):
         # Check rows
         forrowinself.board:
             ifrow[0]==row[1]==row[2]!=' ':
                 returnrow[0]
         # Check columns
         forcolinrange(3):
             ifself.board[0][col]==self.board[1][col]==self.board[2][col]!=' ':
                 returnself.board[0][col]
         # Check diagonals
         ifself.board[0][0]==self.board[1][1]==self.board[2][2]!=' ':
             returnself.board[0][0]
         ifself.board[0][2]==self.board[1][1]==self.board[2][0]!=' ':
             returnself.board[0][2]
         # Check for a tie
         ifall(cell!=' 'forrowinself.boardforcellinrow):
             return'Tie'
         returnNone
     defplay_game(self):
         whileTrue:
             self.print_board()
             print(f"Player {self.current_player}'s turn")
             row=int(input("Enter row (0, 1, 2): "))
             col=int(input("Enter column (0, 1, 2): "))
             self.make_move(row,col)
             winner=self.check_winner()
             ifwinner:
                 self.print_board()
                 ifwinner=='Tie':
                     print("It's a tie!")
                 else:
                     print(f"Player {winner} wins!")
                 break
```
### 输出结果
```
 | | 
-----
 | | 
-----
 | | 
-----
Player X's turn
Enter row (0, 1, 2): 0
Enter column (0, 1, 2): 0
X| | 
-----
 | | 
-----
 | | 
-----
Player O's turn
Enter row (0, 1, 2): 1
Enter column (0, 1, 2): 1
X| | 
-----
 |O| 
-----
 | | 
-----
...
```
源链接: [https://www.runoob.com/python3/python-tic-tac-toe.html](https://www.runoob.com/python3/python-tic-tac-toe.html)