try:
    num=int(input("enter the num: "))
    num2=int(input("enter the number2: "))
    opprater=input("enter the oprater: ")
    match opprater:
        case "+":
            sum=num+num2
            print(f"{num}+{num2}= {sum}")
        case "-":
            s=num-num2
            print(f"{num}-{num2}= {s}")
        case "/":
            d=num/num2
            print(f"{num}/{num2}= {d}")
             
        case "*":
            p=num*num2
            print(f"{num}*{num2}= {p}")
        case _:
            print("invalid")
except ValueError:
    print("invalid input")
except ZeroDivisionError:
    print("invalid input")



# #try-except
# try:
#     num = int(input("Enter a number: "))
#     print(f"You entered: {num}")
# except ValueError:
#     print("Invalid input! Please enter a valid number.")
# #Handling Multiple Exceptions
# try:
#     num = int(input("Enter a number: "))
#     print(f"You entered: {num}")
# except ValueError:
#     print("Invalid input! Please enter a valid number.")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")

# ##
# try:
#     age=int(input("Enter your age: "))
#     if age<0:
#         raise ValueError("Age cannot be negative")
# except ValueError as e:
#     print(f"Error: {e}")
# ## examples
# #1File Handling with Try-Except
# try:
#     with open("file.txt","r") as file:
#         data=file.read()
#         print(data)
# except FileNotFoundError:
#     print("File not found")
# #2.Input Validation
# try:
#     num=int(input("Enter a number: "))
#     print(f"You entered: {num}")
# except ValueError:
#     print("Invalid input! Please enter a valid number.")
# #3.Network Operations
# try:
#     import requests
#     response = requests.get("https://example.com")
#     print(response.content)
# except requests.exceptions.RequestException as e:
#     print(f"Network error: {e}")
# #4.Custom Exceptions
# class CustomException(Exception):
#     def __init__(self,message):
#         self.message=message
#         super().__init__(self.message)
# try:
#     raise CustomException("This is a custom exception")
# except CustomException as e:
#     print(f"Custom exception: {e}")

