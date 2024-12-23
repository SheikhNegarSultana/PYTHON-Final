# Q1: Write a Python program to define a class Person with attributes name and age and a method greet() that prints a greeting message.

class Person():
    def __init__( self , name , age):
        self.name = name
        self.age = age
    def greeting(self):
        return f" Hello I am {self.name} and I am {self.age} years old "
    def greetings(self):
        return f" Hello I am {self.name} "
    
p1 = Person( "Mina" , 12)
p2 = Person( "Raju" , 10)

print(p1.greeting())
print(p2.greetings())


#Write a Python program to define a class Rectangle with attributes length and width, and methods area() and perimeter().

class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)

r1 = Rectangle(8,9)
print(f"Area : {r1.area()}" )
print(f"perimeter : {r1.perimeter()}")