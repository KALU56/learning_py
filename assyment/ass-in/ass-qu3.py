import math

def find_roots(a, b, c):
    # Calculate the discriminant (b^2 - 4ac)
    discriminant = b**2 - 4*a*c
  
    
    if discriminant > 0:
        # Two real and distinct roots
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f"The roots are real and distinct: {root1} and {root2}")
    
    elif discriminant == 0:
        # One real root (repeated root)
        root = -b / (2 * a)
        print(f"The root is real and repeated: {root}")
    
    else:
        # Complex roots
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        print(f"The roots are complex: {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i")

# Get user input for coefficients a, b, and c
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Call the function to find the roots
find_roots(a, b, c)
