#!/usr/bin/env python3
class Shape(object):
    sideln = int(input("Enter the side length="))
    radius = int(input("Enter the radius of circle type objects="))
 
class Triangle(Shape):
    pass
 
class Square(Shape):
    pass
 
class Circle(Shape):
    pass
 
 
 
football = Circle()
basketball = Circle()
 
rubik = Square()
dice = Square()
 
pyramid = Triangle()
prism = Triangle()
 
print(football.radius)
print(dice.sideln)
print(rubik.sideln)
print(basketball.radius)
print(pyramid.sideln)
print(prism.sideln)
