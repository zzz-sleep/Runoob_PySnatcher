# Python 使用抽象类定义接口

## 题目描述
Python3 实例
在 Python 中，抽象类是一种特殊的类，它不能被实例化，只能被继承。抽象类通常用于定义接口，即一组方法的声明，而不提供具体的实现。子类必须实现这些方法才能被实例化。
Python 提供了abc模块来创建抽象类。我们可以使用ABC类和abstractmethod装饰器来定义抽象方法。
下面是一个使用抽象类定义接口的示例：

## 实例
### 代码
```python
fromabcimportABC,abstractmethod
 classAnimal(ABC):
     @abstractmethod
     defmake_sound(self):
         pass
     @abstractmethod
     defmove(self):
         pass
 classDog(Animal):
     defmake_sound(self):
         return"Woof!"
     defmove(self):
         return"Running on four legs"
 classBird(Animal):
     defmake_sound(self):
         return"Chirp!"
     defmove(self):
         return"Flying in the sky"
 # 实例化子类
 dog=Dog()
 bird=Bird()
 print(dog.make_sound())# 输出: Woof!
 print(dog.move())# 输出: Running on four legs
 print(bird.make_sound())# 输出: Chirp!
 print(bird.move())# 输出: Flying in the sky
```
### 输出结果
```
Woof!
Running on four legs
Chirp!
Flying in the sky
```
源链接: [https://www.runoob.com/python3/python-abstract-class.html](https://www.runoob.com/python3/python-abstract-class.html)