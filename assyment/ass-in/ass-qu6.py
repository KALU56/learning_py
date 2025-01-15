import csv
import os

# Function to collect application details
def collect_application_details():
    applications = []

    # Position selection
    print("Welcome! Please select the position you are applying for:")
    print("1. Officer")
    print("2. Software Developer")
    print("3. Sales and Marketing Manager")
    position_choice = input("Enter the number for your position: ")

    positions = {
        '1': "Officer",
        '2': "Software Developer",
        '3': "Sales and Marketing Manager"
    }
    position = positions.get(position_choice, "Officer")  # Default to Officer if invalid

    # Collecting personal details
    name = input("Name: ")

    # Collecting and validating age (must be > 18)
    while True:
        age = input("Age: ")
        if age.isdigit() and int(age) > 18:
            break
        else:
            print("Invalid age! Age must be a number greater than 18.")

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
        if (phone_number.startswith('09') or phone_number.startswith('07')) and len(phone_number) == 10 and phone_number.isdigit():
            break
        else:
            print("Invalid phone number! It must start with 09 or 07 and be exactly 10 digits.")

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
    positions = {
        "Officer": "Officer.csv",
        "Software Developer": "Software_Developer.csv",
        "Sales and Marketing Manager": "Sales_and_Marketing_Manager.csv"
    }

    # Write data to position-based files
    for position, filename in positions.items():
        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            if os.stat(filename).st_size == 0:  # Write header if file is empty
                writer.writerow(["Name", "Age", "CGPA", "Position", "Email", "Phone Number", "Work Experience", "Skills"])
            for applicant in applications:
                if applicant[3] == position:
                    writer.writerow(applicant)

    # Save all applicants in an "All" file
    with open("All_applicants.csv", mode='a', newline='') as file:
        writer = csv.writer(file)
        if os.stat("All_applicants.csv").st_size == 0:  # Write header if file is empty
            writer.writerow(["Name", "Age", "CGPA", "Position", "Email", "Phone Number", "Work Experience", "Skills"])
        writer.writerows(applications)

# Function to filter the best applicant
def filter_best_applicant(position):
    filename = position.replace(" ", "_") + ".csv"
    try:
        if not os.path.exists(filename):
            print(f"There is no file for {position}. No applications have been submitted yet.")
            return

        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            data = list(reader)

            if len(data) <= 1:  # No data except the header
                print(f"There is no data or application for {position}.")
                return

            # Skip the header row
            applicants = []
            for row in data[1:]:
                name, age, cgpa, pos, email, phone, work_exp, skills = row
                applicants.append({
                    "full-Name": name,
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

    except Exception as e:
        print(f"An error occurred while processing {position}: {e}")

# Function to display HR options
def hr_options():
    while True:
        print("\nHR Dashboard:")
        print("1. View all applicants")
        print("2. Filter best applicant by position")
        print("3. Return to Main Menu")
        hr_choice = input("Enter your choice: ")

        if hr_choice == '1':
            view_all_applicants()
        elif hr_choice == '2':
            print("Choose position:")
            print("1. Officer")
            print("2. Software Developer")
            print("3. Sales and Marketing Manager")
            position_choice = input("Enter position: ")

            if position_choice == '1':
                filter_best_applicant("Officer")
            elif position_choice == '2':
                filter_best_applicant("Software Developer")
            elif position_choice == '3':
                filter_best_applicant("Sales and Marketing Manager")
            else:
                print("Invalid choice!")
        elif hr_choice == '3':
            break
        else:
            print("Invalid choice!")

# Function to view all applicants
def view_all_applicants():
    try:
        if not os.path.exists("All_applicants.csv"):
            print("There is no file for all applicants. No applications have been submitted yet.")
            return

        print("\nAll Applicants:")
        with open('All_applicants.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

    except Exception as e:
        print(f"An error occurred while processing all applicants: {e}")

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
            hr_options()  # Show HR options
        elif choice == '3':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

# Run the program
if __name__ == "__main__":
    main_menu()
