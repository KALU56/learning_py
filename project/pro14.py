import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
import hashlib
import json
import os

class BloodBankSystem:
    def __init__(self):
        self.init_data()
        self.setup_main_window()
        self.load_data()  # Load saved data if exists

    def init_data(self):
        """Initialize data structures"""
        self.users = {
            "admin": {
                "password": self.hash_password("admin123"),
                "role": "supervisor"
            }
        }
        self.donors = {}
        self.donations = {}
        self.appointments = []
        self.blood_inventory = {
            "A+": 0, "A-": 0, "B+": 0, "B-": 0,
            "AB+": 0, "AB-": 0, "O+": 0, "O-": 0
        }
        self.medical_records = {}
        self.messages = {}

    def hash_password(self, password):
        """Hash password for security"""
        return hashlib.sha256(password.encode()).hexdigest()

    def load_data(self):
        """Load saved data from file"""
        try:
            if os.path.exists('blood_bank_data.json'):
                with open('blood_bank_data.json', 'r') as file:
                    data = json.load(file)
                    self.users.update(data.get('users', {}))
                    self.donors.update(data.get('donors', {}))
                    self.donations.update(data.get('donations', {}))
                    self.appointments = data.get('appointments', [])
                    self.blood_inventory.update(data.get('blood_inventory', {}))
                    self.medical_records.update(data.get('medical_records', {}))
                    self.messages.update(data.get('messages', {}))
        except Exception as e:
            messagebox.showwarning("Warning", f"Could not load saved data: {str(e)}")

    def save_data(self):
        """Save data to file"""
        data = {
            'users': self.users,
            'donors': self.donors,
            'donations': self.donations,
            'appointments': self.appointments,
            'blood_inventory': self.blood_inventory,
            'medical_records': self.medical_records,
            'messages': self.messages
        }
        try:
            with open('blood_bank_data.json', 'w') as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            messagebox.showwarning("Warning", f"Could not save data: {str(e)}")

    def setup_main_window(self):
        """Setup the main application window"""
        self.root = tk.Tk()
        self.root.title("Blood Bank Management System")
        self.root.geometry("1000x600")
        self.root.configure(bg="#FFE6E6")
        
        # Center window
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - 1000) // 2
        y = (screen_height - 600) // 2
        self.root.geometry(f"1000x600+{x}+{y}")

        # Save data on window close
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.create_login_page()

    def create_login_page(self):
        """Create the login interface"""
        # Main Frame
        main_frame = tk.Frame(self.root, bg="#FFE6E6")
        main_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Title
        title = tk.Label(main_frame, 
                        text="Blood Bank Management System",
                        font=("Arial", 24, "bold"),
                        bg="#FFE6E6",
                        fg="#8B0000")
        title.pack(pady=20)

        # Login Frame
        login_frame = tk.Frame(main_frame, bg="#FFE6E6")
        login_frame.pack(padx=20, pady=20)

        # User Type Selection
        type_frame = tk.Frame(login_frame, bg="#FFE6E6")
        type_frame.pack(pady=10)
        
        self.user_type = tk.StringVar(value="supervisor")
        tk.Radiobutton(type_frame, 
                      text="Supervisor",
                      variable=self.user_type,
                      value="supervisor",
                      bg="#FFE6E6").pack(side=tk.LEFT, padx=10)
        tk.Radiobutton(type_frame,
                      text="Donor",
                      variable=self.user_type,
                      value="donor",
                      bg="#FFE6E6").pack(side=tk.LEFT, padx=10)

        # Username
        tk.Label(login_frame,
                text="Username:",
                font=("Arial", 12),
                bg="#FFE6E6").pack(pady=5)
        self.username_entry = tk.Entry(login_frame,
                                     font=("Arial", 12),
                                     width=30)
        self.username_entry.pack()

        # Password
        tk.Label(login_frame,
                text="Password:",
                font=("Arial", 12),
                bg="#FFE6E6").pack(pady=5)
        self.password_entry = tk.Entry(login_frame,
                                     font=("Arial", 12),
                                     show="•",
                                     width=30)
        self.password_entry.pack()

        # Buttons Frame
        button_frame = tk.Frame(login_frame, bg="#FFE6E6")
        button_frame.pack(pady=20)

        # Login Button
        tk.Button(button_frame,
                 text="Login",
                 command=self.handle_login,
                 bg="#8B0000",
                 fg="white",
                 font=("Arial", 12),
                 width=12).pack(side=tk.LEFT, padx=5)

        # Register Button
        tk.Button(button_frame,
                 text="Register",
                 command=self.show_registration,
                 bg="#DC143C",
                 fg="white",
                 font=("Arial", 12),
                 width=12).pack(side=tk.LEFT, padx=5)

    def handle_login(self):
        """Handle login attempts"""
        username = self.username_entry.get()
        password = self.password_entry.get()
        user_type = self.user_type.get()

        if not username or not password:
            messagebox.showerror("Error", "Please enter both username and password")
            return

        hashed_password = self.hash_password(password)

        if user_type == "supervisor":
            if username in self.users and \
               self.users[username]["password"] == hashed_password and \
               self.users[username]["role"] == "supervisor":
                self.root.withdraw()
                self.open_supervisor_dashboard(username)
            else:
                messagebox.showerror("Error", "Invalid supervisor credentials")
        else:
            if username in self.donors and \
               self.donors[username]["password"] == hashed_password:
                self.root.withdraw()
                self.open_donor_dashboard(username)
            else:
                messagebox.showerror("Error", "Invalid donor credentials")

    def show_registration(self):
        """Show donor registration window"""
        self.root.withdraw()
        DonorRegistration(self)

    def open_supervisor_dashboard(self, username):
        """Open supervisor dashboard"""
        SupervisorDashboard(self, username)

    def open_donor_dashboard(self, username):
        """Open donor dashboard"""
        DonorDashboard(self, username)

    def on_closing(self):
        """Handle application closing"""
        self.save_data()
        self.root.destroy()

def main():
    app = BloodBankSystem()
    app.root.mainloop()

if __name__ == "__main__":
    main()