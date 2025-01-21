#Q1. Write a program with a Animal class and two subclasses Dog and Cat, each with a speak() method. Call the speak() method on each subclass object.
class Animal:
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"
dog = Dog()
cat = Cat()
print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!
#Q2. Create a class Vehicle with a method start() and override it in Car and Bike subclasses. Call the start() method on each subclass object.
class Vehicle:
    def start(self):
        pass
class Car(Vehicle):
    def start(self):
        return "Car started"
class Bike(Vehicle):
    def start(self):
        return "Bike started"
car = Car()
bike = Bike()
print(car.start())  # Output: Car started
print(bike.start())  # Output: Bike started
#Q3. Create a class Employee with a method work() and override it in Manager and Developer subclasses. Call the work() method on each subclass object.
class Employee:
    def work(self):
        pass
class Manager(Employee):
    def work(self):
        return "Manager works"
class Developer(Employee):
    def work(self):
        return "Developer works"
manager = Manager()
developer = Developer()
print(manager.work())  # Output: Manager works
print(developer.work())  # Output: Developer works
#Q4. Create a class Shape with a method area() and override it in Circle and Rectangle subclasses. Call the area() method on each subclass object.
class Shape:
    def area(self):
        pass
class Circle(Shape):
    def area(self):
        return "Circle area"  
class Rectangle(Shape):
    def area(self):
        return "Rectangle area"
circle = Circle()
rectangle = Rectangle()
print(circle.area())  # Output: Circle area
print(rectangle.area())  # Output: Rectangle area
#Q5. Create a class BankAccount with a method deposit() and override it in SavingsAccount and CheckingAccount subclasses. Call the deposit() method on each subclass object.
class BankAccount:
    def deposit(self):
        pass
class SavingsAccount(BankAccount):
    def deposit(self):
        return "Savings account deposit"
class CheckingAccount(BankAccount):
    def deposit(self):
        return "Checking account deposit" 
savings_account = SavingsAccount()
checking_account = CheckingAccount()
print(savings_account.deposit())  # Output: Savings account deposit
print(checking_account.deposit())  # Output: Checking account deposit
#Q6. Create a class Person with a method greet() and override it in Student and Teacher subclasses. Call the greet() method on each subclass object.
class Person:
    def greet(self):
        pass
class Student(Person):
    def greet(self):
        return "Hello, I am a student"
class Teacher(Person):
    def greet(self):
        return "Hello, I am a teacher"  
student = Student()
teacher = Teacher()
print(student.greet())  # Output: Hello, I am a student
print(teacher.greet())  # Output: Hello, I am a teacher
#Q7.Create a Payment class and subclasses CreditCardPayment and PayPalPayment, each with a process() method. Demonstrate how polymorphism works with these classes.
class Payment:
    def process(self):
        pass
class CreditCardPayment(Payment):
    def process(self):
        return "Credit card payment processed"
class PayPalPayment(Payment):
    def process(self):
        return "PayPal payment processed" 
credit_card_payment = CreditCardPayment()
paypal_payment = PayPalPayment()
print(credit_card_payment.process())  # Output: Credit card payment processed
print(paypal_payment.process())  # Output: PayPal payment processed
#Q8.Write a program with a Device class and subclasses Laptop and Smartphone. Each subclass should have a start() method. Call the start() method on different objects using a loop.
class Device:
      def start(self):
        pass
class Laptop(Device):
    def start(self):
        return "Laptop started"
class Smartphone(Device):
    def start(self):
        return "Smartphone started"
devices = [Laptop(), Smartphone()]
for device in devices:
    print(device.start())  # Output: Laptop started, Smartphone started
#Q9.Create a Student class and two subclasses PrimaryStudent and HighSchoolStudent. Each subclass should have an introduce() method. Use polymorphism to introduce different types of students.
class Student:
    def intro(self):
        pass

class PrimaryStudent(Student):
    def intro(self):
        return "I am a primary student"

class HighSchoolStudent(Student):
    def intro(self): 
        return "I am a high school student"

# Creating instances of the subclasses
primary = PrimaryStudent()
high_school = HighSchoolStudent()

# Calling their respective intro methods
print(primary.intro())   
print(high_school.intro())
#Q10.Create a class Book with a method read() and override it in Ebook and AudioBook subclasses. Call the read() method on each subclass object.
class Book:
    def read(self):
        pass
class Ebook(Book):
    def read(self):
        return "Reading an ebook"
class AudioBook(Book):
    def read(self):
        return "Listening to an audiobook"  
book = Book()
ebook = Ebook()
audiobook = AudioBook()
print(book.read())  # Output: Reading a book
print(ebook.read())  # Output: Reading an ebook
print(audiobook.read())  # Output: Listening to an audiobook
