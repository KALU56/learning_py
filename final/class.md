**OOP Final Exam Notes**

### **Class**
📌 A blueprint for real-world objects/entities.
📌 Functions as a template or form for creating objects.
📌 Bundles properties (attributes) and methods (functions).
📌 User-defined data type.

#### **Syntax:**
```python
class ClassName:
    properties
    methods
```
📌 `class` is the keyword used to define a class.
📌 Class names should follow PascalCase convention (e.g., `Student`).
📌 Members of the class (attributes and methods) are accessed using the dot (`.`) operator.

#### **Example:**
```python
class Student:
    pass

print(Student)  # Output: <class '__main__.Student'>
print(type(Student))  # Output: <class 'type'>
```

---

### **`__init__()` Method**
📌 Special (magic) method used to initialize attributes.
📌 Helps to pass data when an object is instantiated.

#### **Example:**
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

### **Variables in OOP**
✅ **Instance Variables**: Specific to each instance.
   - Example: `name`, `age`
✅ **Class Variables**: Shared across all instances.
   - Example: `first_name`, `last_name`

#### **Example:**
```python
class Student:
    school = "ABC High School"  # Class variable

    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age  # Instance variable
```

---

### **Methods in OOP**
✅ **Instance Methods**: Operate on instance attributes.
✅ **Class Methods**: Operate on class-level data (`@classmethod`).
✅ **Static Methods**: Utility functions that do not access class or instance attributes (`@staticmethod`).
✅ **Magic/Dunder Methods**: Special built-in methods (`__init__`, `__str__`, etc.).

#### **Instance Method Example:**
```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def print_info(self):
        print("Name:", self.name, ", Age:", self.age)

student1 = Student("John", 20)
student1.print_info()
```

---

### **Class Methods**
📌 Operate on class attributes rather than instance attributes.
📌 Defined using `@classmethod` decorator.

#### **Example:**
```python
class Student:
    school = "ABC High School"

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

Student.change_school("XYZ Academy")
print(Student.school)  # Output: XYZ Academy
```

---

### **Magic/Dunder Methods**
✅ Special methods in Python that start and end with double underscores (`__`).
✅ Provide built-in behavior like operator overloading and object initialization.

#### **Common Magic Methods:**
- `__init__()` - Initializes an object.
- `__str__()` - Returns a string representation of the object.
- `__eq__()` - Checks equality between objects.
- `__gt__()` - Checks if one object is greater than another.

#### **Example: `__str__()`**
```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

student1 = Student("John", 20)
print(student1)  # Output: Name: John, Age: 20
```

#### **Example: `__eq__()`**
```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __eq__(self, other):
        return self.age == other.age

student1 = Student("John", 20)
student2 = Student("Abel", 22)
print(student1 == student2)  # Output: False
```

#### **Example: `__gt__()`**
```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __gt__(self, other):
        return self.age > other.age

student1 = Student("John", 20)
student2 = Student("Abel", 22)
print(student1 > student2)  # Output: False
```

---

### **Best Practices in OOP**
✔ Use meaningful class names (PascalCase convention).
✔ Keep instance variables private (use getter and setter methods if needed).
✔ Follow DRY (Don't Repeat Yourself) principle.
✔ Use class methods where applicable instead of instance methods.
✔ Leverage magic methods for cleaner code and better object representation.

---

### **Benefits of OOP**
✅ **Code Reusability**: Encourages reuse of classes and objects.
✅ **Easier Debugging & Maintenance**: Modular structure simplifies troubleshooting.
✅ **Improved Scalability**: Suitable for large applications.
✅ **Encapsulation**: Enhances security by restricting direct access to object data.
✅ **Inheritance**: Allows new classes to derive properties from existing ones.

---

This guide provides a solid foundation for understanding OOP concepts in Python. 🚀

