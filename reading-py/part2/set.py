#Q1. Create a set of five vegetables and print it
veggies={"carrot","beetroot","cabbage","potato","tomato"}
print(veggies)
#Q2. Add "lettuce" to the set
veggies.add('lettuce')
print(veggies)
#Q3. . Use a loop to print each item in the set {"python", "java", "c++"} .
languges={"python","java","c","c++","ruby"}
for i in languges:
    print(i)
#Q4. Remove "ruby" from the set {"python", "java", "c++", "ruby"} .
languges.discard('ruby')
print(languges)
#Q5.
animals={"cat","dog","fish","rabbit","elephant"}
"cat" in animals
print(animals)
#Q6. Check if "cat" is in the set {"dog", "cat", "rabbit"} .
pets={"dog","cat","rabbit"}
"cat" in pets
print(pets)
##Medium Exercises
#Q1. Combine the sets {1, 2, 3} and {3, 4, 5} using union() .
num1={1,2,3}
num2={3,4,5}
num3=num1.union(num2)
print(num3)
#Q2. Find the intersection of the sets {1, 2, 3} and {3, 4, 5} using intersection() .
num4=num1.intersection(num2)
print(num4)
#Q3. Find the difference between the sets {1, 2, 3} and {3, 4, 5} using difference() .
num5=num1.difference(num2)
print(num5)
#Q4. Create a set of numbers from 1 to 5 and remove all items using clear() .
num={1,2,3,4,5}
num.clear()
print(num)
#Q5. Write a program to find duplicates in a list using a set.
list1=[1,2,3,2,4,5,1]
list2=set()
list3=set()
for i in list1:
    if i not in list2:
        list2.add(i)
    else:
        list3.add(i)
print(list3)
##Hard Exercises
#Q1. Write a program to find the symmetric difference between two sets {1, 2, 3} and {3, 4, 5} using symmetric_difference() .
num6={1,2,3}
num7={3,4,5}
num8=num6.symmetric_difference(num7)
print(num8)
#Q2. Use a set to remove duplicate characters from a string.
# Input: "hello"
# Output: {'h', 'e', 'l', 'o'}
string="hello"
string1=set(string)
print(string1)
#Q3.3. Check if the set {1, 2} is a subset of {1, 2, 3} 
num9={1,2}
num10={1,2,3}
num11=num9.issubset(num10)
print(num11)
#Q4. Check if the set {1, 2} is a superset of {1, 2, 3}
num12=num9.issuperset(num10)
print(num12)
#Q5. Write a program to find the union of multiple sets using the union() method.
num13={1,2,3}
num14={3,4,5}
num15={5,6,7}
num16=num13.union(num14,num15)
print(num16)









