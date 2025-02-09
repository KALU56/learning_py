# **Object-Oriented Programming (OOP) in Python – Detailed Explanation with Line-by-Line Analysis**  

OOP is a programming paradigm based on objects, which bundle **data (attributes)** and **behavior (methods)** together. This approach makes it easier to manage, scale, and reuse code.

---

# **1. Classes and Objects in Detail**  

### **What is a Class?**  
A **class** is a blueprint for creating objects. It defines attributes and methods that describe how an object behaves.  

### **What is an Object?**  
An **object** is an instance of a class, meaning it follows the structure defined by the class but has its own unique data.

### **Example – Creating a Simple Class and Object**  
```python
class Car:  # Class definition
    def __init__(self, brand, model, year):  # Constructor method
        self.brand = brand  # Instance variable: stores the car's brand
        self.model = model  # Instance variable: stores the car's model
        self.year = year  # Instance variable: stores the car's manufacturing year

    def display_info(self):  # Method to return formatted details
        return f"{self.year} {self.brand} {self.model}"

# Creating objects (instances) of the Car class
car1 = Car("Toyota", "Corolla", 2020)  
car2 = Car("Honda", "Civic", 2022)  

print(car1.display_info())  # Output: 2020 Toyota Corolla
print(car2.display_info())  # Output: 2022 Honda Civic
```

### **Code Explanation**
1. **Defining the class (`Car`)** – Serves as a template for all car objects.  
2. **Constructor (`__init__()`)** – Automatically runs when an object is created, initializing attributes.  
3. **Instance variables (`self.brand, self.model, self.year`)** – Store unique values for each car.  
4. **Method (`display_info()`)** – Returns a formatted string with car details.  
5. **Creating objects (`car1`, `car2`)** – Each object has unique data but follows the same class structure.  

### **Why Use Classes and Objects?**
- **Code Reusability** – You can create multiple cars without rewriting the same code.  
- **Organization** – Keeps related data and functions together.  
- **Scalability** – Easily extendable with new features.  

---

# **2. Class Variables vs. Instance Variables**  

| **Type** | **Scope** | **Example** |
|----------|----------|------------|
| **Class Variable** | Shared among all objects | `school_name = "ABC School"` |
| **Instance Variable** | Unique for each object | `self.name = name` |

### **Example – Understanding Class and Instance Variables**
```python
class School:
    school_name = "ABC School"  # Class variable shared by all instances

    def __init__(self, student_name):
        self.student_name = student_name  # Instance variable unique for each object

s1 = School("Alice")
s2 = School("Bob")

print(s1.student_name)  # Output: Alice (unique to s1)
print(s2.student_name)  # Output: Bob (unique to s2)

print(s1.school_name)  # Output: ABC School (shared)
print(s2.school_name)  # Output: ABC School (shared)

School.school_name = "XYZ School"  # Change class variable

print(s1.school_name)  # Output: XYZ School
print(s2.school_name)  # Output: XYZ School
```

### **Why Use Class Variables?**
- **Memory-efficient** – Instead of storing the same value for each object, a single shared value is used.  
- **Consistency** – Ensures that all instances share the same information, like school name.  

---

# **3. Encapsulation & Properties (Getters & Setters)**  

### **Encapsulation** – Restricts direct access to attributes and allows controlled access using **getters and setters**.  
- **Public Attributes** (`self.name`) – Can be accessed and modified directly.  
- **Private Attributes** (`self.__balance`) – Cannot be accessed directly from outside.  

### **Example – Using Getters & Setters**
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable (cannot be accessed directly)

    @property
    def balance(self):  # Getter method to retrieve balance
        return self.__balance  

    @balance.setter
    def balance(self, amount):  # Setter method to modify balance safely
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = amount  

account = BankAccount(1000)
print(account.balance)  # Output: 1000

account.balance = 2000  # Modifying balance using setter
print(account.balance)  # Output: 2000

# account.__balance = -500  # This would cause an error because __balance is private
```

### **Why Use Getters & Setters?**
- **Encapsulation** – Protects data from direct modification.  
- **Validation** – Prevents invalid values (e.g., negative balance).  

---

# **4. Inheritance – Code Reusability**  

### **What is Inheritance?**  
Inheritance allows a **child class** to inherit attributes and methods from a **parent class**.  

### **Example – Inheriting Attributes & Methods**
```python
class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        return "Some sound"

class Dog(Animal):  # Dog class inherits from Animal
    def __init__(self, name):
        super().__init__("Dog")  # Call parent constructor
        self.name = name

    def make_sound(self):  # Overriding parent method
        return "Bark"

dog1 = Dog("Buddy")
print(dog1.species)  # Output: Dog
print(dog1.make_sound())  # Output: Bark
```

### **Why Use Inheritance?**
- **Code Reusability** – Avoids writing duplicate code.  
- **Hierarchy Representation** – Represents relationships like `Animal -> Dog`.  

---

# **5. Polymorphism – One Interface, Many Forms**  
Polymorphism allows a method to behave differently based on the object calling it.  

### **Example – Polymorphism in Action**
```python
class Animal:
    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def speak(self):
        return "Bark"

class Cat(Animal):
    def speak(self):
        return "Meow"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())  # Output: Bark, Meow
```

### **Why Use Polymorphism?**
- **Flexibility** – A single function can work with different object types.  
- **Scalability** – New object types can be added without modifying existing code.  

---

# **6. Abstraction – Hiding Implementation Details**  

### **What is Abstraction?**  
- Only **essential details** are exposed, while the implementation is hidden.  
- Achieved using **abstract classes** (`ABC` module).  

### **Example – Using Abstraction**
```python
from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract class
    @abstractmethod
    def speak(self):
        pass  # Abstract method with no implementation

class Dog(Animal):
    def speak(self):
        return "Bark"

dog1 = Dog()
print(dog1.speak())  # Output: Bark
```

### **Why Use Abstraction?**
- **Hides Complexity** – Users only need to know `speak()`, not how it's implemented.  
- **Standardization** – Ensures that all subclasses implement required methods.  

---

# **Smart Summary**  

| **Concept** | **Description** | **Why Use It?** |
|------------|----------------|-----------------|
| **Classes & Objects** | Define reusable blueprints for creating objects. | Organizes data & behavior together. |
| **Encapsulation** | Restricts access to data using getters & setters. | Protects data & ensures controlled modification. |
| **Inheritance** | Child class reuses attributes & methods of the parent. | Avoids code duplication. |
| **Polymorphism** | Same method behaves differently for different objects. | Increases flexibility. |
| **Abstraction** | Hides unnecessary details from the user. | Simplifies complex logic. |

OOP helps in **building scalable, maintainable, and efficient software** by structuring code in a reusable and logical manner! 🚀