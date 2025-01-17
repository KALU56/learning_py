with open("file.txt", "r") as file:
   lines=file.readlines()
for line in lines:
   print("hello,",line.strip())