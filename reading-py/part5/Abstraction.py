#Q1.Create an abstract class Vehicle with methods start_engine() and stop_engine(). Then create a Car class that implements these methods.
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass
class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"
    def stop_engine(self):
        return "Car engine stopped"
car = Car()
print(car.start_engine())  # Output: Car engine started
print(car.stop_engine())  # Output: Car engine stopped
#Q2.Create an abstract class Animal with methods make_sound() and move(). Then create a Dog class that implements these methods.
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    @abstractmethod
    def move(self):
        pass  
class Dog(Animal):
    def make_sound(self):
        return "Woof!"
    def move(self):
        return "Dog is running"
dog = Dog()
print(dog.make_sound())  # Output: Woof!
print(dog.move())  # Output: Dog is running
#Q3.Create an abstract class Shape with methods area() and perimeter(). Then create a Circle class that implements these methods.
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass  
class Circle(Shape):
    def area(self):
        return "Circle area"
    def perimeter(self):
        return "Circle perimeter"
circle = Circle()
print(circle.area())  # Output: Circle area
print(circle.perimeter())  # Output: Circle perimeter
#Q4.Create an abstract class Employee with methods work() and salary(). Then create a Manager and Developer subclass that implements these methods.
class Employee(ABC):
    @abstractmethod
    def work(self):
        pass
    @abstractmethod
    def salary(self):
        pass  
class Manager(Employee):
    def work(self):
        return "Manager works"
    def salary(self):
        return "Manager salary"
manager = Manager()
print(manager.work())  # Output: Manager works
print(manager.salary())  # Output: Manager salary
class Developer(Employee):
    def work(self):
        return "Developer works"
    def salary(self):
        return "Developer salary"
developer = Developer()
print(developer.work())  # Output: Developer works
print(developer.salary())  # Output: Developer salary 
#Q5.Create an abstract class Person with methods eat() and sleep(). Then create a Student and Teacher subclass that implements these methods.
class Person(ABC):
    @abstractmethod
    def eat(self):
        pass
    @abstractmethod
    def sleep(self):
        pass
class Student(Person):
    def eat(self):
        return "Student eats"
    def sleep(self):
        return "Student sleeps"
student = Student()
print(student.eat())  # Output: Student eats
print(student.sleep())  # Output: Student sleeps  
class Teacher(Person):
    def eat(self):
        return "Teacher eats"
    def sleep(self):
        return "Teacher sleeps"
teacher = Teacher()
print(teacher.eat())  # Output: Teacher eats
print(teacher.sleep())  # Output: Teacher sleeps
#Q6.Create an abstract class Vehicle with methods start() and stop(). Then create a Car and Bike subclass that implements these methods.
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass  
class Car(Vehicle):
    def start(self):
        return "Car started"
    def stop(self):
        return "Car stopped"
car = Car()
print(car.start())  # Output: Car started
print(car.stop())  # Output: Car stopped
class Bike(Vehicle):
    def start(self):
        return "Bike started"
    def stop(self):
        return "Bike stopped"
bike = Bike()
print(bike.start())  # Output: Bike started
print(bike.stop())  # Output: Bike stopped      
#Q7.Create an abstract class Book with methods read() and write(). Then create a Fiction and NonFiction subclass that implements these methods.
class Book(ABC):
    @abstractmethod
    def read(self):
        pass
    @abstractmethod
    def write(self):
        pass
class Fiction(Book):
    def read(self):
        return "Fiction book read"
    def write(self):
        return "Fiction book written"
fiction = Fiction()
print(fiction.read())  # Output: Fiction book read
print(fiction.write())  # Output: Fiction book written
class NonFiction(Book):
    def read(self):
        return "NonFiction book read"
    def write(self):
        return "NonFiction book written"
nonfiction = NonFiction()
print(nonfiction.read())  # Output: NonFiction book read
print(nonfiction.write())  # Output: NonFiction book written
#Q8.Create an abstract class BankAccount with methods deposit() and withdraw(). Implement these in a SavingsAccount class.
class BankAccount(ABC):
    @abstractmethod
    def deposit(self):
        pass
    @abstractmethod
    def withdraw(self):
        pass
class SavingsAccount(BankAccount):
    def deposit(self):
        return "Savings account deposited"
    def withdraw(self):
        return "Savings account withdrawn"
savings = SavingsAccount()
print(savings.deposit())  # Output: Savings account deposited
print(savings.withdraw())  # Output: Savings account withdrawn  

