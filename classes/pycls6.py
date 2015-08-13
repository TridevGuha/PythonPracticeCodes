
#!/usr/bin/env python3
class Shape(object):
    def __init__(self, weight):
       self.weight = weight
 
class Triangle(Shape):
    def __init__(self, base, height):
       self.base = base
       self.height = height
 
class Square(Shape):
    def __init__(self, side):
       self.side = side
 
class Circle(Shape):
    def __init__(self, radius):
       self.radius = radius
 
football = Circle(6)
basketball = Circle(6)
 
rubikcube = Square(5)
dice = Square(1)
 
pyramid = Triangle(100, 250)
prism = Triangle(2, 5)
 

