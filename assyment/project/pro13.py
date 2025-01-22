import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
import hashlib

class BloodBankSystem:
    def __init__(self):
        self.init_data()
        self.setup_main_window()

    def init_data(self):
        """Initialize data structures"""
        self.users = {
            "admin": {
                "password": self.hash_password("admin123"),
                "role": "supervisor"
            }
        }
        self.donors = {}
        self.blood_inventory = {
            "A+": 0, "A-": 0, "B+": 0, "B-": 0,
            "AB+": 0, "AB-": 0, "O+": 0, "O-": 0
        }

    def hash_password(self, password):
        """Hash password for security"""
        return hashlib.sha256(password.encode()).hexdigest()

    def setup_main_window(self):
        """Setup the main application window"""
        self.root = tk.Tk()
        self.root.title("Blood Bank Management System")
        self.root.geometry("1000x600")
        self.root.configure(bg="#FFE6E6")

        # Center the window
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - 1000) // 2
        y = (screen_height - 600) // 2
        self.root.geometry(f"1000x600+{x}+{y}")

        self.create_login_page()

    def create_login_page(self):
        """Create the login interface"""
        main_frame = tk.Frame(self.root, bg="#FFE6E6")
        main_frame.place(relx=0.5, rely=0.5, anchor="center")

        title = tk.Label(main_frame, text="Blood Bank Management System",
                         font=("Arial", 24, "bold"), bg="#FFE6E6", fg="#8B0000")
        title.pack(pady=20)

        login_frame = tk.Frame(main_frame, bg="#FFE6E6")
        login_frame.pack(padx=20, pady=20)

        type_frame = tk.Frame(login_frame, bg="#FFE6E6")
        type_frame.pack(pady=10)

        self.user_type = tk.StringVar(value="supervisor")
        tk.Radiobutton(type_frame, text="Supervisor", variable=self.user_type,
                       value="supervisor", bg="#FFE6E6").pack(side=tk.LEFT, padx=10)
        tk.Radiobutton(type_frame, text="Donor", variable=self.user_type,
                       value="donor", bg="#FFE6E6").pack(side=tk.LEFT, padx=10)

        tk.Label(login_frame, text="Username:", font=("Arial", 12), bg="#FFE6E6").pack(pady=5)
        self.username_entry = tk.Entry(login_frame, font=("Arial", 12), width=30)
        self.username_entry.pack()

        tk.Label(login_frame, text="Password:", font=("Arial", 12), bg="#FFE6E6").pack(pady=5)
        self.password_entry = tk.Entry(login_frame, font=("Arial", 12), show="\u2022", width=30)
        self.password_entry.pack()

        button_frame = tk.Frame(login_frame, bg="#FFE6E6")
        button_frame.pack(pady=20)

        tk.Button(button_frame, text="Login", command=self.handle_login,
                  bg="#8B0000", fg="white", font=("Arial", 12), width=12).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Register", command=self.show_registration,
                  bg="#DC143C", fg="white", font=("Arial", 12), width=12).pack(side=tk.LEFT, padx=5)

    def handle_login(self):
        """Handle login attempts"""
        username = self.username_entry.get()
        password = self.password_entry.get()
        user_type = self.user_type.get()

        if not username or not password:
            messagebox.showerror("Error", "Please enter both username and password")
            return

        if user_type == "supervisor":
            if username in self.users and \
               self.users[username]["password"] == self.hash_password(password) and \
               self.users[username]["role"] == "supervisor":
                self.root.withdraw()
                self.open_supervisor_dashboard(username)
            else:
                messagebox.showerror("Error", "Invalid supervisor credentials")
        else:
            if username in self.donors and \
               self.donors[username]["password"] == self.hash_password(password):
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

class SupervisorDashboard:
    def __init__(self, app, username):
        self.app = app
        self.username = username
        self.dashboard = tk.Toplevel(app.root)
        self.dashboard.title("Supervisor Dashboard")
        self.dashboard.geometry("800x500")
        self.dashboard.configure(bg="#FFE6E6")

        welcome_label = tk.Label(self.dashboard, text=f"Welcome, {username}!",
                                 font=("Arial", 16, "bold"), bg="#FFE6E6", fg="#8B0000")
        welcome_label.pack(pady=20)

        tk.Button(self.dashboard, text="Logout", command=self.logout,
                  bg="#8B0000", fg="white", font=("Arial", 12), width=12).pack(pady=20)

    def logout(self):
        self.dashboard.destroy()
        self.app.root.deiconify()

class DonorDashboard:
    def __init__(self, app, username):
        self.app = app
        self.username = username
        self.dashboard = tk.Toplevel(app.root)
        self.dashboard.title("Donor Dashboard")
        self.dashboard.geometry("800x500")
        self.dashboard.configure(bg="#FFE6E6")

        welcome_label = tk.Label(self.dashboard, text=f"Welcome, {username}!",
                                 font=("Arial", 16, "bold"), bg="#FFE6E6", fg="#8B0000")
        welcome_label.pack(pady=20)

        tk.Button(self.dashboard, text="Logout", command=self.logout,
                  bg="#8B0000", fg="white", font=("Arial", 12), width=12).pack(pady=20)

    def logout(self):
        self.dashboard.destroy()
        self.app.root.deiconify()

class DonorRegistration:
    def __init__(self, app):
        self.app = app
        self.registration_window = tk.Toplevel(app.root)
        self.registration_window.title("Donor Registration")
        self.registration_window.geometry("600x400")
        self.registration_window.configure(bg="#FFE6E6")

        tk.Label(self.registration_window, text="Donor Registration",
                 font=("Arial", 16, "bold"), bg="#FFE6E6", fg="#8B0000").pack(pady=20)

        tk.Label(self.registration_window, text="Username:", font=("Arial", 12), bg="#FFE6E6").pack(pady=5)
        self.username_entry = tk.Entry(self.registration_window, font=("Arial", 12), width=30)
        self.username_entry.pack()

        tk.Label(self.registration_window, text="Password:", font=("Arial", 12), bg="#FFE6E6").pack(pady=5)
        self.password_entry = tk.Entry(self.registration_window, font=("Arial", 12), show="\u2022", width=30)
        self.password_entry.pack()

        tk.Button(self.registration_window, text="Register", command=self.register_donor,
                  bg="#8B0000", fg="white", font=("Arial", 12), width=12).pack(pady=20)

    def register_donor(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Please enter both username and password")
            return

        if username in self.app.donors or username in self.app.users:
            messagebox.showerror("Error", "Username already exists")
            return

        self.app.donors[username] = {
            "password": self.app.hash_password(password)
        }
        messagebox.showinfo("Success", "Donor registered successfully")
        self.registration_window.destroy()
        self.app.root.deiconify()


def main():
    app = BloodBankSystem()
    app.root.mainloop()

if __name__ == "__main__":
    main()
