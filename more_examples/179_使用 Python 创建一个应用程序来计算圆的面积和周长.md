# 使用 Python 创建一个应用程序来计算圆的面积和周长

## 题目描述
Python3 实例
我们将使用 Python 编写一个简单的应用程序来计算圆的面积和周长。用户将输入圆的半径，程序将输出圆的面积和周长。

## 实例
### 代码
```python
importmath
 defcalculate_area(radius):
     returnmath.pi* radius **2
 defcalculate_circumference(radius):
     return2*math.pi* radius
 defmain():
     radius=float(input("请输入圆的半径: "))
     area=calculate_area(radius)
     circumference=calculate_circumference(radius)
     print(f"圆的面积为: {area:.2f}")
     print(f"圆的周长为: {circumference:.2f}")
 if__name__=="__main__":
     main()
```
### 输出结果
```
请输入圆的半径: 5
圆的面积为: 78.54
圆的周长为: 31.42
```
源链接: [https://www.runoob.com/python3/python-circle-area-circumference.html](https://www.runoob.com/python3/python-circle-area-circumference.html)