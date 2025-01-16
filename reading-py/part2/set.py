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

