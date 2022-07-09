import math


"""
 QUIZ - OOP
"""

# --------------------------------------------------------------------------------------#

# Q 1:
"""
Define a class named Student.
Student has two attributes:
* name (str)
* number (str)

Create two student objects out of this class.
The objects will be:
1- name: James Bond, number: 007
2- name: Klark Kent, number: 333

Print their names.

Hints:
* __init__

Exptected Output:
James Bond
Klark Kent
"""


# S 1:
class Student:
    def __init__(self,name, number):
        self.name = name
        self.number = number
        self.courses = []


    def enroll(self):
        pass
    def get_courses(self):
        return(self.courses)



student1 = Student("James Bond", "007" )
student1.courses = ["Python", "Machine Learning"]
student2 = Student("Klark Kent", "333")

print(student1.name)
print(student2.name)






# --------------------------------------------------------------------------------------#

# Q 2:
"""
The Student class you defined in Q1, has a new attribute.
This attribute is 'courses' and it will keep the list of courses, that the student takes.
Its type is list and it will initialize as an empty list.

There will be a method named 'enroll' to enroll the course.
The student will enroll the course, if it has not enrolled already.

Moreover, there will be a method named 'get_courses' which will return the course list.

Redefine the Student class based on these information.

Student data:
name: John Doe, number: 1111
courses: 
    * Python Hands-On
    * Machine Learning

Expected Output:
student.get_courses()  ->  ['Python Hands-On', 'Machine Learning']
"""


# S 2:

print(student1.get_courses())


# --------------------------------------------------------------------------------------#

# Q 3:
"""
Define a class named 'Point'.
It will represent a point in x-y coordinate space.
And the docstring will be:
'it represents a point in (x,y) coordinates.'

Attributes: 
    * x (int) 
    * y (int)

Define __init__() for Point.
And it has a method named 'distance' which calculates the distance between two Points.
The first point is the current point (self) and the second will be the parameter.

Hints:
* to calculate distance (d):
    * get the difference between x values (x_diff)
    * get the difference between y values (y_diff)
    * d = math.sqrt(x_diff**2 + y_diff**2)
    
Expected Output:
p_1 -> (1, 7)
p_2 -> (4, 3)
dist = p_1.distance(p_2)
print(dist) ->  5.0
"""

#S 3:
import math

class Point:
    """It represents a point in x,y coordinates """
    def __init__(self, x, y):
        self.x = x
        self.y =y
    def distance(self, a,b):
        self.a = a
        self.b = b
        x_diff = self.x - self.a
        y_diff = self.y - self.b
        dist = math.sqrt(x_diff**2 + y_diff**2)
        return dist


point = Point(1,7)
t = point.distance(4,3)
print(t)



# --------------------------------------------------------------------------------------#

# Q 4:
"""
Define a class named Rectangle.
It represents a rectangle on the X-Y coordinate axis.
And this is its docstring:
"This class represents a rectangle on (x,y) coordiante axis."

Rectangle has 4 attributes:
    * corner_1 (Point)
    * corner-2 (Point)
    * corner_3 (Point)
    * corner_4 (Point)

The type of these 4 corners are the Point class we defined in Q3.

Corner 1 and 2 are on the same line (side).
Corner 3 and 4 are on the same line (side).

This is how the corners look like:

1..............2
.              .
.              .
.              .
3..............4

Define the __init__() for Rectangle class.

It has methods to calculate its width and length.
    * width = distance between corner 1 and 2 -> calculate_width()
    * lenght = distance between corner 1 and 3 -> calculate_length()
    
Rectangle uses Point class to calculate these distances.

Finally, Rectangle has a method which returns its area.
The name of this method is 'area'.

Expected Output:
p_1 = Point(5, 8)
p_2 = Point(9, 8)
p_3 = Point(5, 2)
p_4 = Point(9, 2)

width = rect.width
length = rect.length
area = rect.area()

width: 4.0
length: 6.0
area: 24.0
"""


# S 4:
class Rectangle:
    """This class represents a rectangle on (x,y) coordiante axis."""
    def __init__(self):
        self.corner_1 = Point(5,8)
        self.corner_2 = Point(9,8)
        self.corner_3 = Point(5,2)
        self.corner_4 = Point(9,2)

    def width(self):
        w =self.corner_1.distance(self.corner_2.x, self.corner_2.y)
        return w
    def length(self):
        l= self.corner_1.distance(self.corner_3.x, self.corner_3.y)
        return l

    def area(self):
        return self.length() * self.width()


rectangle = Rectangle()
print(rectangle.width())
print(rectangle.length())
print(rectangle.area())



# --------------------------------------------------------------------------------------#

# Q 5:

"""
Define a class named BankAccount.
It has an attribute: balance (int)
And it has two methods:
    * withdraw -> removes money from balance
    * deposit -> adds money to balance

Both methods will update the balance and return the final balance.
The initial balance is 0. (__init__())

Finally there is method named 'display_balance' and it will print the current balance as:
'Balance: xxxxxx'

Expected Output:
account = BankAccount()
account.display_balance()
account.deposit(500)
account.display_balance()
account.withdraw(200)
account.display_balance()

Balance: 0
Balance: 500
Balance: 300
"""

class BankAccount:
    def __init__(self):
        self.balance = 0


    def deposit(self, amount):
        self.balance = amount
        return self.balance


    def withdraw(self, amount):
        self.amount = amount
        balance = self.balance - self.amount
        self.balance = balance

    def display_balance(self):
        return f"Balance : {self.balance}"


account = BankAccount()
print(account.display_balance())
account.deposit(500)
print(account.display_balance())
account.withdraw(200)
print(account.display_balance())