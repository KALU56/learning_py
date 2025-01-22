### loops
#Q1 Write a Python program to print the multiplication table of a given number using a for loop.
# Input from the user
product = int(input("Enter the number for its multiplication table: "))

# Print the multiplication table up to 12
for i in range(1, 13):  # Loop from 1 to 12
    products = i * product
    print(f"{product} * {i} = {products}")
#Q2 Write a program to calculate the factorial of a number using a while loop.
num=int(input("enter the num "))
factorial=1
if num==0:
  print(1)
else:
  while num>0:
    factorial=factorial*num
    num=num-1
  print(factorial)


#Q3 Write a program to print all even numbers between 1 and 100 using a for loop.

for i in range(101):
  if i%2==0:
    print(i)

#Q4 Write a Python program to check if a given number is prime or not using a loop.
num1=int(input("enter the num "))
for i in range(num1):
  if num1%i==0:
    print("not prime")
  else:
    print("prime")
  

#Q5 Create a program that asks the user for a number and prints its digits in reverse order.
num2=int(input("enter the num "))
for i in range(num2):
  print(num2[::-1])
####Functions
#Q1   Write a function to calculate the sum of two numbers and return the result.
def sum(a,b):
  return a+b
print(sum(1,2))
#Q2 Create a function that takes a number as input and returns whether it is even or odd.
def even_odd(a):
  if a%2==0:
    print("even")
  else:
    print("odd")
even_odd(1)
#Q3 Write a function to calculate the area of a circle, given the radius.
def area_circle(r):
  return 3.14*r*r
print(area_circle(1))
#Q4 Write a program with a function to find the maximum of three numbers.
def max_three(a,b,c):
  return max(a,b,c)
print(max_three(1,2,3))
#Q5 Write a recursive function to calculate the Fibonacci sequence up to a given number.
def fibonacci(n):
  if n<=0:
    return 0
  elif n==1:
    return 1
  else:
    return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(1))
###Match-Case
#Q1 Write a Python program using match-case to implement a simple calculator that performs addition, subtraction, multiplication, and division based on the user's choice.
def calculator(a,b,c):
  match c:
    case "+":
      return a+b
    case "-":
      return a-b
    case "*":
      return a*b
    case "/":
      return a/b
print(calculator(1,2,"+"))
#Q2 Create a program that uses match-case to print the days of the week based on user input (1 for Monday, 2 for Tuesday, etc.).
def days_week(a):
  match a:
    case 1:
      return "monday"
    case 2:
      return "tuesday"
print(days_week(1))
#Q3 Write a program using match-case to categorize a given character:
# Vowel
# Consonant
# Digit
# Special character
def char_cat(a):
  match a:
    case "a":
      return "vowel"
    case "b":
      return "consonant"
print(char_cat("a"))
