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
