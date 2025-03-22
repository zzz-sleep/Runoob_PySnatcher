# Python 实现一个迷宫求解算法

## 题目描述
Python3 实例
我们将使用深度优先搜索（DFS）算法来解决一个简单的迷宫问题。迷宫由一个二维数组表示，其中0表示可通行的路径，1表示墙壁，2表示起点，3表示终点。我们将从起点开始，尝试找到一条通往终点的路径。

## 实例
### 代码
```python
defsolve_maze(maze,start,end):
     rows,cols=len(maze),len(maze[0])
     visited=[[Falsefor_inrange(cols)]for_inrange(rows)]
     path=[]
     defdfs(x,y):
         ifx=rowsory=colsormaze[x][y]==1orvisited[x][y]:
             returnFalse
         visited[x][y]=True
         path.append((x,y))
         if(x,y)==end:
             returnTrue
         fordx,dyin[(-1,0),(1,0),(0,-1),(0,1)]:
             ifdfs(x + dx,y + dy):
                 returnTrue
         path.pop()
         returnFalse
     ifdfs(start[0],start[1]):
         returnpath
     else:
         returnNone
 # 示例迷宫
 maze=[
     [2,0,1,0,0],
     [1,0,1,0,1],
     [0,0,0,0,1],
     [1,1,0,1,1],
     [0,0,0,0,3]
 ]
 start=(0,0)
 end=(4,4)
 result=solve_maze(maze,start,end)
 print(result)
```
### 输出结果
```
[(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4)]
```
源链接: [https://www.runoob.com/python3/python-maze-solver.html](https://www.runoob.com/python3/python-maze-solver.html)