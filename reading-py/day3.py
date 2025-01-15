#Q1
age=16
#Q2
height=5.7
#Q3
complex_num=3+4j
#Q4
base=int(input("enter the base:"))
height=int(input("enter the height:"))
area=0.5*base*height
print(f"the area of the triangle is {area}")
#Q5
side_a=int(input("enter the side-a:"))
side_b=int(input("enter the side-b:"))
side_c=int(input("enter the side-c:"))
perimeter=side_a+side_b+side_c
print(f"the perimeter of the triangle is {perimeter}")
#Q6
length=int(input("enter the length:"))
width=int(input("enter the width:"))
perimeter=2*(length+width)
print(f"the perimeter of the rectangle is {perimeter}")
#Q7
radius=int(input("enter the radius:"))
area=3.14*radius*radius
print(f"the area of the circle is {area}")
#Q8
# Define the equation coefficients
slope_line = 2  # slope (coefficient of x)
b = -2  # y-intercept (constant term)

# Calculate y-intercept
y_intercept = (0, b)  # x = 0

# Calculate x-intercept
# At y = 0, solve for x: 0 = m*x + b => x = -b/m
x_intercept = (-b / slope_line, 0)  # y = 0

# Display the results
print(f"slope_line: {slope_line}")
print(f"x-Intercept: {x_intercept}")
print(f"y-Intercept: {y_intercept}")
#Q9
import math
x1, y1 = 2, 2
x2, y2 = 6, 10

slope_points = (y2 - y1) / (x2 - x1)
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


print(f"Slope between points: {slope_points}")
print(f"Euclidean Distance: {distance:.3f}")
#Q10
print(f"are the slopes equal?{"yes" if slope_line==slope_points else "no"}")
#Q22
lived_year=int(input("enter the year you lived:"))
seconds=lived_year*365*24*60*60
print(f"the seconds you lived is {seconds}")
#Q23
# Print the header
print("Number\t1\tNumber^2\tNumber^3")

# Loop through numbers 1 to 5
for number in range(1, 6):
    print(f"{number}\t1\t{number**2}\t{number**3}")
    

