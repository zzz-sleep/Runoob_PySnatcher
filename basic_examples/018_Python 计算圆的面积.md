# Python 计算圆的面积

## 题目描述
Python3 实例
圆的面积公式为 ：
公式中 r 为圆的半径。

## 实例 1
### 代码
```python
# 定义一个方法来计算圆的面积
 deffindArea(r):
     PI=3.142
     returnPI *(r*r)
 # 调用方法
 print("圆的面积为 %.6f"% findArea(5))
```
### 输出结果
```
圆的面积为 78.550000
```
## 实例
### 代码
```python
importmath
 defcalculate_circle_area(radius):
     returnmath.pi* radius **2
 # 示例
 radius=5
 area=calculate_circle_area(radius)
 print(f"半径为 {radius} 的圆的面积是 {area}")
```
### 输出结果
```
半径为 5 的圆的面积是 78.53981633974483
```
源链接: [https://www.runoob.com/python3/python3-area-of-a-circle.html](https://www.runoob.com/python3/python3-area-of-a-circle.html)