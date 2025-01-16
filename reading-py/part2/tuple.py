##Easy Exercises
#Q1. Create a tuple of five colors and print it
color=("red","blue","green","yellow","black")
print(color)
#Q2. Print the item at index 2 in the tuple ("apple", "banana", "cherry") .
fruit=("apple","banana","cherry")
print(fruit[2]) 
#Q3. Slice the tuple ("red", "blue", "green", "yellow", "purple") to get the middle three items.
color1=("red","blue","green","yellow","purple")
print(color1[1:4])
#Q4. Find the index of "apple" in the tuple ("apple", "banana", "cherry") .
fruit1=("apple","banana","cherry")
print(fruit1.index('apple'))
#Q5.Check if "orange" exists in the tuple ("red", "blue", "green") .
color2=("red","blue","green")
"orange" in color2
print(color2)
#Q6. Use a loop to print all items in the tuple ("apple", "banana", "cherry") .
fruit2=("apple","banana","cherry")
for i in fruit2:
    print(i)
##Medium Exercises
#Q1. Create two tuples and merge them into one
num1=(1,2,3)
num2=(4,5,6)
num3=num1+num2
print(num3)
#Q2. Write a program to count how many times a specific item appears in a tuple.
num4=(1,2,3,2,4,5,1)
print(num4.count(1))
#Q3. Extract only the numeric items from a tuple ("apple", 42, 3.14, "banana", 7) 
num5=("apple",42,3.14,"banana",7)
num6=[]
for i in num5:
    if isinstance(i,(int,float)):
        num6.append(i)
print(num6)
#Q4. Create a tuple of numbers from 1 to 5 and print the sum of all items.
num7=(1,2,3,4,5)
print(sum(num7))
#Q5. Write a program to test if every element of a tuple is the same type.
num8=(1,2,3,4,5)
print(all(isinstance(i,int) for i in num8))



