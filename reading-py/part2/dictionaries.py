#Q1Create an empty dictionary called dog
dog={}
#Q2Add name, color, breed, legs, and age to the dog dictionary
dog["name"]="dog"
dog["color"]="black"
dog["breed"]=("labrador","pug")
dog["legs"]=4
dog["age"]=1
print(dog)
#Q3Create a student dictionary and add first_name, last_name, age, skills, country, city and address as keys for the dictionary
student={'first_name':'john','last_name':'doe','age':25,'skills':['python','java','c++'],'country':'nigeria','city':'lagos','address':'no 1,ikeja'}
print(student)
#Q4Get the length of the student dictionary
print(len(student))
#Q5Get the value of skills and check the data type, it should be a list
print(student['skills'])
print(type(student['skills']))
#Q6Modify the skills values by adding one or two skills
print(student['skills'].append('ruby'))
print(student['skills'].append('c#'))
print(student)
#Q7Get the dictionary keys as a list
print(student.keys())
#Q8Get the dictionary values as a list
print(student.values())
#Q9Change the dictionary to a list of tuples using items() method 
print(student.items())
#Q10Delete one of the items in the dictionary
del student['address']
print(student)

#Q11Delete the dictionary completely
del student
print(student)

