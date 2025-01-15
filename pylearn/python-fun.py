# ############
# def sequar(a):
#   return a * a
# print(sequar(2))

# x = lambda a : a * a
# print(x(2))

# def hello():
#   print("Hello World")
# hello()
# hello()
# hello()
# hello()


# def greet(name):
#   print(f"Hello, {name}!")
# greet("Alice")

# def my_f(c3,c2,c1):
#   print("the youngest child is " + c3)
# my_f(c1="al",c2="li",c3="di")

# def my_function(*kids):
#   print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus")
# def my_function(**kid):
#   print("His last name is " + kid["lname"])

# my_function(fname = "Tobias", lname = "Refsnes")
# def my_function(country = "Norway"):
#   print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")

# def my_function(food):
#   for x in food:
#     print(x)

# fruits = ["apple", "banana", "cherry"]

# my_function(fruits)
# def my_function(kalkidan):
#     for x in kalkidan:
#         print(f"{x}: {len(x)} characters")

# my_function(["apple", "banana", "cherry"])

# x = lambda a : a + 10
# print(x(5))
# x = lambda a, b : a * b
# print(x(5, 6))
# x=lambda a,b,c:a+b+c
# print(x(5,6,8))
# def myfunc(n):
#   return lambda a : a ** n

# mydoubler = myfunc(2)

# print(mydoubler(11))
# class MyClass:
#   x = 5
# p1 = MyClass()
# print(p1.x)
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# # print(p1.age)
# from mymodule import person1

# print (person1["age"])
# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   pass

# x = Student("Mike", "Olsen")
# x.printname()
from mymodule import person1

print (person1["age"])
import datetime

x = datetime.datetime.now()
print(x)
import datetime

x = datetime.datetime(2020, 5, 17)

print(x.year)
print(x.strftime("%A"))