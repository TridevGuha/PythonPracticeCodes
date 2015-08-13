#!/usr/bin/env python3
'''In this example , you have to take number of students as input , then ask marks for three subjects as ‘Physics’, ‘Maths’, ‘History’, if the total marks for any student is less 120 then print he failed, or else say passed.'''
n = int(input("Enter the number of students:"))
data = {} # here we will store the data
languages = ('Physics', 'Maths', 'History') #all languages
for i in range(0, n): #for the n number of students
    name = input('Enter the name of the student %d: ' % (i + 1)) #Get the name of the student
    marks = []
    for x in languages:
        marks.append(int(input('Enter marks of %s: ' % x))) #Get the marks for  languages
    data[name] = marks
for x, y in data.iteritems():
    total =  sum(y)
    print("%s 's  total marks %d" % (x, total))
    if total < 120:
        print("%s failed :(" % x)
    else:
        print("%s passed :)" % x)