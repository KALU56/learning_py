### **Difference Between an Abstract Method and a Regular Method**

| **Aspect**                | **Abstract Method**                                                                                      | **Regular Method**                                                                            |
|---------------------------|----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| **Definition**            | A method that is declared but not implemented in a class.                                               | A method that is fully implemented and can be called directly.                              |
| **Purpose**               | To enforce a contract: subclasses must provide an implementation.                                       | To define functionality that can be reused as-is or overridden.                            |
| **Implementation**        | Declared in a class (usually an abstract or interface class) without a body.                            | Contains a body with executable code.                                                      |
| **Use Case**              | Used when you want derived classes to provide their specific implementations.                           | Used when you want to implement functionality that might or might not need customization.  |
| **Class Type**            | Must belong to a class defined as `abstract` (if using `ABC` in Python).                                | Can belong to any class, abstract or not.                                                  |
| **Instantiation**         | The class containing an abstract method cannot be instantiated directly.                                | The class containing only regular methods can be instantiated directly.                    |

---

### **Example of Abstract Method vs. Regular Method**

#### Abstract Method Example
In Python, abstract methods are defined using the `abc` (Abstract Base Class) module:

```python
from abc import ABC, abstractmethod

class Shape(ABC):  # Abstract base class
    @abstractmethod
    def area(self):
        pass  # No implementation here; subclasses must implement this

    def description(self):
        return "This is a shape"  # Regular method with implementation

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2  # Implementing the abstract method

# shape = Shape()  # This will raise an error: Can't instantiate abstract class
circle = Circle(5)
print(circle.area())          # Calls the overridden area method
print(circle.description())   # Calls the regular method from the base class
```

#### Regular Method Example
```python
class Shape:
    def area(self):
        return 0  # Regular method with default implementation

    def description(self):
        return "This is a shape"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):  # Overriding the regular method
        return self.width * self.height

# Instantiate and use the class
shape = Shape()
rectangle = Rectangle(4, 5)
print(shape.area())          # Calls the base class implementation
print(rectangle.area())      # Calls the overridden method
print(rectangle.description())  # Inherited without modification
```

---

### **Key Differences in Action**
1. Abstract methods enforce subclass implementation (`Shape.area()` must be implemented in `Circle`).
2. Regular methods provide reusable functionality directly (`Shape.description()` is reusable as-is).