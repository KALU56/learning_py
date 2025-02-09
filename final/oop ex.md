Your notes are great! I've cleaned up the formatting and improved clarity while keeping the essential concepts. Let me know if you'd like any refinements! 🚀  

### **Object-Oriented Programming (OOP) in Python**

---

## **Class**
- A **class** is a blueprint for a real-world object/entity.
- It acts as a template that defines properties (attributes) and behaviors (methods).
- It is a **user-defined data type**.

### **Syntax**
```python
class ClassName:
    # Properties (attributes)
    # Methods (functions)
```
- **`class`** is a keyword to define a class.
- Class names should follow **PascalCase** (e.g., `Student`, `CarModel`).
- Use a **dot (`.`) operator** to access class members.

Example:
```python
class Student:
    pass

print(Student)          # <class '__main__.Student'>
print(type(Student))    # <class 'type'>
```

---

## **Object**
- An **object** is an **instance** of a class.
- Example: `student1` is an object of the `Student` class.

---

## **Instance Attributes & `__init__()` Method**
- The `__init__()` method (a **constructor**) is used to initialize instance attributes.
- It runs automatically when an object is created.

### **Example:**
```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("John", 20)
print("Name:", student1.name, ", Age:", student1.age)
```
**Output:**
```
Name: John, Age: 20
```

---

## **Class vs. Instance Variables**
- **Instance Variables:** Unique to each object (e.g., `name`, `age`).
- **Class Variables:** Shared across all instances (e.g., `school_name`).

```python
class Student:
    school_name = "ABC School"  # Class Variable

    def __init__(self, name, age):
        self.name = name  # Instance Variable
        self.age = age

student1 = Student("John", 20)
print(student1.school_name)  # ABC School
```

---

## **Methods in Python Classes**
### **Instance Method**
- Works on **instance attributes**.
- Requires `self` as the first parameter.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def print_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

student1 = Student("John", 20)
student1.print_info()
```

### **Class Method**
- Works on **class variables**.
- Uses `@classmethod` decorator.
- First parameter is `cls`.

```python
class Student:
    school_name = "ABC School"

    @classmethod
    def get_school_name(cls):
        return cls.school_name

print(Student.get_school_name())  # ABC School
```

### **Static Method**
- Doesn't use `self` or `cls`.
- Used for utility functions.

```python
class Math:
    @staticmethod
    def add(x, y):
        return x + y

print(Math.add(5, 3))  # 8
```

---

## **Encapsulation & Properties (Getters & Setters)**
- Use **`_` (single underscore)** or **`__` (double underscore)** for private attributes.
- **`@property`** is used to define a **getter**.
- **`@<name>.setter`** is used to define a **setter**.

```python
class Student:
    def __init__(self, name):
        self._name = name  # Private attribute

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

student1 = Student("John")
student1.name = "Abel"
print(student1.name)  # Abel
```

---

## **Four Pillars of OOP**
### **1. Inheritance**
- Allows a child class to inherit methods and attributes from a parent class.
- Uses `super()` to access the parent class.

```python
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(User):  # Student inherits from User
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

student1 = Student("John", 20, 12345)
print(student1.name, student1.student_id)  # John 12345
```

---

## **Magic (Dunder) Methods**
- **`__init__()`** → Constructor
- **`__str__()`** → String representation
- **`__eq__()`** → Equality comparison
- **`__gt__()`** → Greater than comparison

### **Example: `__str__()`**
```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

student1 = Student("John", 20)
print(student1)  # Name: John, Age: 20
```

### **Example: `__eq__()`**
```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

s1 = Student("John", 20)
s2 = Student("Abel", 22)
print(s1 == s2)  # False
```

---

### **Hope this makes things clearer! Let me know if you need any changes. 🚀**