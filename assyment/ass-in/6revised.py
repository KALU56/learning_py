import os

# Function to collect application details
def collect_application_details():
    applications = []

    # Position selection using if...else
    print("Welcome! Please select the position you are applying for:")
    print("1. Officer")
    print("2. Software Developer")
    print("3. Sales and Marketing Manager")
    position_choice = input("Enter the number for your position: ")

    if position_choice == '1':
        position = "Officer"
    elif position_choice == '2':
        position = "Software Developer"
    elif position_choice == '3':
        position = "Sales and Marketing Manager"
    else:
        print("Invalid choice! Defaulting to Officer.")
        position = "Officer"

    # Collecting personal details
    name = input("Name: ")

    # Collecting and validating age (must be > 18)
    while True:
        age = input("Age: ")
        if age.isdigit():
            if int(age) > 18:
                break
            else:
                print("Age must be greater than 18!")
        else:
            print("Invalid input! Please enter a number.")

    cgpa = input("CGPA: ")

    # Collecting email with validation
    while True:
        email = input("Email Address (must end with @gmail.com): ")
        if email.endswith('@gmail.com'):
            break
        else:
            print("Invalid email! Please enter a valid Gmail address.")

    # Collecting phone number with validation
    while True:
        phone_number = input("Phone Number (must start with 09 or 07 and be 10 digits): ")
        if phone_number.startswith('09') or phone_number.startswith('07'):
            if len(phone_number) == 10 and phone_number.isdigit():
                break
            else:
                print("Invalid phone number! It must be exactly 10 digits.")
        else:
            print("Invalid phone number! It must start with 09 or 07.")

    # Collecting work experience (mandatory)
    while True:
        work_experience = input("Work Experience (required): ")
        if work_experience.strip():
            break
        else:
            print("Work experience is mandatory!")

    # Collecting optional skills
    skills = input("Skills (optional): ")

    # Collecting the details in a list
    applicant = [name, age, cgpa, position, email, phone_number, work_experience, skills]
    applications.append(applicant)

    return applications

# Function to save details to separate files based on position
def save_to_files(applications):
    for applicant in applications:
        position = applicant[3]
        if position == "Officer":
            filename = "Officer.csv"
        elif position == "Software Developer":
            filename = "Software_Developer.csv"
        elif position == "Sales and Marketing Manager":
            filename = "Sales_and_Marketing_Manager.csv"
        else:
            filename = "Unknown_Position.csv"

        # Write data to the file
        with open(filename, mode='a', newline='') as file:
            if os.stat(filename).st_size == 0:  # Write header if file is empty
                file.write("Name,Age,CGPA,Position,Email,Phone Number,Work Experience,Skills\n")
            file.write(','.join(applicant) + '\n')

    # Save all applicants in an "All" file
    with open("All_applicants.csv", mode='a', newline='') as file:
        if os.stat("All_applicants.csv").st_size == 0:  # Write header if file is empty
            file.write("Name,Age,CGPA,Position,Email,Phone Number,Work Experience,Skills\n")
        for applicant in applications:
            file.write(','.join(applicant) + '\n')

# Function to filter the best applicant
def filter_best_applicant(position):
    if position == "Officer":
        filename = "Officer.csv"
    elif position == "Software Developer":
        filename = "Software_Developer.csv"
    elif position == "Sales and Marketing Manager":
        filename = "Sales_and_Marketing_Manager.csv"
    else:
        print(f"Invalid position: {position}")
        return

    if os.path.exists(filename):
        with open(filename, mode='r') as file:
            lines = file.readlines()

        if len(lines) > 1:  # Check if data exists beyond the header
            applicants = []
            for line in lines[1:]:  # Skip header
                fields = line.strip().split(',')
                if len(fields) == 8:  # Ensure correct format
                    name, age, cgpa, pos, email, phone, work_exp, skills = fields
                    applicants.append({
                        "Name": name,
                        "Age": age,
                        "CGPA": float(cgpa),
                        "Position": pos,
                        "Email": email,
                        "Phone": phone,
                        "Work Experience": work_exp,
                        "Skills": skills
                    })

            # Sort applicants by CGPA (descending)
            applicants.sort(key=lambda x: x["CGPA"], reverse=True)
            best_applicant = applicants[0]

            # Display the best applicant
            print(f"\nBest Applicant for {position}:")
            for key, value in best_applicant.items():
                print(f"{key}: {value}")
        else:
            print(f"There is no data or application for {position}.")
    else:
        print(f"There is no file for {position}. No applications have been submitted yet.")

# Main menu
def main_menu():
    while True:
        print("\nWelcome to the Applicant and HR System")
        print("1. Apply as an Applicant")
        print("2. HR Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            applications = collect_application_details()  # Collect data from applicant
            save_to_files(applications)  # Save data to files
            print("Your application has been submitted!")
        elif choice == '2':
            print("\nHR Options:")
            print("1. View All Applicants")
            print("2. Filter Best Applicant by Position")
            print("3. Return to Main Menu")
            hr_choice = input("Enter your choice: ")

            if hr_choice == '1':
                print("Viewing All Applicants...")
                if os.path.exists("All_applicants.csv"):
                    with open("All_applicants.csv", mode='r') as file:
                        print(file.read())
                else:
                    print("No applicants found.")
            elif hr_choice == '2':
                print("1. Officer")
                print("2. Software Developer")
                print("3. Sales and Marketing Manager")
                position_choice = input("Enter the position: ")
                if position_choice == '1':
                    filter_best_applicant("Officer")
                elif position_choice == '2':
                    filter_best_applicant("Software Developer")
                elif position_choice == '3':
                    filter_best_applicant("Sales and Marketing Manager")
                else:
                    print("Invalid position choice!")
            elif hr_choice == '3':
                break
            else:
                print("Invalid HR choice!")
        elif choice == '3':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

# Run the program
if __name__ == "__main__":
    main_menu()
