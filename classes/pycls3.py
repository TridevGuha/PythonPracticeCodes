#!/usr/bin/env python3
 
class student(object):
    def __init__(self, name, branch, roll, college):
        self.name = name
        self.branch = branch
        self.roll = roll
        self.college = college
        print("student object is created!")
 
    def print_all(self):
        print("Name: " + self.name)
        print("Branch: " + self.branch)
        print("Roll No.: " + self.roll)
        print("College: " + self.college)
 
std1 = student('Abhishek', 'CSE', '13CS1002','MVN')
std1.print_all()
 
