**Object-Oriented Programming (OOP) Final Exam Notes**

### **1. Introduction to OOP**
Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects," which are instances of classes. It helps in organizing code efficiently by bundling data and functions that operate on the data together.

### **2. Key Concepts of OOP**

#### **a. Class**
A class is a blueprint for creating objects. It defines the attributes (variables) and behaviors (methods) of objects.

```python
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.brand} {self.model}"
```

#### **b. Object**
An object is an instance of a class. It has its own state and behaviors as defined by the class.

```python
my_car = Car("Toyota", "Corolla", 2022)
print(my_car.display_info())  # Output: 2022 Toyota Corolla
```

#### **c. Variables (Attributes/Properties)**
Variables in a class store data related to an object. They can be:
- **Instance Variables:** Unique to each object.
- **Class Variables:** Shared among all instances of the class.

```python
class Example:
    class_variable = "Shared Data"
    
    def __init__(self, instance_value):
        self.instance_variable = instance_value
```

#### **d. Methods**
Methods are functions defined within a class that operate on objects.
- **Instance Methods:** Work with instance attributes.
- **Class Methods:** Work with class variables.
- **Static Methods:** Independent of class and instance.

```python
class Student:
    school_name = "Greenwood High"  # Class variable
    
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age
    
    def greet(self):  # Instance method
        return f"Hello, my name is {self.name}."
    
    @classmethod
    def school_info(cls):  # Class method
        return f"This student studies at {cls.school_name}."
```

#### **e. Best Practices in OOP**
- Use meaningful class and method names.
- Follow the **Single Responsibility Principle (SRP)** – each class should have one responsibility.
- Encapsulate data using private variables (`self.__variable`).
- Use inheritance wisely to avoid unnecessary complexity.
- Apply polymorphism to make code more flexible and reusable.

---
### **3. Benefits of OOP**
✅ **Code Reusability:** Reuse existing code through **inheritance** and **polymorphism**.
✅ **Easier Debugging & Maintenance:** Well-structured code is easier to read and debug.
✅ **Improved Modularity & Scalability:** Large projects are easier to manage by breaking them into classes.
✅ **Encapsulation:** Protects data and only exposes necessary details.
✅ **Abstraction:** Hides implementation details to reduce complexity.

---
### **4. OOP in Action: Key Principles**

#### **1. Encapsulation** (Data Hiding)
Restrict access to certain data to prevent unintended modification.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable
    
    def deposit(self, amount):
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance
```

#### **2. Inheritance** (Code Reusability)
Allows a class to inherit attributes and methods from another class.

```python
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Bark"
```

#### **3. Polymorphism** (Different Behavior for the Same Method)
Allows different classes to define the same method differently.

```python
for animal in [Dog(), Animal()]:
    print(animal.speak())
```

#### **4. Abstraction** (Hiding Implementation Details)
Hides complex logic, exposing only necessary parts.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius
```

---
### **5. Summary**
- **Class:** Blueprint for creating objects.
- **Object:** Instance of a class with properties and behaviors.
- **Encapsulation:** Restricts direct access to variables.
- **Inheritance:** Allows code reuse across classes.
- **Polymorphism:** Enables multiple implementations of the same method.
- **Abstraction:** Hides unnecessary details from users.

OOP helps in building scalable, maintainable, and reusable software systems! 🚀

