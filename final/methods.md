## **Methods in Python Classes – A Detailed Explanation**  

In Python, **methods** are functions defined inside a class that operate on instances, class variables, or external logic. There are **three** main types of methods in Python:  

1. **Instance Methods** (work on instance attributes)  
2. **Class Methods** (work on class attributes)  
3. **Static Methods** (independent of instance/class, used for utility tasks)  

Additionally, **Encapsulation** allows controlled access using **Getters & Setters**.

---

## **1. Instance Methods**  

### **Definition**  
- Instance methods work **on instance attributes** (data unique to each object).  
- They require `self` as the **first parameter** to access instance-specific data.  

### **Example – Instance Method**
```python
class Student:
    def __init__(self, name, age):
        self.name = name   # Instance attribute
        self.age = age     # Instance attribute

    def print_info(self):  # Instance method
        print(f"Name: {self.name}, Age: {self.age}")

# Creating an instance
student1 = Student("John", 20)
student1.print_info()  # Output: Name: John, Age: 20
```

### **Why Use Instance Methods?**
- They **modify or retrieve instance-specific** data.  
- Every object has **its own data**, making the method work on that specific object.  

### **Key Differences from Other Methods**
| **Feature**       | **Instance Method** |
|------------------|-------------------|
| Works on        | Instance attributes (`self.name`, `self.age`) |
| Requires `self` | ✅ Yes |
| Changes instance-specific data? | ✅ Yes |
| Access class variables? | ✅ Yes (via `self.__class__.variable_name`) |
| Call Syntax | `object.method()` |

---

## **2. Class Methods**  

### **Definition**  
- Class methods **work on class-level attributes** (shared across all instances).  
- They require `cls` (class itself) as the **first parameter**.  
- Defined using the `@classmethod` **decorator**.  

### **Example – Class Method**
```python
class Student:
    school_name = "ABC School"  # Class variable (shared)

    @classmethod
    def get_school_name(cls):  # Class method
        return cls.school_name

# Calling the class method
print(Student.get_school_name())  # Output: ABC School
```

### **Why Use Class Methods?**
- They work with **class attributes** instead of instance attributes.  
- Useful when a method needs to **modify or retrieve class-level information**.  

### **Key Differences from Other Methods**
| **Feature**       | **Class Method** |
|------------------|----------------|
| Works on        | Class attributes (`cls.variable`) |
| Requires `cls`  | ✅ Yes |
| Changes class-wide data? | ✅ Yes |
| Access instance variables? | ❌ No |
| Call Syntax | `Class.method()` or `object.method()` |

---

## **3. Static Methods**  

### **Definition**  
- **Independent** of both instance (`self`) and class (`cls`).  
- Used for **utility functions** that do not modify instance or class data.  
- Defined using the `@staticmethod` **decorator**.  

### **Example – Static Method**
```python
class Math:
    @staticmethod
    def add(x, y):  # Static method (no self or cls)
        return x + y

# Calling the static method
print(Math.add(5, 3))  # Output: 8
```

### **Why Use Static Methods?**
- When a method **doesn’t need to access or modify** instance/class attributes.  
- Used for **helper functions**, like calculations or string manipulations.  

### **Key Differences from Other Methods**
| **Feature**       | **Static Method** |
|------------------|----------------|
| Works on        | General utility logic (no instance/class data) |
| Requires `self` or `cls`? | ❌ No |
| Changes instance/class data? | ❌ No |
| Call Syntax | `Class.method()` or `object.method()` |

---

## **4. Encapsulation & Properties (Getters & Setters)**  

### **Definition**  
- Encapsulation restricts **direct access** to an attribute.  
- `_single underscore` → **Protected** (by convention, should not be accessed directly).  
- `__double underscore` → **Private** (name-mangled, harder to access directly).  
- **Getters & Setters** allow controlled access to private attributes.  

### **Example – Getters & Setters**
```python
class Student:
    def __init__(self, name):
        self._name = name  # Private attribute

    @property
    def name(self):  # Getter
        return self._name

    @name.setter
    def name(self, value):  # Setter
        self._name = value

student1 = Student("John")
student1.name = "Abel"  # Calls setter
print(student1.name)  # Calls getter, Output: Abel
```

### **Why Use Getters & Setters?**
- **Encapsulation** – Protects attributes from being modified incorrectly.  
- **Validation** – Can restrict invalid values.  
- **Flexibility** – If internal implementation changes, the API remains consistent.  

### **Key Differences from Other Methods**
| **Feature**       | **Getter & Setter Methods** |
|------------------|--------------------------|
| Works on        | Private attributes (`self.__attribute`) |
| Controls data access? | ✅ Yes |
| Uses `@property`? | ✅ Yes |
| Call Syntax | `object.attribute` (not like a function) |

---

## **Summary – Comparing All Method Types**  

| **Method Type** | **Works on** | **Requires** | **Modifies Data?** | **Usage Example** |
|---------------|------------|------------|--------------|----------------|
| **Instance Method** | Instance attributes | `self` | ✅ Yes (instance-specific) | Modify/retrieve object’s data |
| **Class Method** | Class attributes | `cls` | ✅ Yes (class-wide) | Modify/retrieve shared class data |
| **Static Method** | No specific data | None | ❌ No | General utility function |
| **Getter & Setter** | Private attributes | `@property`, `@name.setter` | ✅ Yes (controlled access) | Restrict or validate attribute changes |

---

## **Final Takeaways**  

### **When to Use Each Method?**
✅ **Use instance methods** when you need to modify or retrieve **object-specific** data.  
✅ **Use class methods** when you need to modify or retrieve **class-wide** data.  
✅ **Use static methods** for **utility functions** that do not depend on instance or class.  
✅ **Use getters & setters** to **encapsulate data** and control access.

---

This structured approach helps **write clean, reusable, and maintainable OOP code** in Python! 🚀