# Python 判断列表是否为升序

## 题目描述
Python3 实例
我们可以通过编写一个函数来判断一个列表是否是升序排列的。这个函数会遍历列表中的元素，检查每个元素是否小于或等于下一个元素。如果所有元素都满足这个条件，那么列表就是升序的。

## 实例
### 代码
```python
defis_ascending(lst):
     foriinrange(len(lst)-1):
         iflst[i]>lst[i +1]:
             returnFalse
     returnTrue
 # 测试用例
 print(is_ascending([1,2,3,4,5]))# True
 print(is_ascending([1,3,2,4,5]))# False
 print(is_ascending([5,4,3,2,1]))# False
```
### 输出结果
```
True
False
False
```
源链接: [https://www.runoob.com/python3/python-ascending-list.html](https://www.runoob.com/python3/python-ascending-list.html)