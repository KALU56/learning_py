Here’s a detailed note on **Conditional Statements in Python** that you can use for your practical exam preparation:

---

## **Conditional Statements in Python**

Conditional statements in Python are used to execute code based on specific conditions. They are essential for decision-making in programs. Python uses the following keywords for conditional statements:

1. **if**
2. **elif** (short for else if)
3. **else**

### **Syntax**
```python
if condition:
    # Code block for true condition
elif another_condition:
    # Code block for another true condition
else:
    # Code block if all conditions are false
```

---

### **Components of Conditional Statements**

1. **Condition**:
   - A condition is an expression that evaluates to `True` or `False`.
   - Conditions often use comparison operators (e.g., `==`, `!=`, `<`, `>`, `<=`, `>=`) or logical operators (e.g., `and`, `or`, `not`).

2. **Code Block**:
   - The indented block of code under a conditional statement.
   - Indentation is critical in Python; it defines the scope of the conditional block.

---

### **Types of Conditional Statements**

1. **Simple if Statement**:
   Executes a block of code if the condition is `True`.
   ```python
   age = 18
   if age >= 18:
       print("You are eligible to vote.")
   ```

2. **if-else Statement**:
   Executes one block of code if the condition is `True`, and another block if it is `False`.
   ```python
   age = 16
   if age >= 18:
       print("You are eligible to vote.")
   else:
       print("You are not eligible to vote.")
   ```

3. **if-elif-else Statement**:
   Used to check multiple conditions. Only the first true condition's block is executed.
   ```python
   marks = 75
   if marks >= 90:
       print("Grade: A")
   elif marks >= 75:
       print("Grade: B")
   elif marks >= 60:
       print("Grade: C")
   else:
       print("Grade: D")
   ```

4. **Nested if Statement**:
   An `if` statement inside another `if` statement.
   ```python
   num = 15
   if num > 0:
       if num % 2 == 0:
           print("Positive Even Number")
       else:
           print("Positive Odd Number")
   else:
       print("Negative Number")
   ```

---

### **Practical Examples**

1. **Check if a Number is Even or Odd**:
   ```python
   number = int(input("Enter a number: "))
   if number % 2 == 0:
       print(f"{number} is Even.")
   else:
       print(f"{number} is Odd.")
   ```

2. **Find the Largest Number Among Three Numbers**:
   ```python
   a = int(input("Enter first number: "))
   b = int(input("Enter second number: "))
   c = int(input("Enter third number: "))
   
   if a > b and a > c:
       print(f"{a} is the largest.")
   elif b > c:
       print(f"{b} is the largest.")
   else:
       print(f"{c} is the largest.")
   ```

3. **Grading System**:
   ```python
   score = int(input("Enter your score: "))
   if score >= 90:
       print("Grade: A")
   elif score >= 80:
       print("Grade: B")
   elif score >= 70:
       print("Grade: C")
   elif score >= 60:
       print("Grade: D")
   else:
       print("Grade: F")
   ```

4. **Leap Year Check**:
   ```python
   year = int(input("Enter a year: "))
   if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
       print(f"{year} is a leap year.")
   else:
       print(f"{year} is not a leap year.")
   ```

5. **ATM Withdrawal System**:
   ```python
   balance = 5000
   amount = int(input("Enter withdrawal amount: "))
   
   if amount <= balance:
       print("Withdrawal successful.")
       balance -= amount
       print(f"Remaining balance: {balance}")
   else:
       print("Insufficient balance.")
   ```

---

### **Points to Remember**
- **Indentation** is crucial in Python. Use 4 spaces (or a tab) to indent code blocks.
- Only the first true condition in an `if-elif` chain is executed.
- Use parentheses for complex conditions to improve readability.
- Avoid redundant `else` blocks if the logic doesn't require it.

---

### **Practice Questions**
1. Write a Python program to check whether a number is positive, negative, or zero.
2. Create a simple calculator using if-elif-else.
3. Write a Python program to find the roots of a quadratic equation.

With these notes and examples, you’ll be well-prepared for your practical exam. Good luck! 😊