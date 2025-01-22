import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import re

# Global Data Storage
class DataStore:
    def __init__(self):
        self.users = {
            "supervisor": {
                "password": "admin123",
                "role": "supervisor"
            }
        }
        self.donors = {}
        self.blood_inventory = {
            "A+": 0, "A-": 0, "B+": 0, "B-": 0,
            "AB+": 0, "AB-": 0, "O+": 0, "O-": 0
        }
        self.medical_records = {}

db = DataStore()

class LoginSystem:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Blood Bank Management System")
        self.root.geometry("1000x600")
        self.root.configure(bg="#FFE6E6")
        self.setup_login_window()

    def setup_login_window(self):
        main_frame = tk.Frame(self.root, bg="#FFE6E6")
        main_frame.place(relx=0.5, rely=0.5, anchor="center")

        title = tk.Label(main_frame, text="Blood Bank Management System",
                         font=("Arial", 24, "bold"), bg="#FFE6E6", fg="#8B0000")
        title.pack(pady=20)

        login_frame = tk.Frame(main_frame, bg="#FFE6E6", relief="ridge", bd=2)
        login_frame.pack(padx=20, pady=20)

        tk.Label(login_frame, text="Username:", font=("Arial", 12), bg="#FFE6E6").pack(pady=5)
        self.username_entry = tk.Entry(login_frame, font=("Arial", 12), width=30)
        self.username_entry.pack(pady=5)

        tk.Label(login_frame, text="Password:", font=("Arial", 12), bg="#FFE6E6").pack(pady=5)
        self.password_entry = tk.Entry(login_frame, font=("Arial", 12), show="*", width=30)
        self.password_entry.pack(pady=5)

        tk.Button(login_frame, text="Login", font=("Arial", 12), bg="#8B0000", fg="white", width=20,
                  command=self.login).pack(pady=10)

        tk.Button(login_frame, text="Register as Donor", font=("Arial", 12), bg="#DC143C", fg="white", width=20,
                  command=self.open_registration).pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in db.users and db.users[username]["password"] == password:
            role = db.users[username]["role"]
            self.root.destroy()
            if role == "supervisor":
                SupervisorDashboard(username)
            else:
                DonorDashboard(username)
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def open_registration(self):
        self.root.withdraw()
        DonorRegistration(self)

class DonorRegistration:
    def __init__(self, login_system):
        self.login_system = login_system
        self.window = tk.Toplevel()
        self.window.title("Donor Registration")
        self.window.geometry("800x600")
        self.window.configure(bg="#FFE6E6")
        self.setup_registration_form()

    def setup_registration_form(self):
        main_frame = tk.Frame(self.window, bg="#FFE6E6")
        main_frame.pack(expand=True, fill="both", padx=20, pady=20)

        tk.Label(main_frame, text="Donor Registration", font=("Arial", 20, "bold"), bg="#FFE6E6", fg="#8B0000").pack(pady=10)

        canvas = tk.Canvas(main_frame, bg="#FFE6E6")
        scrollbar = tk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#FFE6E6")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        self.fields = {}
        registration_fields = {
            "Account Information": ["Username", "Password", "Confirm Password", "Email"],
            "Personal Information": ["First Name", "Last Name", "Date of Birth", "Gender", "Blood Type", "Phone Number", "Address", "City"]
        }

        for section, fields in registration_fields.items():
            tk.Label(scrollable_frame, text=section, font=("Arial", 14, "bold"), bg="#FFE6E6", fg="#8B0000").pack(pady=10)
            for field in fields:
                tk.Label(scrollable_frame, text=f"{field}:", font=("Arial", 12), bg="#FFE6E6").pack(anchor="w", padx=20)
                show = "*" if "Password" in field else None
                self.fields[field] = tk.Entry(scrollable_frame, show=show, width=40)
                self.fields[field].pack(padx=20, pady=5)

        tk.Button(scrollable_frame, text="Register", font=("Arial", 12), bg="#8B0000", fg="white",
                  command=self.register).pack(pady=20)
        tk.Button(scrollable_frame, text="Back to Login", font=("Arial", 12), bg="#DC143C", fg="white",
                  command=self.back_to_login).pack(pady=10)

        canvas.pack(side="left", fill="both", expand=True, padx=10)
        scrollbar.pack(side="right", fill="y")

    def register(self):
        for field, entry in self.fields.items():
            if not entry.get().strip():
                messagebox.showerror("Error", f"{field} is required!")
                return

        if self.fields["Password"].get() != self.fields["Confirm Password"].get():
            messagebox.showerror("Error", "Passwords do not match!")
            return

        email = self.fields["Email"].get()
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showerror("Error", "Invalid email format!")
            return

        username = self.fields["Username"].get()
        if username in db.users:
            messagebox.showerror("Error", "Username already exists!")
            return

        donor_info = {
            "username": username,
            "email": email,
            "first_name": self.fields["First Name"].get(),
            "last_name": self.fields["Last Name"].get(),
            "dob": self.fields["Date of Birth"].get(),
            "gender": self.fields["Gender"].get(),
            "blood_type": self.fields["Blood Type"].get(),
            "phone": self.fields["Phone Number"].get(),
            "address": self.fields["Address"].get(),
            "city": self.fields["City"].get(),
            "registration_date": datetime.now().strftime("%Y-%m-%d")
        }

        db.users[username] = {"password": self.fields["Password"].get(), "role": "donor"}
        db.donors[username] = donor_info
        db.medical_records[username] = []

        messagebox.showinfo("Success", "Registration successful! You can now login.")
        self.back_to_login()

    def back_to_login(self):
        self.window.destroy()
        self.login_system.root.deiconify()

if __name__ == "__main__":
    LoginSystem().root.mainloop()