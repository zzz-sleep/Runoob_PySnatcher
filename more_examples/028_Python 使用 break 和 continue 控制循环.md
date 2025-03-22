# Python 使用 break 和 continue 控制循环

## 题目描述
Python3 实例
在 Python 中，break和continue是两个用于控制循环流程的关键字。break用于立即终止整个循环，而continue用于跳过当前迭代，直接进入下一次迭代。
下面是一个示例代码，展示了如何使用break和continue来控制循环。

## 实例
### 代码
```python
# 示例代码
 foriinrange(1,11):
     ifi==5:
         continue# 跳过当前迭代
     ifi==8:
         break# 终止循环
     print(i)
```
### 输出结果
```
1
2
3
4
6
7
```
源链接: [https://www.runoob.com/python3/python-break-continue.html](https://www.runoob.com/python3/python-break-continue.html)