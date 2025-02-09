**Summary of Object-Oriented Programming (OOP) and Programming Paradigms**

### **Programming Paradigms**
The document introduces different programming paradigms, including:
1. **Imperative**: Focuses on step-by-step instructions to modify program state.
2. **Procedural**: Organizes code into reusable procedures or functions.
3. **Functional**: Treats computation as the evaluation of mathematical functions.
4. **Declarative**: Expresses logic without describing control flow.
5. **Object-Oriented**: Organizes data and behavior into objects and classes.

It provides examples of imperative, procedural, functional, and declarative paradigms.

### **Classes in OOP**
A class is a **blueprint** for creating objects. It defines a **user-defined data type** that bundles properties (attributes) and methods (functions).
- The syntax for defining a class is `class ClassName:`.
- A class can be defined with or without properties and methods.
- The `__init__()` method is used to pass data when an object is instantiated.
- **Instance attributes** are specific to an object instance.
- **Class attributes** are shared across all instances and can be referred to directly by the class.

### **Methods in a Class**
Methods are **functions within a class**. There are different types:
1. **Instance Methods**: Operate on instance-level data and take `self` as the first parameter.
2. **Class Methods**: Operate on the class itself and take `cls` as the first parameter. They are defined using the `@classmethod` decorator.
3. **Static Methods**: Do not modify class or instance state. Defined using `@staticmethod`.
4. **Magic/Dunder Methods**: Special methods that start and end with double underscores (`__init__`, `__str__`, `__eq__`, `__gt__`) to provide built-in behaviors.

### **Objects in OOP**
An object is an **instance** of a class. Objects store **data (attributes)** and perform **operations (methods)**.

### **Properties and Encapsulation**
- Properties help control attribute access using getter and setter methods.
- The `@property` decorator is used for defining a **getter**.
- The `@<name>.setter` decorator is used for defining a **setter**.
- Encapsulation is achieved using access modifiers:
  - **Public**: Accessible from anywhere.
  - **Protected (_attribute)**: Should not be accessed directly but is not strictly private.
  - **Private (__attribute)**: Cannot be accessed directly outside the class.

### **Four Pillars of OOP**
1. **Inheritance**
   - Enables **code reuse** by allowing a child class to inherit from a parent class.
   - Syntax: `class DerivedClass(BaseClass):`
   - The `super()` function allows calling methods from the parent class.
   - Multiple inheritance is possible but should be used with caution.

2. **Abstraction**
   - Hides complex implementation details and exposes only essential features.
   - Achieved using **abstract base classes (ABC)** and the `@abstractmethod` decorator from the `abc` module.

3. **Encapsulation**
   - Bundles data and methods into a single unit (**class**).
   - Restricts direct access to some attributes using access modifiers.

4. **Polymorphism**
   - Allows objects of different classes to be treated as instances of a common superclass.
   - Achieved through **method overriding** (subclass provides its own implementation of a parent method).
   - **Duck typing**: If an object behaves like a type, it can be used as that type.

### **Best Practices in OOP**
The document also mentions the **SOLID principles**, which help in designing scalable and maintainable software:
1. **Single Responsibility Principle (SRP)**: A class should have only one responsibility.
2. **Open-Closed Principle (OCP)**: Classes should be open for extension but closed for modification.
3. **Liskov Substitution Principle (LSP)**: Subtypes must be substitutable for their base types.
4. **Interface Segregation Principle (ISP)**: Clients should not be forced to depend on interfaces they do not use.
5. **Dependency Inversion Principle (DIP)**: High-level modules should not depend on low-level modules. Both should depend on abstractions.

This structured approach to OOP ensures better code organization, reusability, and maintainability.

