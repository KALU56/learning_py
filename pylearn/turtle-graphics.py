# # # # ######### *Basic Turtle Movements* #############
# import turtle  # Import the turtle module

# # Create a screen and turtle object
# screen = turtle.Screen()
# t = turtle.Turtle()

# # Move forward by 100 units
# t.forward(100)

# # Turn left 90 degrees
# t.left(90)

# # Move forward by 100 units again
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)


# # Finish drawing and keep the window open
# turtle.done()
# # # '''
# # Explanation:
# # 1,forward(100): This command moves the turtle forward by 100 units.
# # 2,left(90): This command turns the turtle 90 degrees to the left.
# # 3,forward(100): This command moves the turtle forward again by 100 units.
# # When you run this code, the turtle will move forward 100 units, turn 90 degrees to the left, and move forward another 100 units. This results in a path that looks like an "L" shape.'''
# ########## * Controlling Pen Up/Down * #######

# import turtle  # Import the turtle module

# # Create a screen and turtle object
# screen = turtle.Screen()
# t = turtle.Turtle()

# t.pencolor("yellow")
# t.begin_fill()
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.end_fill()
# t.penup()
# t.pencolor("red")
# t.begin_fill()
# # t.forward(100)
# t.pendown()
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.end_fill()
# t.penup()
# t.pencolor("green")
# t.begin_fill()
# t.forward(100)
# t.pendown()
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.end_fill()
# t.penup()
# t.forward(200)
# t.pendown()
# # Lift the pen so the turtle moves without drawing
# # t.penup()
# # t.forward(100)  # Move forward by 100 units without drawing

# # # Lower the pen so the turtle will start drawing again
# # t.pendown()
# # t.forward(100)  # Move forward by 100 units and draw

# # Finish drawing and keep the window open
# turtle.done()
# # '''Explanation:
# # 1,penup(): This lifts the pen off the screen, so the turtle will move without leaving a trail.
# # 2,forward(100): The turtle moves forward by 100 units, but since the pen is up, no line will be drawn.
# # 3,pendown(): This lowers the pen, so the turtle will start drawing again as it moves.
# # 4,forward(100): The turtle moves forward by 100 units and leaves a trail, creating a line.
# # '''
# # ########## * Changing Pen Color and Style * ########

# import turtle  # Import the turtle module

# # Create a screen and turtle object
# screen = turtle.Screen()
# t = turtle.Turtle()

# # Set the pen color to blue and the pen size (thickness) to 5
# t.pencolor('blue')
# t.pensize(5)

# # Move forward by 100 units and draw a blue line
# t.forward(100)

# # Turn 90 degrees to the left
# t.left(90)

# # Move forward by 100 units and draw another blue line
# t.forward(100)

# # Finish drawing and keep the window open
# turtle.done()

# # '''Explanation:
# # 1,pencolor('blue'): This sets the pen's color to blue. All lines drawn afterward will be in blue.
# # 2,pensize(5): This changes the thickness of the pen to 5. Thicker lines will be drawn.
# # 3,forward(100): The turtle moves forward by 100 units and draws a blue line.
# # 4,left(90): The turtle turns 90 degrees to the left.
# # 5,forward(100): The turtle moves forward by another 100 units and draws another blue line.
# # When you run this code, the turtle will draw two connected lines, each 100 units long, forming a right angle. The lines will be drawn in blue with a pen thickness of 5.
# # '''
# # ############# *  Controlling Turtle’s Speed * ############

# import turtle  # Import the turtle module

# # Create a screen and turtle object
# screen = turtle.Screen()
# t = turtle.Turtle()

# # Set the turtle speed to the fastest
# # t.speed("fastest")
# t.pencolor("blue")
# t.begin_fill()
# t.speed("slow")
# # Draw a circle with a radius of 50 units
# t.circle(100)
# t.end_fill()
# # Finish drawing and keep the window open
# turtle.done()

# # '''Explanation:
# # 1,speed("fastest"): This sets the turtle's speed to the fastest setting. The available options for speed are:
# # "fastest" (turtle moves the quickest)
# # "fast"
# # "normal" (default)
# # "slow"
# # "slowest" (turtle moves the slowest)
# # 2,circle(50): This command draws a circle with a radius of 50 units. The turtle will draw the circle at the fastest possible speed, as specified.
# # When you run this code, the turtle will draw a circle with a radius of 50 units very quickly because of the fastest speed setting.
# # '''
# # #############** Drawing Shapes with Turtle**######
import turtle  # Import the turtle module

# Create a screen and turtle object
screen = turtle.Screen()
t = turtle.Turtle()

# Loop to draw the square
for _ in range(4):  # Repeat 4 times for each side of the square
    t.forward(100)  # Move the turtle forward by 100 units
    t.left(90)
t.penup()
t.right(90) 
t.forward(0)
t.pendown()
for _ in range(4):  # Repeat 4 times for each side of the square
    t.forward(100)  # Move the turtle forward by 100 units
    t.left(90)    # Turn the turtle 90 degrees to the left
t.penup() 
t.forward(100)
t.pendown()
for _ in range(4):  # Repeat 4 times for each side of the square
    t.forward(100)  # Move the turtle forward by 100 units
    t.left(90)
# Finish drawing and keep the window open
turtle.done()
# # '''Explanation of the Full Code:
# # 1,import turtle: This imports the Turtle Graphics library.
# # 2,screen = turtle.Screen(): Initializes a screen object where the turtle will draw.
# # 3,t = turtle.Turtle(): Creates a turtle object that will perform the drawing actions.
# # 4,for _ in range(4):: Repeats the following block 4 times to draw the 4 sides of the square.
# # 5,t.forward(100): Moves the turtle forward by 100 units to draw one side of the square.
# # 6,t.left(90): Turns the turtle 90 degrees to the left, ensuring the correct angle for the square corners.
# # 7,turtle.done(): Ensures the drawing window stays open until you manually close it.
# # When you run this code, the turtle will draw a square with each side being 100 units long. The window will remain open until you close it manually.

# # '''
# # #############**  Adding Color to Shapes***##

# import turtle  # Import the turtle module

# # Create a screen and turtle object
# screen = turtle.Screen()
# t = turtle.Turtle()

# # Set the pen color to red
# # t.pencolor("red")  # Change the pen color to red

# # Start filling the shape with the current pen color
# t.begin_fill("red")

# # Loop to draw a square
# for _ in range(4):  # Repeat 4 times for each side of the square
#     t.forward(100)  # Move the turtle forward by 100 units
#     t.left(90)      # Turn the turtle 90 degrees to the left

# # End filling the shape
# t.end_fill()

# # Finish drawing and keep the window open
# turtle.done()
# # '''
# # Explanation of Changes:
# # 1,t.pencolor("red"): This sets the pen color to red. All subsequent drawing and filling will use this color.
# # 2,t.begin_fill(): Starts filling the shape with the current pen color (which is red).
# # 3,t.end_fill(): Ends the filling process and completes the shape's color fill.
# # Note:
# # You don't need to pass the color to begin_fill() or end_fill(); it will automatically use the current pen color set by pencolor().
# # The result will be a red-filled square.
# # '''
