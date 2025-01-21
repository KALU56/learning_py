# Global lists and dictionaries for donors, donations, etc.
donors = []
donation_history = {}
medical_history = {}
pending_donations = []  # List to store pending donations
approved_donations = []  # List to store approved donations

def register_donor():
    print("\n--- Donor Registration ---")
    # Collecting donor information
    name = input("Enter your name: ")
    father_name = input("Enter your father's name: ")
    surname = input("Enter your surname: ")
    age = int(input("Enter your age: "))
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
    hiv_status = input("Do you have HIV? (yes/no): ").lower() == "yes"
    phone = input("Enter your phone number: ")
    email = input("Enter your email address: ")
    blood_type = input("Enter your blood type (e.g., A+, O-): ")

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
        "status": "pending"  # Status for approval
    }

    donors.append(donor)
    pending_donations.append(donor)
    print(f"\nDonor {name} registered successfully. Awaiting supervisor approval.")

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
        print(f"HIV Status: {'Yes' if donor['hiv_status'] else 'No'}")

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
    email = input("Enter donor's email: ")
    
    if email in medical_history:
        notes = input("Enter medical notes after donation: ")
        medical_history[email]['post_donation_notes'] = notes
        print("Medical history updated successfully!")
    else:
        print("Donor not found.")

def donor_menu():
    while True:
        print("\n--- Donor Menu ---")
        print("1. Register as a Donor")
        print("2. Schedule an Appointment")
        print("3. View Donation History")
        print("4. View Medical History")
        print("5. Return to Main Menu")

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
            break
        else:
            print("\nInvalid choice. Please try again.")

def schedule_appointment():
    print("\n--- Schedule an Appointment ---")
    donor_email = input("Enter your email to schedule an appointment: ")
    donor = next((d for d in donors if d['email'] == donor_email), None)
    if donor:
        date = input("Enter appointment date (YYYY-MM-DD): ")
        if donor_email not in donation_history:
            donation_history[donor_email] = []
        donation_history[donor_email].append({"date": date, "status": "pending"})
        print(f"Appointment scheduled for {donor['name']} on {date}.")
    else:
        print("Donor not found.")

def view_donation_history():
    email = input("Enter your email to view donation history: ")
    if email in donation_history:
        print(f"Donation History for {email}:")
        for apt in donation_history[email]:
            print(f"Date: {apt['date']} - Status: {apt['status']}")
    else:
        print("No donation history found.")

def view_medical_history():
    email = input("Enter your email to view medical history: ")
    if email in medical_history:
        print(f"Medical History for {email}:")
        print(f"Pre-donation Notes: {medical_history[email].get('pre_donation_notes', 'None')}")
        print(f"Post-donation Notes: {medical_history[email].get('post_donation_notes', 'None')}")
    else:
        print("No medical history found.")

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
