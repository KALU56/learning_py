import register  # Import register module
import appointment  # Import appointment module

def donor_welcome():
    while True:  # Loop to keep the menu running until user exits
        print("\nWelcome to Donor Bank X!")
        print("-------------------------")
        print("1. Register a New Donor")
        print("2. Schedule an Appointment")
        print("3. View Medical Information")
        print("4. Exit")
        
        option = input("Please choose an option (1, 2, 3, 4): ").strip()
        
        if option == "1":
            register.register()  # Call the register function from register.py
        elif option == "2":
            appointment.appointment()  # Call the appointment function from appointment.py
        elif option == "3":
            print("Medical Information feature is under development.")
        elif option == "4":
            print("Exiting... Goodbye!")
            break  # Exit the loop and program
        else:
            print("Invalid choice! Please try again.")

# Run the welcome menu
donor_welcome()
