# Global lists and dictionaries for donors, donations, etc.
donors = []
donation_history = {}
medical_history = {}
pending_donations = []  # List to store pending donations
approved_donations = []  # List to store approved donations

# Simulate a dictionary for registered users (username and password)
user_credentials = {}

def register_donor():
    print("\n--- Donor Registration ---")
    
    # Collecting donor information (with validation)
    name = input("Enter your name: ").strip()
    if not name:
        print("Invalid input. Name cannot be empty.")
        return

    father_name = input("Enter your father's name: ").strip()
    if not father_name:
        print("Invalid input. Father's name cannot be empty.")
        return

    surname = input("Enter your surname: ").strip()
    if not surname:
        print("Invalid input. Surname cannot be empty.")
        return

    while True:
        try:
            age = input("Enter your age: ").strip()
            if not age or int(age) <= 0:
                print("Invalid input. Age must be a positive number.")
                continue
            age = int(age)  # Convert to integer
            break
        except ValueError:
            print("Invalid input. Age must be a number.")

    while True:
        try:
            weight = float(input("Enter your weight in kilos: "))
            if weight < 50:
                print("\nSorry, you must weigh at least 50 kilos to donate blood.")
                continue
            break
        except ValueError:
            print("\nInvalid input. Weight must be a number.")
            continue

    # Optional medical info
    is_smoker = input("Are you a smoker? (yes/no): ").lower() == "yes"
    
    # Blood type (optional)
    blood_type = input("Enter your blood type (e.g., A+, O-), or type 'unknown' if you don't know: ").upper()
    if blood_type not in ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-", "unknown"]:
        print("Invalid blood type input. Defaulting to 'unknown'.")
        blood_type = "unknown"

    # HIV status (optional)
    hiv_status = input("Do you have HIV? (yes/no/unknown): ").lower()
    if hiv_status not in ["yes", "no", "unknown"]:
        print("Invalid HIV status input. Defaulting to 'unknown'.")
        hiv_status = "unknown"

    phone = input("Enter your phone number: ").strip()
    if not phone:
        print("Invalid input. Phone number cannot be empty.")
        return

    email = input("Enter your email address: ").strip()
    if not email:
        print("Invalid input. Email address cannot be empty.")
        return

    while True:
        username = input("Create a username: ").strip()
        if username in user_credentials:
            print("Username already taken. Please choose another.")
        else:
            break
    
    password = input("Create a password: ").strip()

    donor = {
        "name": name,
        "father_name": father_name,
        "surname": surname,
        "age": age,
        "weight": weight,
        "phone": phone,
        "email": email,
        "blood_type": blood_type,
        "is_smoker": is_smoker,
        "hiv_status": hiv_status,
        "status": "pending",  # Status for approval
        "username": username,  # Added username
        "password": password   # Added password
    }

    # Store donor details
    donors.append(donor)
    user_credentials[username] = password  # Store username and password for login
    pending_donations.append(donor)

    print(f"\nDonor {name} registered successfully. Awaiting supervisor approval.")
    print("Note: If you selected 'unknown' for blood type or HIV status, please ensure to update this information later.")

def login():
    print("\n--- Login ---")
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()
    
    if username in user_credentials and user_credentials[username] == password:
        print(f"Login successful! Welcome {username}.")
        return username
    else:
        print("Invalid username or password. Please try again.")
        return None

def supervisor_menu():
    while True:
        print("\n--- Supervisor Menu ---")
        print("1. Review Pending Donations")
        print("2. View All Donors")
        print("3. Manage Appointments")
        print("4. Send Medical History")
        print("5. Return to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            review_pending_donations()
        elif choice == "2":
            view_all_donors()
        elif choice == "3":
            manage_appointments()
        elif choice == "4":
            send_medical_history()
        elif choice == "5":
            break
        else:
            print("\nInvalid choice. Please try again.")

def view_all_donors():
    print("\n--- View All Donors ---")
    if not donors:
        print("No donors registered.")
        return
    
    for i, donor in enumerate(donors, 1):
        print(f"\nDonor {i}:")
        print(f"Name: {donor['name']}")
        print(f"Age: {donor['age']}")
        print(f"Weight: {donor['weight']} kg")
        print(f"Blood Type: {donor['blood_type']}")
        print(f"Phone: {donor['phone']}")
        print(f"Email: {donor['email']}")
        print(f"Status: {donor['status']}")
        print(f"Smoker: {'Yes' if donor['is_smoker'] else 'No'}")
        print(f"HIV Status: {donor['hiv_status']}")

def review_pending_donations():
    print("\n--- Review Pending Donations ---")
    pending = [d for d in donors if d["status"] == "pending"]
    
    if not pending:
        print("No pending donations to review.")
        return

    for i, donor in enumerate(pending, 1):
        print(f"\nDonor {i}:")
        print(f"Name: {donor['name']}")
        print(f"Age: {donor['age']}")
        print(f"Weight: {donor['weight']} kg")
        print(f"Medical History: {medical_history.get(donor['email'], 'No medical history yet')}")
        
        choice = input("Approve donation? (yes/no): ")
        if choice.lower() == 'yes':
            donor['status'] = 'approved'
            approved_donations.append(donor)
            pending_donations.remove(donor)
            print("Donation approved!")
        else:
            donor['status'] = 'rejected'
            pending_donations.remove(donor)
            print("Donation rejected.")

def manage_appointments():
    print("\n--- Manage Appointments ---")
    for email, appointments in donation_history.items():
        if appointments:
            donor = next((d for d in donors if d['email'] == email), None)
            if donor:
                print(f"\nDonor: {donor['name']}")
                for apt in appointments:
                    print(f"Date: {apt['date']}")
                    if 'status' not in apt:
                        choice = input("Accept appointment? (yes/no): ")
                        apt['status'] = 'accepted' if choice.lower() == 'yes' else 'rejected'
                        print(f"Appointment {apt['status']}!")

def send_medical_history():
    print("\n--- Send Medical History ---")
    email = input("Enter donor's email: ").strip()
    
    if email in medical_history:
        notes = input("Enter medical notes after donation: ").strip()
        medical_history[email]['post_donation_notes'] = notes
        print("Medical history updated successfully!")
    else:
        print("Donor not found.")

def donor_menu():
    while True:
        print("\n--- Donor Menu ---")
        print("1. Login as Donor")
        print("2. Register as a Donor")
        print("3. Return to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = login()
            if username:  # If login is successful
                print(f"Welcome back, {username}")
                # Proceed to donor-specific options (e.g., appointment, donation history)
                break
        elif choice == "2":
            register_donor()
        elif choice == "3":
            break
        else:
            print("\nInvalid choice. Please try again.")

def main():
    while True:
        print("\n--- Blood Bank Registration System ---")
        print("1. Donor Menu")
        print("2. Supervisor Menu")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            donor_menu()
        elif choice == "2":
            supervisor_menu()
        elif choice == "3":
            print("\nExiting the system. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
