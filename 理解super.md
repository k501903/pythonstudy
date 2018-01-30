[TOC]

## super的作用
在类的继承中，如果子类重定义了继承树上（上一级）的某个方法，在子类中就会覆盖(上一级)的同名方法。有时候，希望子类的方法能够在(上一级)方法功能的基础上实现，这就需要在子类的该方法中使用super()函数调用(上一级)的同名方法。（类似于DELPHI的inherit）
```Python
class Animal(object):
    def __init__(self, name):
        self.name = name
    def greet(self):
        print('Hello, I am', self.name)

class Dog(Animal):
    def greet(self):
        super(Dog, self).greet()
        print('WangWang...')

dog = Dog('Dog')
dog.greet()
>>> Hello, I am Dog
>>> WangWang...
```
`super()`函数常用于在子类中调用父类的初始化`__init__`方法

## super深入
由于Python支持多重继承，在一个类的继承链上，会出现一些独特的现象：没有直接继承关系的两个类，出现在继承链上。这块比较不好理解，接着往下看。
在开始介绍之前，先介绍一个概念MRO(Method Resolution Order)方法解析顺序列表，它代表了类继承的顺序。
通过调用一个类（不是实例）的`__MRO__`属性可以查看该类的继承顺序列表。

下面通过一个例子进行这部分概念的解释。
```Python
class Base(object):
    def __init__(self):
        print('Enter Base')
        print('Leave Base')
class A(Base):
    def __init__(self):
        print('Enter A')
        super(A, self).__init()
        print('Leave A')
class B(Base):
    def __init__(self):
        print('Enter B')
        super(B, self).__init()
        print('Leave B')
class C(A, B):
    def __init__(self):
        print('Enter C')
        super(C, self).__init()
        print('Leave C')

c = C()
>>> Enter C
>>> Enter A
>>> Enter B
>>> Enter Base
>>> Leave Base
>>> Leave B
>>> Leave A
>>> Leave C
```
结果并不是我们预期的那样，怎么在类的继承链上B是A的父类了，它们两个可是没有任何的继承关系呢？
通过MRO进一步验证了上例中的输出结果
```Python
print(C.mro())
>>> [__main__.C, __main__.A, __main__.B, __main__.Base, object]
```
下面就是super()函数的实现原理了，看仔细了
```Python
# super()函数有两个参数
# cls 表示类
# inst 表示当前实例
# 输出: 在inst的类的MRO列表中，查找cls类的下一个类
def super(cls, inst):
    # 得到inst实例类的mro
    mro = inst.__class__.mro()
    # 从中查找cls的下一个类
    return mro[mro.index(cls) + 1]
```
