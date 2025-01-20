import tkinter as tk
from tkinter import messagebox
from .data_manager import DataManager

class LoginSystem:
    def __init__(self, root):
        self.root = root
        self.data_manager = DataManager()
        self.setup_login_window()

    def setup_login_window(self):
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(padx=20, pady=20)

        # User type selection
        tk.Label(self.login_frame, text="Select User Type:").pack()
        self.user_type = tk.StringVar(value="donor")
        tk.Radiobutton(self.login_frame, text="Donor", variable=self.user_type, 
                      value="donor").pack()
        tk.Radiobutton(self.login_frame, text="Supervisor", variable=self.user_type, 
                      value="supervisor").pack()

        # Username
        tk.Label(self.login_frame, text="Username:").pack()
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.pack()

        # Password
        tk.Label(self.login_frame, text="Password:").pack()
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.pack()

        # Login button
        tk.Button(self.login_frame, text="Login", command=self.login).pack(pady=10)
        
        # Register button (for donors)
        tk.Button(self.login_frame, text="Register as Donor", 
                 command=self.open_registration).pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        user_type = self.user_type.get()

        data = self.data_manager.load_data()
        
        if user_type == "supervisor":
            if (username == data['users']['supervisor']['username'] and 
                password == data['users']['supervisor']['password']):
                self.open_supervisor_dashboard()
            else:
                messagebox.showerror("Error", "Invalid supervisor credentials")
        else:
            # Check donor credentials
            donor_found = False
            for donor_id, donor_data in data['donors'].items():
                if (donor_data['username'] == username and 
                    donor_data['password'] == password):
                    self.open_donor_dashboard(donor_id)
                    donor_found = True
                    break
            
            if not donor_found:
                messagebox.showerror("Error", "Invalid donor credentials")

    def open_registration(self):
        self.login_frame.pack_forget()
        from .donor_registration import DonorRegistration
        DonorRegistration(self.root, self.show_login)

    def open_supervisor_dashboard(self):
        self.login_frame.pack_forget()
        from .supervisor_dashboard import SupervisorDashboard
        SupervisorDashboard(self.root)

    def open_donor_dashboard(self, donor_id):
        self.login_frame.pack_forget()
        from .donor_dashboard import DonorDashboard
        DonorDashboard(self.root, donor_id)

    def show_login(self):
        self.login_frame.pack()