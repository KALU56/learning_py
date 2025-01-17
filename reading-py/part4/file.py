# name=input ("Enter your name: ")
# file=open('file.txt','a')
# file.write(f"{name}/n")
# file.close()
name=input("what is your name?")
with open('file.txt','a') as file:
    file.write(f"{name}\n")