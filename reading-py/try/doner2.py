import re
from datetime import datetime

donors = []
donation_history = {}
medical_history = {}

def save_to_file():
    with open("registration.txt", "w") as file:
        for donor in donors:
            file.write(f"Name: {donor['name']}, Father Name: {donor['father_name']}, Surname: {donor['surname']}, Age: {donor['age']}, Phone: {donor['phone']}, Email: {donor['email']}, Blood Type: {donor['blood_type']}, Smoker: {donor['is_smoker']}, HIV Status: {donor['hiv_status']}\n")

def register_donor():
    print("\n--- Donor Registration ---")
    while True:
        name = input("Enter your Name: ")
        if not name.strip():
            print("\nInvalid input. Name cannot be empty.")
            continue
        break

    while True:
        father_name = input("Enter your Father's Name: ")
        if not father_name.strip():
            print("\nInvalid input. Father's Name cannot be empty.")
            continue
        break

    while True:
        surname = input("Enter your Surname: ")
        if not surname.strip():
            print("\nInvalid input. Surname cannot be empty.")
            continue
        break

    while True:
        try:
            age = int(input("Enter your Age: "))
            if age <= 18:
                print("\nSorry, you must be older than 18 to register.")
                continue
        except ValueError:
            print("\nInvalid input. Age must be a number.")
            continue
        break

    while True:
        phone = input("Enter your Phone Number (start with 09 or 07 and 10 digits): ")
        if not re.fullmatch(r"(09|07)\d{8}", phone):
            print("\nInvalid phone number format. Please try again.")
            continue
        break

    while True:
        email = input("Enter your Email (must end with @gmail.com): ")
        if not email.endswith("@gmail.com"):
            print("\nInvalid email format. Must end with @gmail.com. Please try again.")
            continue
        if any(donor["email"] == email for donor in donors):
            print("\nThis email is already registered. Please enter another email.")
            continue
        break

    print("\nOptional Information:")
    print("1. Fill optional information")
    print("2. Skip optional information")
    optional_choice = input("Enter your choice: ")

    blood_type = ""
    is_smoker = ""
    hiv_status = ""

    if optional_choice == "1":
        blood_type = input("Enter your Blood Type (optional): ")
        is_smoker = input("Are you a smoker? (yes/no, optional): ")
        hiv_status = input("HIV status (positive/negative, optional): ")

    donor = {
        "name": name,
        "father_name": father_name,
        "surname": surname,
        "age": age,
        "phone": phone,
        "email": email,
        "blood_type": blood_type,
        "is_smoker": is_smoker,
        "hiv_status": hiv_status,
    }

    donors.append(donor)
    donation_history[email] = []
    medical_history[email] = {
        "blood_type": blood_type,
        "is_smoker": is_smoker,
        "hiv_status": hiv_status,
    }

    save_to_file()
    print("\nRegistration Successful!")

def schedule_appointment():
    print("\n--- Schedule an Appointment ---")
    email = input("Enter your registered email: ")

    if email not in donation_history:
        print("\nEmail not found. Please register first.")
        return

    while True:
        date_str = input("Enter the date for the appointment (YYYY-MM-DD): ")
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
            if date <= datetime.now().date():
                print("\nInvalid date. Appointments must be scheduled for future dates. Please try again.")
                continue
        except ValueError:
            print("\nInvalid date format. Please use YYYY-MM-DD.")
            continue
        break

    donation_history[email].append({"date": date_str})
    print("\nAppointment Scheduled Successfully!")

def view_donation_history():
    print("\n--- Donation History ---")
    email = input("Enter your registered email: ")

    if email not in donation_history:
        print("\nEmail not found. Please register first.")
        return

    history = donation_history[email]
    if not history:
        print("\nNo donation history found.")
    else:
        print("\nDonation History:")
        for record in history:
            print(f"- {record['date']}")

def view_medical_history():
    print("\n--- Medical History ---")
    email = input("Enter your registered email: ")

    if email not in medical_history:
        print("\nEmail not found. Please register first.")
        return

    history = medical_history[email]
    print("\nMedical History:")
    for key, value in history.items():
        print(f"- {key.replace('_', ' ').capitalize()}: {value}")

def main():
    while True:
        print("\n--- Blood Bank Registration System ---")
        print("1. Register as a Donor")
        print("2. Schedule an Appointment")
        print("3. View Donation History")
        print("4. View Medical History")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_donor()
        elif choice == "2":
            schedule_appointment()
        elif choice == "3":
            view_donation_history()
        elif choice == "4":
            view_medical_history()
        elif choice == "5":
            print("\nExiting the system. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
