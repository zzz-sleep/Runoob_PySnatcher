# Python 拓扑排序

## 题目描述
Python3 实例
对一个有向无环图(Directed Acyclic Graph简称DAG)G进行拓扑排序，是将G中所有顶点排成一个线性序列，使得图中任意一对顶点u和v，若边(u,v)∈E(G)，则u在线性序列中出现在v之前。通常，这样的线性序列称为满足拓扑次序(Topological Order)的序列，简称拓扑序列。简单的说，由某个集合上的一个偏序得到该集合上的一个全序，这个操作称之为拓扑排序。
在图论中，由一个有向无环图的顶点组成的序列，当且仅当满足下列条件时，称为该图的一个拓扑排序（英语：Topological sorting）：

## 示例图片
![Python 拓扑排序_graph.png](Python 拓扑排序_graph.png)

## 实例
### 代码
```python
fromcollectionsimportdefaultdictclassGraph:def__init__(self,vertices):self.graph=defaultdict(list)self.V=verticesdefaddEdge(self,u,v):self.graph[u].append(v)deftopologicalSortUtil(self,v,visited,stack):visited[v]=Trueforiinself.graph[v]:ifvisited[i]==False:self.topologicalSortUtil(i,visited,stack)stack.insert(0,v)deftopologicalSort(self):visited=[False]*self.Vstack=[]foriinrange(self.V):ifvisited[i]==False:self.topologicalSortUtil(i,visited,stack)print(stack)g=Graph(6)g.addEdge(5,2);g.addEdge(5,0);g.addEdge(4,0);g.addEdge(4,1);g.addEdge(2,3);g.addEdge(3,1);print("拓扑排序结果：")g.topologicalSort()
```
### 输出结果
```

拓扑排序结果：
[5, 4, 2, 3, 1, 0]

```
源链接: [https://www.runoob.com/python3/python-topological-sorting.html](https://www.runoob.com/python3/python-topological-sorting.html)