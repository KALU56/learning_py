Each programming paradigm has a distinct approach to solving problems. Here’s the **main difference** between them:

---

## **1. Imperative Programming**  
📌 **Focus:** *How to do it* (step-by-step execution)  
📌 **Key Idea:** The program consists of instructions that change the program's state.  
📌 **Example Concept:** Think of a recipe where you give exact steps to follow.  

✅ **Advantages:**  
- Easy to understand for beginners  
- Provides full control over execution  
- Works well for simple tasks  

❌ **Disadvantages:**  
- Can lead to complex, hard-to-maintain code  
- Prone to errors due to direct state manipulation  

**Example (Imperative Style in Python):**  
```python
numbers = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for number in numbers:
    if number != 8:
        sum += number

print("Sum of the first ten integers except 8 =", sum)
```
---

## **2. Procedural Programming**  
📌 **Focus:** *Breaking the program into functions (procedures)*  
📌 **Key Idea:** Organizing code into reusable functions to improve modularity.  
📌 **Example Concept:** Like a factory, where different departments (functions) handle specific tasks.  

✅ **Advantages:**  
- Code is structured and modular  
- Easier to debug and maintain  
- Avoids repetition (DRY principle: Don't Repeat Yourself)  

❌ **Disadvantages:**  
- Less reusable compared to OOP  
- Functions still operate on global data, leading to side effects  

**Example (Procedural Style in Python):**  
```python
numbers = [1,2,3,4,5,6,7,8,9,10]

def add():
    sum = 0
    for number in numbers:
        if number != 8:
            sum += number
    return sum

print("Sum of the first ten integers except 8 =", add())
```
---

## **3. Functional Programming**  
📌 **Focus:** *What to do, not how to do it* (avoiding state changes)  
📌 **Key Idea:** Uses **pure functions** that always return the same result given the same input.  
📌 **Example Concept:** Like a math function, where `f(x) = x + 2` always gives the same result for `x`.  

✅ **Advantages:**  
- No side effects (doesn't change state)  
- Easier debugging and parallel processing  
- More predictable code  

❌ **Disadvantages:**  
- Can be harder to understand for beginners  
- Sometimes less efficient (since data is immutable)  

**Example (Functional Style in Python):**  
```python
numbers = [1,2,3,4,5,6,7,8,9,10]

# Using filter and sum (Functional approach)
sum_result = sum(filter(lambda x: x != 8, numbers))

print("Sum of the first ten integers except 8 =", sum_result)
```
---

## **4. Declarative Programming**  
📌 **Focus:** *What should be done, not how*  
📌 **Key Idea:** Hides implementation details, focusing on high-level logic.  
📌 **Example Concept:** Like SQL queries (`SELECT * FROM students WHERE age > 18`) – you don’t worry about *how* it fetches data.  

✅ **Advantages:**  
- Simplifies complex operations  
- More readable and maintainable  
- Reduces code size  

❌ **Disadvantages:**  
- Less control over execution  
- Can be difficult to debug if an error occurs  

**Example (Declarative Style in Python):**  
```python
numbers = [1,2,3,4,5,6,7,8,9,10]

# Using lambda functions (Declarative)
add = lambda: sum(filter(lambda x: x != 8, numbers))

print("Sum of the first ten integers except 8 =", add())
```
---

## **5. Object-Oriented Programming (OOP)**  
📌 **Focus:** *Modeling real-world entities using objects*  
📌 **Key Idea:** Uses **classes** to define **objects** that contain **attributes** and **methods**.  
📌 **Example Concept:** Like a car blueprint (class) that can be used to create many cars (objects).  

✅ **Advantages:**  
- Encourages code reuse (via inheritance)  
- Easier to scale and maintain large programs  
- Encapsulation improves security and data hiding  

❌ **Disadvantages:**  
- More complex than procedural programming  
- Can introduce unnecessary complexity for small programs  

**Example (OOP Style in Python):**  
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Creating an object
person1 = Person("John", 25)
print(person1.introduce())
```
---

## **🔍 Key Differences Between Each Paradigm**
| Paradigm        | Focus                         | How it Works | Example Concept |
|----------------|--------------------------------|--------------|----------------|
| **Imperative** | Step-by-step execution       | Uses loops & conditionals | Cooking recipe (exact steps) |
| **Procedural** | Organizing code into functions | Uses functions to group logic | Factory departments (each does one task) |
| **Functional** | Avoiding state changes       | Uses pure functions & immutability | Math function (f(x) = x + 2) |
| **Declarative** | Describing what to do, not how | Uses high-level functions like `map()` | SQL query (`SELECT * FROM users`) |
| **OOP** | Modeling real-world entities | Uses objects & classes | Car blueprint (Class → Object) |

---

### **📌 When to Use Each Paradigm?**
| Paradigm | When to Use? |
|----------|-------------|
| **Imperative** | Simple scripts, small tasks |
| **Procedural** | Medium-sized programs where modularity is needed |
| **Functional** | When immutability and pure functions are beneficial (e.g., data analysis) |
| **Declarative** | When working with databases, automation, or UI frameworks |
| **OOP** | Large applications with complex structures (e.g., web apps, game development) |

---

## **🎯 Conclusion**
- **Imperative**: Tells the computer *how* to do something step by step.  
- **Procedural**: Uses **functions** to organize code into reusable blocks.  
- **Functional**: Uses **pure functions** and **immutable data** to avoid side effects.  
- **Declarative**: Focuses on *what* needs to be done, hiding implementation details.  
- **OOP**: Models real-world entities using **classes and objects**.  

Each paradigm has its own strengths and weaknesses, and **Python allows you to use multiple paradigms** together! 🚀