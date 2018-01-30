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
