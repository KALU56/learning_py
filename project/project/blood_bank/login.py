import tkinter as tk
from tkinter import ttk, messagebox
import hashlib
from supervisor_dashboard import SupervisorDashboard
from donor_dashboard import DonorDashboard
from donor_registration import DonorRegistration

class BloodBankSystem:
    def __init__(self):
        self.init_data()
        self.setup_main_window()

    def init_data(self):
        # Initial data setup
        self.users = {
            "supervisor": {
                "password": self.hash_password("admin123"),
                "role": "supervisor"
            }
        }
        self.donors = {}
        self.schedules = {}
        self.messages = {}
        self.blood_inventory = {
            "A+": 0, "A-": 0, "B+": 0, "B-": 0,
            "AB+": 0, "AB-": 0, "O+": 0, "O-": 0
        }
        self.donation_history = {}

    def setup_main_window(self):
        self.root = tk.Tk()
        self.root.title("Blood Bank Management System")
        self.root.geometry("1000x600")
        self.root.configure(bg="#FFE6E6")
        
        # Create main login frame
        main_frame = tk.Frame(self.root, bg="#FFE6E6")
        main_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Title
        title = tk.Label(main_frame, 
                        text="Blood Bank Management System",
                        font=("Arial", 24, "bold"),
                        bg="#FFE6E6",
                        fg="#8B0000")
        title.pack(pady=20)

        # User type selection
        self.user_type = tk.StringVar(value="supervisor")
        type_frame = tk.Frame(main_frame, bg="#FFE6E6")
        type_frame.pack(pady=10)
        
        tk.Radiobutton(type_frame, text="Supervisor", 
                      variable=self.user_type,
                      value="supervisor",
                      bg="#FFE6E6").pack(side=tk.LEFT, padx=10)
        tk.Radiobutton(type_frame, text="Donor",
                      variable=self.user_type,
                      value="donor",
                      bg="#FFE6E6").pack(side=tk.LEFT, padx=10)

        # Login fields
        login_frame = tk.Frame(main_frame, bg="#FFE6E6")
        login_frame.pack(pady=20)

        tk.Label(login_frame, text="Username:",
                font=("Arial", 12),
                bg="#FFE6E6").pack()
        self.username_entry = tk.Entry(login_frame, font=("Arial", 12))
        self.username_entry.pack(pady=5)

        tk.Label(login_frame, text="Password:",
                font=("Arial", 12),
                bg="#FFE6E6").pack()
        self.password_entry = tk.Entry(login_frame,
                                     font=("Arial", 12),
                                     show="•")
        self.password_entry.pack(pady=5)

        # Buttons
        button_frame = tk.Frame(main_frame, bg="#FFE6E6")
        button_frame.pack(pady=20)

        tk.Button(button_frame, text="Login",
                 command=self.handle_login,
                 bg="#8B0000",
                 fg="white",
                 font=("Arial", 12)).pack(side=tk.LEFT, padx=5)

        tk.Button(button_frame, text="Register as Donor",
                 command=self.show_registration,
                 bg="#DC143C",
                 fg="white",
                 font=("Arial", 12)).pack(side=tk.LEFT, padx=5)

    def handle_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        user_type = self.user_type.get()

        if not username or not password:
            messagebox.showerror("Error", "Please enter both username and password")
            return

        if user_type == "supervisor":
            if username == "supervisor" and password == "admin123":
                self.root.withdraw()
                SupervisorDashboard(self, username)
            else:
                messagebox.showerror("Error", "Invalid supervisor credentials")
        else:
            if username in self.donors and \
               self.donors[username]["password"] == password:
                self.root.withdraw()
                DonorDashboard(self, username)
            else:
                messagebox.showerror("Error", "Invalid donor credentials")

    def show_registration(self):
        self.root.withdraw()
        DonorRegistration(self)

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

def main():
    app = BloodBankSystem()
    app.root.mainloop()

if __name__ == "__main__":
    main()