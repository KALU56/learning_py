class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

p = Person('Selam', 'Yetayeh', 25, 'Finland', 'Helsinki')
print(p.firstname)  # Output: Selam
print(p.lastname)   # Output: Yetayeh

print(p.age)

class Person:
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    

# Creating two objects of the Person class
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Accessing instance attributes
print(person1.name, person1.age)  # Output: Alice 25
print(person2.name, person2.age)  # Output: Bob 30

# Modifying instance attributes
person1.age = 26
print(person1.age)  # Output: 26
class Car:
    wheels = 4  # Class attribute

    def __init__(self, make, model):
        self.make = make  # Instance attribute
        self.model = model  # Instance attribute

# Creating two objects of the Car class
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

# Accessing class attributes
print(car1.wheels)  # Output: 4
print(car2.wheels)  # Output: 4

# Accessing instance attributes
print(car1.make, car1.model)  # Output: Toyota Corolla
print(car2.make, car2.model)  # Output: Honda Civic

# Modifying the class attribute
Car.wheels = 5
print(car1.wheels)  # Output: 5
print(car2.wheels)  # Output: 5
class Employee:
    company_name = "TechCorp"  # Class attribute

    def __init__(self, name, position):
        self.name = name  # Instance attribute
        self.position = position  # Instance attribute
 
# Creating objects
emp1 = Employee("Alice", "Developer")
emp2 = Employee("Bob", "Manager")

# Accessing both attributes
print(emp1.name, emp1.position, Employee.company_name)  # Output: Alice Developer TechCorp
print(emp2.name, emp2.position, emp2.company_name)  # Output: Bob Manager TechCorp