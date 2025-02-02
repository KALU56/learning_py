def approve_appointments():
    try:
        with open("appointments.txt", "r") as file:
            appointments = file.read().strip().split("----------------------------------------\n")
        
        pending_appointments = []
        for appointment in appointments:
            if "AppointmentStatus: Scheduled" in appointment:
                pending_appointments.append(appointment)
        
        if not pending_appointments:
            print("No pending appointments to approve or disapprove.")
            return
        
        for index, appointment in enumerate(pending_appointments):
            print(f"\nAppointment {index + 1}:")
            print(appointment.strip())
            
            decision = input("Approve (A), Disapprove (D), or Exit (E) the approval process? (A/D/E): ").strip().upper()
            
            if decision == 'A':
                appointment = appointment.replace("AppointmentStatus: Scheduled", "AppointmentStatus: Approved")
                print("Appointment approved.")
            elif decision == 'D':
                appointment = appointment.replace("AppointmentStatus: Scheduled", "AppointmentStatus: Disapproved")
                print("Appointment disapproved.")
            elif decision == 'E':
                print("Exiting the appointment approval process.")
                break  # Exit the loop immediately
            else:
                print("Invalid input. Skipping this appointment.")
            
            # Update the appointment in the main list if not exiting
            if decision in ['A', 'D']:
                appointments[appointments.index(pending_appointments[index])] = appointment
        
        # Write the updated appointments back to the file only if changes were made
        with open("appointments.txt", "w") as file:
            for appointment in appointments:
                if appointment.strip():  # Avoid writing empty lines
                    file.write(appointment.strip() + "\n----------------------------------------\n")
        
        print("All updates saved successfully!")

    except FileNotFoundError:
        print("No appointments found. Please schedule appointments first.")
    except Exception as e:
        print(f"An error occurred: {e}")
def view_donors():
    try:
        donors_list = []
        with open("donor_registration.txt", "r") as file:
            lines = file.readlines()

            donor_data = {}
            for line in lines:
                line = line.strip()
                if line.startswith("DonorID:"):
                    if donor_data:  # If donor_data is not empty, add the previous donor data to the list
                        donors_list.append(donor_data)
                    donor_data = {"DonorID": line.split(":")[1].strip()}  # Start new donor
                elif line.startswith("FirstName:"):
                    donor_data["FirstName"] = line.split(":")[1].strip()
                elif line.startswith("LastName:"):
                    donor_data["LastName"] = line.split(":")[1].strip()
                elif line.startswith("BloodType:"):
                    donor_data["BloodType"] = line.split(":")[1].strip()
                elif line.startswith("DateOfBirth:"):
                    donor_data["DateOfBirth"] = line.split(":")[1].strip()
                # Add more fields as needed
            if donor_data:  # Add the last donor after finishing reading the file
                donors_list.append(donor_data)

        # Now you can access donors using indexes
        if donors_list:
            for donor in donors_list:
                print(f"Donor ID: {donor['DonorID']}, Name: {donor['FirstName']} {donor['LastName']}, Blood Type: {donor['BloodType']}, Date of Birth: {donor['DateOfBirth']}")
        else:
            print("No donor data found.")
    except FileNotFoundError:
        print("The donors' file does not exist yet. Please register first.")

# Example of accessing a donor by index
def view_single_donor(index):
    try:
        donors_list = []
        with open("donor_registration.txt", "r") as file:
            lines = file.readlines()

            donor_data = {}
            for line in lines:
                line = line.strip()
                if line.startswith("DonorID:"):
                    if donor_data:  # If donor_data is not empty, add the previous donor data to the list
                        donors_list.append(donor_data)
                    donor_data = {"DonorID": line.split(":")[1].strip()}  # Start new donor
                elif line.startswith("FirstName:"):
                    donor_data["FirstName"] = line.split(":")[1].strip()
                elif line.startswith("LastName:"):
                    donor_data["LastName"] = line.split(":")[1].strip()
                elif line.startswith("BloodType:"):
                    donor_data["BloodType"] = line.split(":")[1].strip()
                elif line.startswith("DateOfBirth:"):
                    donor_data["DateOfBirth"] = line.split(":")[1].strip()
            if donor_data:  # Add the last donor after finishing reading the file
                donors_list.append(donor_data)

        # Now you can access donors by index
        if 0 <= index < len(donors_list):
            donor = donors_list[index]
            print(f"Donor ID: {donor['DonorID']}, Name: {donor['FirstName']} {donor['LastName']}, Blood Type: {donor['BloodType']}, Date of Birth: {donor['DateOfBirth']}")
        else:
            print("Invalid index. Please select a valid donor index.")
    except FileNotFoundError:
        print("The donors' file does not exist yet. Please register first.")
