#q1 Create a Person class to store a person's name, age, and a list of their favorite colors. Instantiate the class and display the person's name, age, and all the favorite colors.

class Person:
    def __init__(self, name, age, favorite_colors):
        self.name = name
        self.age = age
        self.favorite_colors = favorite_colors

person = Person("John", 30, ["blue", "green", "red"])
print(person.name)
print(person.age)
print(person.favorite_colors)
print(person.name, person.age, person.favorite_colors)

#q2 Define a Library class to store the library's name, location, and a list of available books (titles). Display the library name, location, and all the book titles.

class Library:
    def __init__(self, name, location, books):
        self.name = name
        self.location = location
        self.books = books

library = Library("Central Library", "New York", ["The Great Gatsby", "To Kill a Mockingbird", "1984"])
library2=Library("Central Library", "New York", ["The Great Gatsby", "To Kill a Mockingbird", "1984"])
print(library.name)
print(library.location)
print(library.books)
print(library2.name)
print(library2.location)
print(library2.books)
print(library.name, library.location, library.books)
print(library2.name, library2.location, library2.books)
#q3 Build a Student class that holds a student's name, age, grades (in a dictionary), and enrolled courses (a list). Create an instance of a student and print their name, age, and grades.

class Student:
    def __init__(self, name, age, grades, enrolled_courses):
        self.name = name
        self.age = age
        self.grades = grades
        self.enrolled_courses = enrolled_courses

student = Student("John", 20, {"Math": 95, "Science": 88, "History": 92}, ["Math", "Science", "History"])
print(student.name)
print(student.age)
print(student.grades)
print(student.enrolled_courses)
print(student.name, student.age, student.grades, student.enrolled_courses)
#q4 Implement a Product class to accept name, price, and manufacturing date. Display all the product details.

class Product:
    def __init__(self, name, price, manufacturing_date):
        self.name = name
        self.price = price
        self.manufacturing_date = manufacturing_date
product_name=input("Enter the name of the product: ")
product_price=int(input("Enter the price of the product: "))
product_manufacturing_date=input("Enter the manufacturing date of the product: ")

product = Product(product_name, product_price, product_manufacturing_date)
print(product.name)
print(product.price)
print(product.manufacturing_date)
print(product.name, product.price, product.manufacturing_date)
#q5 Create a Car class to store the car's brand, model, year, and a list of service dates. Instantiate the class with a car’s information and print all details, including the car's brand, model, year, and service dates.

class Car:
    def __init__(self, brand, model, year, service_dates):
        self.brand = brand
        self.model = model
        self.year = year
        self.service_dates = service_dates

car_brand=input("Enter the brand of the car: ")
car_model=input("Enter the model of the car: ")
car_year=input("Enter the year of the car: ")
car_service_dates=input("Enter the service dates of the car: ")

car = Car(car_brand, car_model, car_year, car_service_dates)
print(car.brand)
print(car.model)
print(car.year)
print(car.service_dates)
print(car.brand, car.model, car.year, car.service_dates)
#q6 Implement a School class to store the school's name, the number of students, and a dictionary of student names with their respective grades. Display the school's name, the number of students, and the students with their grades.

class School:
    school_name="Central School"
    def __init__(self, number_of_students, student_names_with_grades):
        self.number_of_students = number_of_students
        self.student_names_with_grades = student_names_with_grades

school = School(100, {"John": "A", "Jane": "B", "Jim": "C"})
print(school.school_name)
print(school.number_of_students)
print(school.student_names_with_grades)
print(school.school_name, school.number_of_students, school.student_names_with_grades)