#break: Exits the loop prematurely.
for i in range(1, 6):
    if i == 3:
        break
    print(i)
# Output: 1 2
#continue: Skips the current iteration and moves to the next one.
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
# Output: 1 2 4 5
#else with for: Executes if the loop completes normally (without break).
for i in range(3):
    print(i)
else:
    print("Loop completed!")
# Output: 0 1 2 Loop completed!
####pattern
# 1. Pyramid Pattern
rows = 5
for i in range(1, rows + 1):
    print("*" * i)
# 2. Inverted Pyramid Pattern
rows = 5
for i in range(rows, 0, -1):
    print("*" * i)
# 3. Right-Aligned Triangle
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * i)
# 4. Number Pyramid
rows = 5
for i in range(1, rows + 1):
    print("".join(str(j) for j in range(1, i + 1)))

# 5. Hollow Pyramid Pattern
for i in range(1,6):
  for j in range(1,6):
    if i==1 or i==5 or j==1 or j==5:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print() 
# 6.Diamond Pattern
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
# 5. Number Pyramid
rows = 5
for i in range(1, rows + 1):
    print("".join(str(j) for j in range(1, i + 1)))

# 7. Hollow Diamond Pattern
