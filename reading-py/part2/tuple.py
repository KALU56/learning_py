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
##Hard Exercises
#Q1. Write a program to convert a tuple to a dictionary.
num9=((1,"apple"),(2,"banana"),(3,"cherry"))
num10=dict(num9)
print(num10)
#Q2. Write a program to reverse a tuple.
num11=(1,2,3,4,5)
num12=tuple(reversed(num11))
print(num12)
#Q3.Convert a tuple of strings to uppercase: ("hello", "world") → ("HELLO", "WORLD") .
string=("hello","world")
string1=tuple(i.upper() for i in string)
print(string1)
#Q4.Write a program to find the unique elements in two tuples.
num13=(1,2,3,4,5)
num14=(4,5,6,7,8)
num15=set(num13).symmetric_difference(set(num14))
print(num15)
#Q5.  Create a tuple of mixed data types and filter out only the string elements
num16=(1,"apple",3.14,"banana",7)
num17=tuple(i for i in num16 if isinstance(i,str))
print(num17)







