# Practical Examples
# Check if a Number is Even or Odd:
number=int(input("Enter a number: "))
if number%2==0:
  print("The number is even")
else:
  print("The number is odd")

# Find the Largest Number Among Three Numbers:
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number: "))
if num1>num2 and num1>num3:
  print("The largest number is",num1)
elif num2>num1 and num2>num3:
  print("The largest number is",num2)
else:
  print("The largest number is",num3)

#Grading System:
score=int(input("Enter the score: "))
if score>=90:
  print("Grade: A")
elif score>=80:
  print("Grade: B")
elif score>=70:
  print("Grade: C")
else:
  print("Grade: F")
#Leap Year Check:
year=int(input("Enter the year: "))
if year%4==0:
  print("The year is a leap year")
else:
  print("The year is not a leap year")
# ATM Withdrawal System:
balance=int(input("Enter the balance: "))
withdrawal=int(input("Enter the withdrawal amount: "))
if withdrawal<=balance:
  balance=balance-withdrawal
  print("Withdrawal successful")
  print("Remaining balance:",balance)
else:
  print("Insufficient balance")
#Practice Questions
#1 Write a Python program to check whether a number is positive, negative, or zero.
num=int(input("enter your want : "))
if num>0 :
  print("it is +ve")
elif num<0:
  print("it is -ve")
else:
  print("it is zero")
#2 Create a simple calculator using if-elif-else.
num1=int(input("enter your want : "))
num2=nt(input("enter your want : "))
operater=input("your want operater")
if operater=="+" :
  print({num1} + {num2}) 
elif operater=="*" :
  print({num1} * {num2}) 
elif operater=="/" :
  print({num1} / {num2}) 
elif operater=="-" :
  print({num1} - {num2}) 
else:
  print("invalid")
#3 Write a Python program to find the roots of a quadratic equation.
import math

# Input coefficients
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

# Calculate the discriminant
d = b**2 - 4*a*c

# Check the nature of roots based on discriminant
if d > 0:
    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b - math.sqrt(d)) / (2 * a)
    print(f"The roots are real and distinct: root1 = {root1}, root2 = {root2}")
elif d == 0:
    root1 = root2 = -b / (2 * a)
    print(f"The roots are real and equal: root1 = root2 = {root1}")
else:
    real_part = -b / (2 * a)
    imaginary_part = math.sqrt(-d) / (2 * a)
    print(f"The roots are complex: root1 = {real_part} + {imaginary_part}i, root2 = {real_part} - {imaginary_part}i")

