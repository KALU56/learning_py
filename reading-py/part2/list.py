#Q1. Create a list of 7 fruits and print it
fruit=["apple","banana","cherry","date","elderberry","fig","grape"]
print(fruit)
#Q2Access and print the last element in the list ["apple", "banana", "cherry"] .
fruit1=["apple","banana","cherry"]
print(fruit1[-1])

#Q3. Add "kiwi" to the list ["apple", "banana"] and print the updated list.
fruit1.append('kiwi')
print(fruit1)
#Q4. Remove "banana" from the list ["apple", "banana", "cherry"] .
fruit1.remove('banana')
#5. Use a loop to print each item in the list ["cat", "dog", "fish"] 
animal=["cat","dog","fish"]
for i in animal:
    print(i)
##medium
#Q1. Create a list of numbers from 1 to 10 and print only the even numbers.
num=[1,2,3,4,5,6,7,8,9,10]
for i in num:
    if i%2==0:
        print(i)
#Q2. Reverse the list ["red", "green", "blue"] 
color=["red","green","blue","yellow"]
color.reverse()
print(color)
#Q3. Combine the two lists [1, 2, 3] and [4, 5, 6] into one list
num1=[1,2,3]
num2=[4,5,6]
num1.extend(num2)
print(num1)
#Q4. Modify the list [5, 10, 15] by replacing 10 with 12 .
nums=[5,10,15]
nums[1]=12
print(nums) 
#Q5. Find the length of the list ["a", "b", "c", "d"] and print it.
alpha=["a","b","c","d"]
print(len(alpha))
##hard
#Q1.1. Use list comprehension to generate a list of squares for numbers from 1 to 10, excluding numbers divisible by 3.
numbers=[i**2 for i in range(1,11)if i%3!=0]
print(numbers)
#Q2. Create a nested list (matrix) and print the second row.
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix)
#Q3. Write a program to find duplicates in a list [1, 2, 3, 2, 4, 5, 1] .
list1=[1,2,3,2,4,5,1]
list2=[]
for i in list1:
    if list1.count(i)>1:
        if i not in list2:
            list2.append(i)
print(list2)
#Q4. Write a program to find the common elements between two lists [1, 2, 3] and [3, 4, 5] .
list3=[1,2,3]
list4=[3,4,5]
list5=[]
for i in list3:
    if i in list4:
        list5.append(i)
print(list5)
#Q5. Write a program to remove duplicates from a list [1, 2, 3, 2, 4, 5, 1] .
list6=[1,2,3,2,4,5,1]
list7=[]
for i in list6:
    if list6.count(i)==1:
        list7.append(i)
print(list7)
#Q6. Sort the list [3, 1, 4, 1, 5, 9] in descending order
list8=[3,1,4,1,5,9]
list8.sort(reverse=True)
print(list8)
#
list9=[1,2]
list10=[3,4]
list11=[5,6]
list12=[]
list12.extend(list9)
list12.extend(list10)
list12.extend(list11)
print(list12)