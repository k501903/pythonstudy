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

class Base(object):
    def __init__(self):
        print('Enter Base')
        print('Leave Base')
class A(Base):
    def __init__(self):
        print('Enter A')
        super().__init__()
        print('Leave A')
class B(Base):
    def __init__(self):
        print('Enter B')
        super().__init__()
        print('Leave B')
class C(A, B):
    def __init__(self):
        print('Enter C')
        super().__init__()
        print('Leave C')

c = C()

class Root:
    def draw(self):
        # 将委托链(delegation)中断
        # 利用防御性编程(defensive programming)的assert确保中断调用链条
        assert not hasattr(super(), 'draw')
class Shape(Root):
    def __init__(self, shapename, **kw):
        self.shapename = shapename
        super().__init__(**kw)
    def draw(self):
        print('Drawing. Setting shape to:', self.shapename)
        super().draw()
class ColoredShape(Shape):
    def __init__(self, color, **kw):
        self.color = color
        super().__init__(**kw)
    def draw(self):
        print('Drawing. Setting color to', self.color)
        super().draw()

cs = ColoredShape(color='blue', shapename='square')
cs.draw()

class Moveable:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self):
        print('Drawing at position:', self.x, self.y)
    
# 定义一个Adapter类，从Root继承
class MoveableAdapter(Root):
    # 定义**kw的签名
    def __init__(self, x, y, **kw):
        # 创建第三方类的对象实例
        self.moveable = Moveable(x, y)
        # 使用super()
        super().__init__(**kw)
    def draw(self):
        self.moveable.draw()
        super().draw()

class MoveableColoredShape(MoveableAdapter, ColoredShape):
    pass

mcs = MoveableColoredShape(color='red', shapename='triangle',
        x=10, y=20)
mcs.draw()
print(mcs.__class__.__mro__)