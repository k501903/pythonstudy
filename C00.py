#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'练习用的模块'

__author__ = 'Jacklee'

# 导入模块
import collections, types, sys

class Root:  
    def draw(self):  
        # the delegation chain stops here  
        assert not hasattr(super(), 'draw')  
  
class Shape(Root):  
    def __init__(self, shapename, **kwds):  
        self.shapename = shapename  
        super().__init__(**kwds)  
    def draw(self):  
        print('Drawing.  Setting shape to:', self.shapename)  
        super().draw()  
  
class ColoredShape(Shape):  
    def __init__(self, color, **kwds):  
        self.color = color  
        super().__init__(**kwds)  
    def draw(self):  
        print('Drawing.  Setting color to:', self.color)  
        super().draw()  
  
cs = ColoredShape(color='blue', shapename='square')  
cs.draw()  


import pprint
import logging
import collections

class LoggingDict(dict):

    def __setitem__(self, key, value):
        logging.info('Setting %r to %r' % (key, value))
        print('父类名称:', super(LoggingDict, self).__class__)
        super().__setitem__(key, value)

class LoggingOD(LoggingDict, collections.OrderedDict):
    pass

myod = LoggingOD()
myod['c'] = 1
myod['b'] = 2
myod['k'] = 3
print(myod)
print(LoggingOD.__mro__)