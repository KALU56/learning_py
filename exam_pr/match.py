#1. Matching Days of the Week
day=input("enter your day")
match day:
  case "morning":
    print("good morning")
  case "afternoon":
    print("good afternoon")
  case "evening":
    print("good evening")
  case _:
    print("invalid")
#2. Matching Months of the Year
month=input("enter your month")
match month:
  case "january":
    print("january")
  case "february":
    print("february")
  case _:
    print("invalid")
  

#3 Grading System
score= int(input("enter your score: "))
match score:
  case n if n >= 90:
    print("A")
  case n if 80 <= n < 90:
    print("Grade: B")
  case n if 70 <= n < 80:
    print("Grade: C")
  case n if 60 <= n < 70:
    print("Grade: D")
  case _:
    print("Grade: F")
#5 ATM Withdrawal System
balance=int(input("enter your balance: "))
withdrawal=int(input("enter your withdrawal: "))
match balance:
  case n if n>=withdrawal:
    print("withdrawal successful")
  case _:
    print("insufficient balance") 
##
import math
area=input("enter your want to calculat area (circle,rectangle,trangel: )")
if area=="circle:":
  raduis=float(input("enter the radius of the circle: "))
  resule=math
 #6 file operation
file=open("file.txt","r")
content=file.read()
match content:
  case n if n=="":
    print("file is empty")
  case _:
    print("file is not empty")

#7 3. Shape Detection
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