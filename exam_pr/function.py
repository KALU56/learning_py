
 #
def greet(name):
  return f"Hello, {name}!"

print(greet("Alice"))
# Examples
# 1. Calculate the Area of a Circle
import math
def area_of_circle(radius):
  return math.pi * radius ** 2

print(area_of_circle(5))  

# 2. Find the Largest Number
def find_largest_number(*numbers):
  return max(numbers)
numbers=[]
n=int(input("Enter the number of elements: "))
for i in range(n):
  numbers.append(int(input("Enter the number: ")))
print(find_largest_number(numbers))

# 3. Check if a Number is Prime
def is_prime(number):
  if number <= 1:
    return False
  for i in range(2, number):
    if number % i == 0:
      return False
  return True
print(is_prime(11))

# 4. Calculate the Factorial of a Number
def factorial(number):
  if number == 0:
    return 1
  return number * factorial(number - 1)
print(factorial(5))

# 5. Calculate the Fibonacci Sequence
def fibonacci(n):
  if n <= 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(10))
# 6. grade
def grade(score):
  if score >= 90:
    return "A"
  elif score >= 80:
    return "B"
  else:
    return "C"
score=int(input("Enter the score: "))
print(grade(score))
# 7. Calculate the Sum of Digits
def sum_of_digits(number):
  return sum(int(digit) for digit in str(number))
print(sum_of_digits(12345))
# 8. Check if a String is Palindrome
def is_palindrome(string):
  return string == string[::-1]
print(is_palindrome("racecar"))
