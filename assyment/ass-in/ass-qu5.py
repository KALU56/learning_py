def greet_and_classify_age(age):
    if age <= 18:
        print(f"Hello! You are a Child, and you are {age} years old.")
    elif age>18 and age<=35:
        print(f"Hello! You are Young, and you are {age} years old.")
    else:
        print(f"Hello! You are an Elder, and you are {age} years old.")

# Accept user input for age
age = int(input("Please enter your age: "))

# Call the function to greet and classify
greet_and_classify_age(age)
