#example 1
#1. Count Words in a File
with open("file.txt","r") as file:
  data=file.read()
  words=data.split()
  print(f"the number of words in the file is {len(words)}") 

#2. Search for a Word in a File
with open("file.txt","r") as file:
  data=file.read()
  words=data.split()
  word=input("Enter the word to search: ")
  if word in words:
    print(f"the word {word} is found in the file")
  else:
    print(f"the word {word} is not found in the file")
#3.  Logging Messages
with open("log.txt", "a") as log_file:
    log_file.write("Program executed successfully.\n")
#4. Storing and Retrieving Data
with open("data.txt", "w") as data_file:
    data_file.write("Name: John Doe\nAge: 25\nEmail: john.doe@example.com\n")
with open("data.txt", "r") as data_file:
    print(data_file.read())
