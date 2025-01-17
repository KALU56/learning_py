import tkinter as tk
from tkinter import messagebox


# Function to handle login
def login():
    username = username_entry.get()
    password = password_entry.get()

    # Dummy credentials for testing
    if username == "admin" and password == "admin123":
        root.destroy()  # Close login window
        open_dashboard()
    else:
        messagebox.showerror("Error", "Invalid username or password")


# Function to open the dashboard
def open_dashboard():
    dashboard = tk.Tk()
    dashboard.title("Dashboard")
    dashboard.geometry("400x400")

    tk.Label(dashboard, text="Welcome to the Blood Bank System!", font=("Arial", 16)).pack(pady=20)

    tk.Button(dashboard, text="Register Donor", width=20, command=open_donor_registration).pack(pady=10)
    tk.Button(dashboard, text="View Donors", width=20, command=view_donors).pack(pady=10)
    tk.Button(dashboard, text="Exit", width=20, command=dashboard.destroy).pack(pady=10)

    dashboard.mainloop()


# Function to open the donor registration form
def open_donor_registration():
    registration = tk.Toplevel()
    registration.title("Donor Registration")
    registration.geometry("400x400")

    tk.Label(registration, text="Donor Registration", font=("Arial", 16)).pack(pady=10)

    tk.Label(registration, text="Name:").pack(anchor="w", padx=20)
    name_entry = tk.Entry(registration, width=30)
    name_entry.pack(padx=20)

    tk.Label(registration, text="Age:").pack(anchor="w", padx=20)
    age_entry = tk.Entry(registration, width=30)
    age_entry.pack(padx=20)

    tk.Label(registration, text="Blood Type:").pack(anchor="w", padx=20)
    blood_type_entry = tk.Entry(registration, width=30)
    blood_type_entry.pack(padx=20)

    tk.Label(registration, text="Medical History:").pack(anchor="w", padx=20)
    medical_history_entry = tk.Text(registration, width=30, height=5)
    medical_history_entry.pack(padx=20)

    def save_donor():
        name = name_entry.get()
        age = age_entry.get()
        blood_type = blood_type_entry.get()
        medical_history = medical_history_entry.get("1.0", "end-1c")

        if not name or not age or not blood_type:
            messagebox.showerror("Error", "All fields are required!")
        else:
            # Save donor details to a file or database (dummy implementation here)
            with open("donors.txt", "a") as file:
                file.write(f"{name},{age},{blood_type},{medical_history}\n")
            messagebox.showinfo("Success", "Donor registered successfully!")
            registration.destroy()

    tk.Button(registration, text="Register", command=save_donor).pack(pady=10)


# Function to view donors
def view_donors():
    try:
        with open("donors.txt", "r") as file:
            donors = file.readlines()

        donor_window = tk.Toplevel()
        donor_window.title("Donor List")
        donor_window.geometry("400x400")

        tk.Label(donor_window, text="Registered Donors", font=("Arial", 16)).pack(pady=10)

        for donor in donors:
            tk.Label(donor_window, text=donor.strip()).pack(anchor="w", padx=20)

    except FileNotFoundError:
        messagebox.showerror("Error", "No donors found!")


# Main Login Window
root = tk.Tk()
root.title("Blood Bank Login")
root.geometry("400x300")

tk.Label(root, text="Blood Bank Login", font=("Arial", 16)).pack(pady=20)

tk.Label(root, text="Username:").pack(anchor="w", padx=20)
username_entry = tk.Entry(root, width=30)
username_entry.pack(padx=20)

tk.Label(root, text="Password:").pack(anchor="w", padx=20)
password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack(padx=20)

tk.Button(root, text="Login", width=15, command=login).pack(pady=20)

root.mainloop()
