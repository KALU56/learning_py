#Practice Example: Student Management System
# Write a class Student with the following:

# An instance method add_marks(self, subject, marks) to add marks for a subject.
# A class method set_school(cls, school_name) to change the school name.
# A static method is_passing(marks) to check if marks are above 50.

class Student:
    school_name="Central School"
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def add_marks(self, subject, marks):
        self.marks[subject] = marks
    @classmethod
    def set_school(cls, school_name):
        cls.school_name = school_name
    @staticmethod
    def is_passing(marks):
        return marks > 50
  
student = Student("John", 20, {"Math": 95, "Science": 88, "History": 92})
student.add_marks("Math", 100)
print(student.marks)
Student.set_school("Global School")
print(Student.school_name)
print(Student.is_passing(95))
class Person:
    def __init__(self, firstname='John', lastname='Doe', age=30, country='USA'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country

    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old from {self.country}.'

# Using default values
p1 = Person()
print(p1.person_info())  # Output: John Doe is 30 years old from USA.

# Overriding default values
p2 = Person('Alice', 'Smith', 25, 'Canada')
print(p2.person_info())  # Output: Alice Smith is 25 years old from Canada.
##Q1 Create a Book class that stores the title, author, and publication year. Add a method to display the book's details.
class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def display_details(self):
        return f'{self.title} by {self.author} published in {self.publication_year}.'
book = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
print(book.display_details())  # Output: The Great Gatsby by F. Scott Fitzgerald published in 1925.
#Q2 Create an Animal class with an instance method describe to return the animal's name and species, a class method display_class_info , and a static method is_domestic to check if a species is domestic or wild.
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def describe(self):
        return f'{self.name} is a {self.species}.'

    @classmethod
    def display_class_info(cls):
        return f'This class represents {cls.__name__} animals.'

    @staticmethod
    def is_domestic(species):
        return species == "Domestic"    
animal = Animal("Dog", "Domestic")
print(animal.describe())  # Output: Dog is a Domestic.
print(Animal.display_class_info())  # Output: This class represents Animal animals.
print(Animal.is_domestic("Dog"))  # Output: True

#Q3 Design a Company class with attributes for name, industry, and founding year. Write a method to display the company's details and another method to calculate its age based on the current year.

class Company:
    def __init__(self, name, industry, founding_year,datetime):
        self.name = name
        self.industry = industry
        self.founding_year = founding_year
        self.datetime = datetime

    def display_details(self):
        return f'{self.name} is a {self.industry} company founded in {self.founding_year}.'

    def calculate_age(self):
        return self.datetime - self.founding_year
company = Company("Google", "Technology", 1998,2002)
print(company.display_details())  # Output: Google is a Technology company founded in 1998.
print(company.calculate_age())  # Output: 27    
#Q4 Design a Product class with the attributes name, price, and stock quantity. Include a method to calculate the total value of the stock.
class Product:
    def __init__(self, name, price, stock_quantity):
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity

    def calculate_total_value(self):
        return self.price * self.stock_quantity
product = Product("Laptop", 1000, 10)
print(product.calculate_total_value())  # Output: 10000
#Q5 Create a Rectangle class with attributes for width and height. Add a method to calculate the area of the rectangle.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height
rectangle = Rectangle(10, 5)
print(rectangle.calculate_area())  # Output: 50
#Q6 Design a Circle class with an instance method to calculate the area of the circle.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius
circle = Circle(5)
print(circle.calculate_area())  # Output: 78.5  
#Q7 Define a Car class with attributes such as brand, model, and year. Include a method that prints the car's full description.
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def print_description(self):
        return f'{self.brand} {self.model} {self.year}.'
car = Car("Toyota", "Corolla", 2020)
print(car.print_description())  # Output: Toyota Corolla 2020.
#Q8 Create a Student class with the following attributes: name, age, and a list of grades. Implement a method that calculates the average grade.
class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def calculate_average_grade(self):
        return sum(self.grades) / len(self.grades)
student = Student("John", 20, [95, 88, 92])
print(student.calculate_average_grade())  # Output: 91.666
#Q9 Define a BankAccount class with attributes for account number, balance, and owner name. Implement methods to deposit and withdraw funds.
class BankAccount:
    def __init__(self, account_number, balance, owner_name):
        self.account_number = account_number
        self.balance = balance
        self.owner_name = owner_name

    def deposit(self, amount):
        self.balance += amount
        return f'Deposited {amount} into account {self.account_number}.'
    def withdraw(self, amount):
        self.balance -= amount
        return f'Withdrawn {amount} from account {self.account_number}.'
    def account_amount(self):
        return f'The account balance is {self.balance}.'
bank_account = BankAccount("1234567890", 1000, "John Doe")
print(bank_account.deposit(500))  # Output: Deposited 500 into account 1234567890.
print(bank_account.withdraw(200))  # Output: Withdrawn 200 from account 1234567890.
print(bank_account.account_amount())  # Output: The account balance is 1000.
#Q10 Implement a Library class that holds a list of books, each represented by a dictionary containing the title, author, and year. Write a method to display all books
class Library:
    def __init__(self, books):
        self.books = books

    def display_books(self):
        return f'The library has the following books: {self.books}.'
library = Library([{"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925}, {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960}])
print(library.display_books())  # Output: The library has the following books: [{'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'year': 1925}, {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'year': 1960}].    
#Q11Create a House class with attributes like address, number of rooms, and square footage. Implement a method that calculates the price based on square footage.
class House:
    def __init__(self, address, number_of_rooms, square_footage):
        self.address = address
        self.number_of_rooms = number_of_rooms
        self.square_footage = square_footage

    def calculate_price(self):
        return self.square_footage * 100
house = House("123 Main St", 3, 1500)
print(house.calculate_price())  # Output: 150000    
#Q12 Define a Temperature class with attributes for degrees Celsius and Fahrenheit. Implement methods to convert between the two scales.
class Temperature:
    def __init__(self, degrees_celsius, degrees_fahrenheit):
        self.degrees_celsius = degrees_celsius
        self.degrees_fahrenheit = degrees_fahrenheit

    def convert_to_fahrenheit(self):
        return self.degrees_celsius * 1.8 + 32
    def convert_to_celsius(self):
        return (self.degrees_fahrenheit - 32) / 1.8
ce=int(input("Enter the temperature in celsius: "))
fah=int(input("Enter the temperature in fahrenheit: "))
temperature = Temperature(ce,fah)
print(temperature.convert_to_fahrenheit())  # Output: 68.0    
print(temperature.convert_to_celsius())  # Output: 20.0    
#Q13 Create a ShoppingCart class with attributes for items and their prices. Implement methods to add items, remove items, and calculate the total price.
class ShoppingCart:
    def __init__(self, items, prices):
        self.items = items
        self.prices = prices

    def add_item(self, item, price):
        self.items.append(item)
        self.prices.append(price)   
    def remove_item(self, item):
        self.items.remove(item)
        self.prices.remove(item)
    def calculate_total_price(self):
        return sum(self.prices)
shopping_cart = ShoppingCart(["Item1", "Item2", "Item3"], [10, 20, 30])
print(shopping_cart.calculate_total_price())  # Output: 60    
#Q14 Build an Employee class that stores an employee’s name, position, and salary. Write a method to calculate the annual salary.
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def calculate_annual_salary(self):
        return self.salary * 12
employee = Employee("John Doe", "Manager", 5000)
print(employee.calculate_annual_salary())  # Output: 60000    

