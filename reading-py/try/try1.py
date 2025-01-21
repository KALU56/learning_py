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
    # Create a donor
    donor = Donor(
        name="John Doe",
        email="john.doe@example.com",
        phone="1234567890",
        address="123 Main St",
        blood_type="O+",
        gender="Male",
        date_of_birth="1990-01-01"
    )

    # Create a supervisor
    supervisor = Supervisor(username="admin", password="password123")

    # Schedule an appointment
    print(supervisor.schedule_appointment(donor, "2025-02-15"))

    # Record a donation
    print(supervisor.record_donation(donor, "2025-01-01", 500))

    # View donation history
    print(donor.view_donation_history())

    # Try scheduling again before eligibility date
    print(supervisor.schedule_appointment(donor, "2025-01-20"))
