Here’s a **detailed note on `match` statements in Python** for your practical exam preparation:

---

## **Python `match` Statement (Pattern Matching)**

The `match` statement in Python (introduced in Python 3.10) allows for **pattern matching**, enabling you to match values against patterns and execute specific code blocks. It is similar to a `switch-case` statement in other languages but much more powerful.

---

### **Basic Syntax**
```python
match variable:
    case pattern1:
        # Code to execute if variable matches pattern1
    case pattern2:
        # Code to execute if variable matches pattern2
    case _:
        # Default case (if no other patterns match)
```

- **`variable`**: The value you want to match against.
- **`case`**: Defines a pattern to match.
- **`_`**: A wildcard pattern that matches anything (like the `default` in `switch`).

---

### **Features of `match`**
1. **Simple Value Matching**:
   Match variable values directly.
   ```python
   match x:
       case 1:
           print("x is 1")
       case 2:
           print("x is 2")
       case _:
           print("x is something else")
   ```

2. **Tuple/Sequence Matching**:
   Match structures like tuples or lists.
   ```python
   match point:
       case (0, 0):
           print("Origin")
       case (0, y):
           print(f"Point on Y-axis at {y}")
       case (x, 0):
           print(f"Point on X-axis at {x}")
       case (x, y):
           print(f"Point at ({x}, {y})")
   ```

3. **Destructuring**:
   Extract values from objects or tuples.
   ```python
   match coordinates:
       case (x, y, z):
           print(f"3D Point with x={x}, y={y}, z={z}")
   ```

4. **Guard Conditions**:
   Add conditions for a match using `if`.
   ```python
   match number:
       case n if n > 0:
           print("Positive number")
       case n if n < 0:
           print("Negative number")
       case _:
           print("Zero")
   ```

5. **Class Matching**:
   Match objects of specific classes and destructure attributes.
   ```python
   class Point:
       def __init__(self, x, y):
           self.x = x
           self.y = y

   point = Point(3, 4)

   match point:
       case Point(x=0, y=0):
           print("Origin")
       case Point(x, y):
           print(f"Point at ({x}, {y})")
   ```

---

### **Examples**

#### **1. Matching Days of the Week**
```python
day = "Monday"

match day:
    case "Monday":
        print("Start of the workweek!")
    case "Friday":
        print("End of the workweek!")
    case "Saturday" | "Sunday":
        print("It's the weekend!")
    case _:
        print("A regular weekday.")
```

#### **2. Grading System**
```python
score = 85

match score:
    case n if n >= 90:
        print("Grade: A")
    case n if 80 <= n < 90:
        print("Grade: B")
    case n if 70 <= n < 80:
        print("Grade: C")
    case n if 60 <= n < 70:
        print("Grade: D")
    case _:
        print("Grade: F")
```

#### **3. Shape Detection**
```python
shape = ("rectangle", 10, 20)

match shape:
    case ("circle", r):
        print(f"Circle with radius {r}")
    case ("rectangle", l, w):
        print(f"Rectangle with length {l} and width {w}")
    case ("triangle", a, b, c):
        print(f"Triangle with sides {a}, {b}, and {c}")
    case _:
        print("Unknown shape")
```

#### **4. Command-Line Arguments**
```python
command = ("copy", "/path/to/source", "/path/to/destination")

match command:
    case ("copy", src, dest):
        print(f"Copying from {src} to {dest}")
    case ("delete", path):
        print(f"Deleting {path}")
    case ("move", src, dest):
        print(f"Moving from {src} to {dest}")
    case _:
        print("Unknown command")
```

---

### **Key Points to Remember**
1. **Use `_` for Default Cases**:
   - The wildcard `_` matches any value and acts as the "default" case.
   
2. **Readable Conditions**:
   - Use `if` conditions to add extra logic to patterns.

3. **Match Data Structures**:
   - The `match` statement supports advanced patterns like tuples, lists, and objects.

4. **Type Safety**:
   - Ensure the patterns match the expected data type to avoid runtime errors.

5. **Python Version**:
   - The `match` statement is available starting from Python 3.10.

---

### **Practical Applications**

#### **1. Input Validation**
```python
input_value = "42"

match input_value:
    case str() if input_value.isdigit():
        print(f"Valid number: {int(input_value)}")
    case str():
        print("Input is a string but not a number.")
    case _:
        print("Invalid input.")
```

#### **2. File Operation Commands**
```python
command = ("create", "file.txt")

match command:
    case ("create", filename):
        print(f"Creating file {filename}")
    case ("delete", filename):
        print(f"Deleting file {filename}")
    case _:
        print("Unknown command")
```

---

By mastering the `match` statement, you’ll be equipped to handle modern Python programming scenarios effectively. Let me know if you'd like more examples or explanations! 😊