# Python 在一个列表中找到第二大的元素

## 题目描述
Python3 实例
描述内容：在 Python 中，我们可以通过多种方法找到一个列表中的第二大的元素。下面是一个简单的方法，通过排序列表并选择倒数第二个元素来实现。
代码部分：

## 实例
### 代码
```python
deffind_second_largest(lst):
     # 首先去除列表中的重复元素
     unique_lst=list(set(lst))
     # 对列表进行排序
     unique_lst.sort()
     # 返回倒数第二个元素
     returnunique_lst[-2]
 # 示例列表
 numbers=[10,20,4,45,99,99]
 # 调用函数
 second_largest=find_second_largest(numbers)
 print("第二大的元素是:",second_largest)
```
### 输出结果
```
第二大的元素是: 45
```
源链接: [https://www.runoob.com/python3/python-second-largest.html](https://www.runoob.com/python3/python-second-largest.html)