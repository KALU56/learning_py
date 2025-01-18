import json
from datetime import datetime

# File Paths
DATA_FILE = "data/blood_bank_data.json"

# Helper Functions
def load_data():
    """Load data from JSON file."""
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {
            "users": [],
            "blood_inventory": {},
            "appointments": [],
            "messages": []
        }

def save_data(data):
    """Save data to JSON file."""
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

# Login System
def login(username, password):
    """Authenticate user and return role (supervisor/donor)."""
    data = load_data()
    for user in data["users"]:
        if user["username"] == username and user["password"] == password:
            return user["role"]
    return None

# Supervisor Dashboard
def supervisor_dashboard():
    """Display Supervisor functionalities."""
    data = load_data()

    def view_blood_inventory():
        print("\nBlood Inventory:")
        for blood_type, count in data["blood_inventory"].items():
            print(f"  {blood_type}: {count} units")

    def view_appointments():
        print("\nDonor Appointments:")
        for appointment in data["appointments"]:
            print(f"  Donor: {appointment['donor']}, Date: {appointment['date']}, Time: {appointment['time']}")

    def send_message():
        recipient = input("Enter donor username: ")
        message = input("Enter your message: ")
        data["messages"].append({"recipient": recipient, "message": message, "timestamp": datetime.now().isoformat()})
        save_data(data)
        print("Message sent!")

    while True:
        print("\nSupervisor Dashboard")
        print("1. View Blood Inventory")
        print("2. View Appointments")
        print("3. Send Message to Donor")
        print("4. Logout")
        choice = input("Choose an option: ")

        if choice == "1":
            view_blood_inventory()
        elif choice == "2":
            view_appointments()
        elif choice == "3":
            send_message()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")

# Donor Dashboard
def donor_dashboard(username):
    """Display Donor functionalities."""
    data = load_data()

    def view_history():
        print("\nDonation History:")
        for appointment in data["appointments"]:
            if appointment["donor"] == username:
                print(f"  Date: {appointment['date']}, Time: {appointment['time']}")

    def schedule_appointment():
        date = input("Enter preferred date (YYYY-MM-DD): ")
        time = input("Enter preferred time (HH:MM): ")
        data["appointments"].append({"donor": username, "date": date, "time": time})
        save_data(data)
        print("Appointment scheduled!")

    def view_messages():
        print("\nMessages:")
        for message in data["messages"]:
            if message["recipient"] == username:
                print(f"  {message['timestamp']}: {message['message']}")

    while True:
        print("\nDonor Dashboard")
        print("1. View Donation History")
        print("2. Schedule Appointment")
        print("3. View Messages")
        print("4. Logout")
        choice = input("Choose an option: ")

        if choice == "1":
            view_history()
        elif choice == "2":
            schedule_appointment()
        elif choice == "3":
            view_messages()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")

# Main Entry Point
def main():
    """Main function to run the application."""
    while True:
        print("\nBlood Bank System")
        print("1. Login")
        print("2. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            role = login(username, password)

            if role == "supervisor":
                supervisor_dashboard()
            elif role == "donor":
                donor_dashboard(username)
            else:
                print("Invalid credentials. Try again.")

        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
