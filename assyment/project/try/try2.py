class Donor:
    def __init__(self, name, email, phone, address, blood_type, gender, date_of_birth):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.blood_type = blood_type
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.donation_history = []  # List to store donation records
        self.eligibility_date = None

    def update_details(self, email=None, phone=None, address=None):
        if email:
            self.email = email
        if phone:
            self.phone = phone
        if address:
            self.address = address

    def add_donation_record(self, date, amount):
        self.donation_history.append({"date": date, "amount": amount})
        self.update_eligibility_date(date)

    def update_eligibility_date(self, last_donation_date):
        from datetime import datetime, timedelta
        recovery_period = timedelta(days=56)  # Typically 8 weeks
        self.eligibility_date = datetime.strptime(last_donation_date, "%Y-%m-%d") + recovery_period

    def view_donation_history(self):
        return self.donation_history


class Supervisor:
    def __init__(self, username, password):
        self.username = username
        self.password = password  # In real systems, passwords should be hashed

    def verify_donor_eligibility(self, donor):
        from datetime import datetime
        if donor.eligibility_date and datetime.now() < donor.eligibility_date:
            return False, f"Donor is not eligible until {donor.eligibility_date.strftime('%Y-%m-%d')}"
        return True, "Donor is eligible."

    def schedule_appointment(self, donor, date):
        is_eligible, message = self.verify_donor_eligibility(donor)
        if is_eligible:
            return f"Appointment scheduled for {donor.name} on {date}."
        return message

    def record_donation(self, donor, date, amount):
        is_eligible, message = self.verify_donor_eligibility(donor)
        if is_eligible:
            donor.add_donation_record(date, amount)
            return f"Donation of {amount} ml recorded for {donor.name} on {date}."
        return message


# Example Usage
if __name__ == "__main__":
    from datetime import datetime

    # Input donor details
    print("--- Donor Registration ---")
    name = input("Enter Donor Name: ")
    email = input("Enter Donor Email: ")
    phone = input("Enter Donor Phone: ")
    address = input("Enter Donor Address: ")
    blood_type = input("Enter Donor Blood Type: ")
    gender = input("Enter Donor Gender: ")
    date_of_birth = input("Enter Donor Date of Birth (YYYY-MM-DD): ")

    donor = Donor(
        name=name,
        email=email,
        phone=phone,
        address=address,
        blood_type=blood_type,
        gender=gender,
        date_of_birth=date_of_birth
    )

    # Input supervisor details
    print("--- Supervisor Login ---")
    username = input("Enter Supervisor Username: ")
    password = input("Enter Supervisor Password: ")

    supervisor = Supervisor(username=username, password=password)

    # Supervisor actions
    while True:
        print("\n--- Supervisor Menu ---")
        print("1. Schedule Appointment")
        print("2. Record Donation")
        print("3. View Donor History")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter Appointment Date (YYYY-MM-DD): ")
            print(supervisor.schedule_appointment(donor, date))

        elif choice == "2":
            date = input("Enter Donation Date (YYYY-MM-DD): ")
            amount = int(input("Enter Donation Amount (ml): "))
            print(supervisor.record_donation(donor, date, amount))

        elif choice == "3":
            print("--- Donation History ---")
            for record in donor.view_donation_history():
                print(record)

        elif choice == "4":
            print("Exiting Supervisor Menu.")
            break

        else:
            print("Invalid choice. Please try again.")
