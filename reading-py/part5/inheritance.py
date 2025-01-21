#Q1,Create a Student class that inherits from the Person class. The Person class should have attributes name and age, and a method introduce() that introduces the person by stating their name and age. The Student class should inherit from Person and add an additional attribute course to represent the course the student is studying. Modify the introduce() method in the Student class to include the student's course, so the introduction should include: "Hi, I'm [name], I'm [age] years old, and I study [course]." Ensure that the Student class uses the super() function to call the constructor of the Person class to initialize the name and age attributes.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, I'm {self.name}, I'm {self.age} years old."


class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def introduce(self):
        # Build upon the Person's introduction
        base_intro = super().introduce()
        return f"{base_intro} I study {self.course}."


# Example usage
student1 = Student("John", 25, "Computer Science")
print(student1.introduce())
#Q2. Create a Car class that has the following attributes: make, model, and year. The Car class should have a method display() that prints the make, model, and year of the car. Create a ElectricCar class that inherits from the Car class and adds an
# additional attribute battery_size. The ElectricCar class should also have a method display() that prints the make, model, year, and battery size of the electric car. Ensure that the ElectricCar class uses the super() function to call the constructor of the Car class to initialize the make, model, and year attributes.
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}"


class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def display(self):
        # Get base class display information
        f_intro = super().display()
        # Add the battery size information
        return f"{f_intro}, Battery Size: {self.battery_size}"


# Example usage
electric_car = ElectricCar("Tesla", "Model S", 2023, "100 kWh")
print(electric_car.display())
#Q3. Create a Shape class that has a method area() that returns 0. Create a Rectangle class that inherits from the Shape class and adds a method area() that calculates and returns the area of the rectangle. The Rectangle class should have attributes width and height. Create a Square class that inherits from the Rectangle class and adds a method area() that calculates and returns the area of the square. The Square class should have an attribute side_length. Ensure that the Rectangle and Square classes use the super() function to call the constructor of the Shape and Rectangle classes, respectively.
class Shape:
    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    def area(self):
        return super().area()
    
# Example usage 
rectangle = Rectangle(4, 5)
print(rectangle.area())  # 20
Square = Square(5)
print(Square.area())  # 25
#Q4. Create a BankAccount class that has attributes account_number and balance, and methods deposit() and withdraw() to add or subtract from the balance. Create a CheckingAccount class that inherits from BankAccount and adds an additional attribute limit and a method withdraw() that allows for overdrafts up to the limit. If the withdrawal amount exceeds the balance and the overdraft limit, print "Insufficient funds." Ensure that the CheckingAccount class uses the super() function to call the constructor of the BankAccount class to initialize the account number and balance attributes.
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance, limit):
        super().__init__(account_number, balance)
        self.limit = limit

    def withdraw(self, amount):
        if amount > self.balance + self.limit:
            print("Insufficient funds.")
        else:
            self.balance -= amount
# Example usage
checking_account = CheckingAccount("123456", 1000, 500)
checking_account.deposit(500)
print(checking_account.balance)  # 1500
checking_account.withdraw(2000)  # Insufficient funds.
print(checking_account.balance)  # 1500
checking_account.withdraw(1500)
print(checking_account.balance)  # 0
#Q5. Create a Animal class that has a method speak() that prints "Animal speaks". Create a Dog class that inherits from the Animal class and overrides the speak() method to print "Dog barks". Create a Cat class that inherits from the Animal class and overrides the speak() method to print "Cat meows". Ensure that the Dog and Cat classes use the super() function to call the speak() method of the Animal class.
class Animal:
    def speak(self):
        print("Animal speaks")
class Dog(Animal):
    def speak(self):
        super().speak()
        print("Dog barks")
class Cat(Animal):
    def speak(self):
        super().speak()
        print("Cat meows")
# Example usage
dog = Dog()
dog.speak()  # Animal speaks, Dog barks
cat = Cat()
cat.speak()  # Animal speaks, Cat meows
#Q6. Write a program to demonstrate hierarchical inheritance with a Person class and Student and Teacher subclasses
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display(self):
        super().display()
        print(f"Student ID: {self.student_id}")
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display(self):
        super().display()
        print(f"Subject: {self.subject}")
# Example usage
student = Student("Alice", 20, "1234")
student.display()
teacher = Teacher("Bob", 35, "Math")
teacher.display()
#Q7. Write a program to demonstrate multiple inheritance with classes A, B, and C, where A is the base class and B and C inherit from A. Class D inherits from both B and C.
class A:
    def method_a(self):
        print("Method A")
class B(A):
    def method_b(self):
        print("Method B")
class C(A):
    def method_c(self):
        print("Method C")
class D(B, C):
    def method_d(self):
        print("Method D")
# Example usage
d = D()
d.method_a()  # Method A
d.method_b()  # Method B
d.method_c()  # Method C
d.method_d()  # Method D
#Q8. Write a program to demonstrate hybrid inheritance with classes A, B, C, and D, where A is the base class and B and C inherit from A. Class D inherits from both B and C.
class A:
    def method_a(self):
        print("Method A")
class B(A):
    def method_b(self):
        print("Method B")
class C(A):
    def method_c(self):
        print("Method C")

class D(B, C):
    def method_d(self):
        print("Method D")
# Example usage
d = D()
d.method_a()  # Method A
d.method_b()  # Method B
d.method_c()  # Method C
d.method_d()  # Method D
#Q9.Demonstrate single inheritance using Company and Employee.
class Company:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def display(self):
        print(f"Company: {self.name}, Location: {self.location}")
class Employee(Company):
    def __init__(self, name, location, emp_id):
        super().__init__(name, location)
        self.emp_id = emp_id

    def display(self):
        super().display()
        print(f"Employee ID: {self.emp_id}")
# Example usage
employee = Employee("ABC Inc.", "New York", "12345")
employee.display()
#Q10.Create a Vehicle class with a method fuel_efficiency() and override it in Car and Bike subclasses.
class Vehicle:
    def fuel_efficiency(self):
        pass
class Car(Vehicle):
    def fuel_efficiency(self):
        print("Car fuel efficiency: 20 km/l")
class Bike(Vehicle):
    def fuel_efficiency(self):
        print("Bike fuel efficiency: 40 km/l")
# Example usage
car = Car()

car.fuel_efficiency()  # Car fuel efficiency: 20 km/l



    