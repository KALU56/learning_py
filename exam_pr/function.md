### **Functions in Python**

Functions are reusable blocks of code that perform a specific task. They help make your programs more organized, modular, and easier to debug.

---

### **Defining a Function**

A function is defined using the `def` keyword.

```python
def function_name(parameters):
    """Optional docstring"""
    # Function body
    return value  # Optional
```

- **`function_name`**: Name of the function.
- **`parameters`**: Values passed to the function (optional).
- **`return`**: Returns a value from the function (optional).

---

### **Types of Functions**

1. **Built-in Functions**:
   Predefined in Python, like `print()`, `len()`, `type()`, etc.2
   ```python
   print("Hello, World!")
   print(len("Python"))  # Output: 6
   ```

2. **User-defined Functions**:
   Defined by the user.
   ```python
   def greet(name):
       return f"Hello, {name}!"

   print(greet("Alice"))  # Output: Hello, Alice!
   ```

3. **Lambda Functions**:
   Anonymous, single-line functions.
   ```python
   square = lambda x: x ** 2
   print(square(4))  # Output: 16
   ```

---

### **Calling a Function**

To execute a function, use its name followed by parentheses.

```python
def add(a, b):
    return a + b

result = add(3, 5)  # Calling the function
print(result)  # Output: 8
```

---

### **Parameters and Arguments**

- **Parameters**: Variables in the function definition.
- **Arguments**: Actual values passed to the function.

Example:
```python
def multiply(x, y):
    return x * y

print(multiply(2, 3))  # Output: 6
```

#### Types of Arguments
1. **Positional Arguments**:
   Matched to parameters based on position.
   ```python
   def greet(name, age):
       print(f"Name: {name}, Age: {age}")

   greet("Alice", 25)
   ```

2. **Keyword Arguments**:
   Matched to parameters by name.
   ```python
   greet(age=25, name="Alice")
   ```

3. **Default Arguments**:
   Parameters with default values.
   ```python
   def greet(name, age=18):
       print(f"Name: {name}, Age: {age}")

   greet("Bob")  # Output: Name: Bob, Age: 18
   ```

4. **Variable-length Arguments**:
   - **`*args`**: Passes multiple positional arguments.
     ```python
     def total(*args):
         return sum(args)

     print(total(1, 2, 3, 4))  # Output: 10
     ```
   - **`**kwargs`**: Passes multiple keyword arguments.
     ```python
     def display_info(**kwargs):
         for key,.
          value in kwargs.items():
             print(f"{key}: {value}")

     display_info(name="Alice", age=25)
     ```

---

### **Returning Values**

Functions can return values using the `return` statement.

```python
def square(x):
    return x ** 2

result = square(4)
print(result)  # Output: 16
```

---

### **Scopes of Variables**

1. **Local Scope**: Variables defined inside a function.
2. **Global Scope**: Variables defined outside a function.
3. **Global Keyword**: Modifies global variables inside a function.
   ```python
   x = 10

   def update():
       global x
       x += 5

   update()
   print(x)  # Output: 15
   ```

---

### **Recursive Functions**

A function that calls itself to solve smaller sub-problems.

Example:
```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120
```

---

### **Examples**

#### **1. Calculate the Area of a Circle**
```python
import math

def area_of_circle(radius):
    return math.pi * radius ** 2

print(area_of_circle(5))  # Output: 78.53981633974483
```

#### **2. Find the Largest Number**
```python
def largest(a, b, c):
    return max(a, b, c)

print(largest(10, 25, 15))  # Output: 25
```

#### **3. Fibonacci Sequence**
```python
def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

#### **4. Check if a Number is Prime**
```python
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

print(is_prime(17))  # Output: True
```

---

### **Advantages of Functions**
1. **Code Reusability**: Write once, use multiple times.
2. **Modularity**: Break large programs into smaller functions.
3. **Improved Readability**: Makes code easier to understand.
4. **Ease of Debugging**: Isolate errors in individual functions.

---

Let me know if you'd like more examples or detailed explanations! 😊