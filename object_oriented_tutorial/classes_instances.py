# Python Object Oriented Tutorial 1: Classes and Instances
- # Classes logically group our data and functions in a way that is easy to reuse and aslo to build upon
- # Data and Functions are called Attributes and Methods (a function associated with a class)
- # A pass statement lets Python know that you want to leave a class or function empty for now
- # A class is a blueprint for creating instances
- # Instance variables contain data that is unique to that instance

class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)


print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
print(emp_2.fullname())

emp_1.fullname()
print(Employee.fullname(emp_1))