#!/usr/bin/env python3
class Student(object):
    """
    Returns a ```Student``` object with the given name, branch and year.
 
    """
    def __init__(self, name, branch, year,college):
            self.name = name
            self.branch = branch
            self.year = year
            self.college = college
            print("A student object is created.")
 
    def print_details(self):
        """
        Prints the details of the student.
        """
        print("Name:", self.name)
        print("Branch:", self.branch)
        print("Year:", self.year)
        print("College:", self.college)
 
student1 = Student('Sayan', 'CSE', '2009', 'Techno')
student1.print_details()
student2 = Student('RTNPRO', 'CSE', '2007', 'ABC')
student2.print_details()
