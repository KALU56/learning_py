#study
#practice problems
#1. Write a program that checks whether a number is positive, negative, or zero.
x=int(input("enter a number:"))
if x>0:
    print("positive")
elif x<0:
    print("negative")
else:
    print("zero")
#2. Create a program that prints "Eligible to vote" if the age is 18 or above, otherwise prints "Noteligible."
age=int(input("enter your age:"))
if age>=18:
    print("Eligible to vote")
else:
    print("Not eligible")
#3. Write a nested if program to check whether a number is divisible by 2 and also by 5.
y=int(input("enter a number:"))
if y%2==0:
    if y%5==0:
        print("divisible by 2 and 5")
    else:
        print("not divisible by 5")
else:
    print("not divisible by 2")
#Practice problems2
#1. Write a for loop to print all even numbers from 1 to 20.
for i in range(1,21):
    if i%2==0:
        print(i)
#2. Use a while loop to calculate the sum of numbers from 1 to 50.
sum=0
i=1
while i<=50:
    sum+=i
    i+=1
print(sum)
#3. Write a program that loops through a list of numbers and prints "Skip" if the number is 5, using
for i in range(1,10):
    if i==5:
        continue
   
    print(i)
#4. Create a program that breaks out of a loop when a randomly generated number is greater than 90.
# Use the random module to generate the number.
# Hint: Use the randint function from the random module to generate a random number.
import random
random_number = random.randint(1, 100)
print(random_number)
while True:
  if random_number>90:
    break
  print(random_number)
  

                       

