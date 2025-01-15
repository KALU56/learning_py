# # def area_circle(num):
  
# #   aree=2*3.14*num
# #   print(area)
# # num1=input("please enter the num : ")
# # area_circle(num)
# def area_circle(radius):
#     # Calculate the area using the correct formula
#     area = 3.14 * radius**2
#     print(f"The area of the circle with radius {radius} is: {area}")

# # Get input from the user and convert it to a float
# num = float(input("Please enter the radius of the circle: "))

# # Call the function with the user input
# area_circle(num)
import math

def area_circle(radius):
    # Calculate the area using math.pi for better accuracy
    area = math.pi * radius**2
    print(f"The area of the circle with radius {radius} is: {area}")

# Get input from the user and convert it to a float
num = float(input("Please enter the radius of the circle: "))

# Call the function with the user input
area_circle(num)

