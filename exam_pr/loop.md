### **For Loop in Python**

The `for` loop in Python is used to iterate over a sequence (like a list, tuple, dictionary, set, or string) or a range of numbers.

---

### **Syntax**
```python
for variable in sequence:
    # Code block to execute for each element in the sequence
```

- **`variable`**: A placeholder that takes the value of each element in the sequence.
- **`sequence`**: The collection you are iterating over.
- The loop executes the block of code for each item in the sequence.

---

### **Using `for` with `range()`**
The `range()` function generates a sequence of numbers.
```python
for i in range(start, stop, step):
    # Code block
```

- **`start`**: Starting value (default is 0).
- **`stop`**: Stopping value (exclusive).
- **`step`**: Increment (default is 1).

Example:
```python
for i in range(1, 6):
    print(i)
# Output: 1 2 3 4 5
```

---

### **Loop Control Statements**
1. **`break`**: Exits the loop prematurely.
   ```python
   for i in range(1, 6):
       if i == 3:
           break
       print(i)
   # Output: 1 2
   ```

2. **`continue`**: Skips the current iteration and moves to the next one.
   ```python
   for i in range(1, 6):
       if i == 3:
           continue
       print(i)
   # Output: 1 2 4 5
   ```

3. **`else` with `for`**: Executes if the loop completes normally (without `break`).
   ```python
   for i in range(3):
       print(i)
   else:
       print("Loop completed!")
   # Output: 0 1 2 Loop completed!
   ```

---

### **Pattern Printing Using Loops**
Pattern printing is a common practical problem solved using nested loops.

---

#### **1. Pyramid Pattern**
```python
rows = 5
for i in range(1, rows + 1):
    print("*" * i)
```
**Output:**
```
*
**
***
****
*****
```

---

#### **2. Inverted Pyramid Pattern**
```python
rows = 5
for i in range(rows, 0, -1):
    print("*" * i)
```
**Output:**
```
*****
****
***
**
*
```

---

#### **3. Right-Aligned Triangle**
```python
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * i)
```
**Output:**
```
    *
   **
  ***
 ****
*****
```

---

#### **4. Number Pyramid**
```python
rows = 5
for i in range(1, rows + 1):
    print("".join(str(j) for j in range(1, i + 1)))
```
**Output:**
```
1
12
123
1234
12345
```

---

#### **5. Diamond Pattern**
```python
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
```
**Output:**
```
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
```

---

#### **6. Pascal’s Triangle**
```python
rows = 5
for i in range(rows):
    print(" " * (rows - i), end="")
    num = 1
    for j in range(i + 1):
        print(f"{num} ", end="")
        num = num * (i - j) // (j + 1)
    print()
```
**Output:**
```
     1 
    1 1 
   1 2 1 
  1 3 3 1 
 1 4 6 4 1 
```

---

#### **7. Hollow Square Pattern**
```python
rows = 5
for i in range(rows):
    if i == 0 or i == rows - 1:
        print("*" * rows)
    else:
        print("*" + " " * (rows - 2) + "*")
```
**Output:**
```
*****
*   *
*   *
*   *
*****
```

---

### **Nested Loops for Patterns**
Nested loops are frequently used in pattern printing:
- The outer loop controls the rows.
- The inner loop controls the columns or elements in each row.

Example:
```python
rows = 4
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end="")
    print()  # Move to the next line
```
**Output:**
```
*
**
***
****
```

---

### **Points to Remember**
1. **Break down the pattern** into rows and columns to determine loop logic.
2. Use **nested loops** for more complex patterns.
3. Adjust spacing carefully for aligned patterns.
4. **`end=""`** in `print()` is useful for controlling output format.

---

By mastering `for` loops and patterns, you'll be well-prepared for practical exams, as these are commonly tested concepts. Let me know if you'd like more examples or advanced patterns! 😊