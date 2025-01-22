import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from io import BytesIO
import requests
from PIL import Image, ImageTk
import re
from datetime import datetime
import hashlib
import json
import csv

# Constants
COLORS = {
    'primary': '#8B0000',      # Dark Red
    'secondary': '#FFE6E6',    # Light Pink
    'accent': '#DC143C',       # Crimson
    'text_dark': '#2C0000',    # Very Dark Red
    'text_light': '#FFFFFF',   # White
    'success': '#28a745',      # Green
    'warning': '#ffc107',      # Yellow
    'error': '#dc3545'         # Red
}

BLOOD_TYPES = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']

class Database:
    def __init__(self):
        self.users = {
            "admin": {
                "password": self.hash_password("admin123"),
                "role": "supervisor"
            }
        }
        self.donors = {}
        self.donations = {}
        self.events = []
        self.appointments = []
        self.news = []
        self.blood_inventory = {blood_type: 0 for blood_type in BLOOD_TYPES}
        self.medical_records = {}
        
        # Load demo data
        self.load_demo_data()

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def load_demo_data(self):
        # Add some demo events
        self.events = [
            {
                "title": "Blood Donation Drive",
                "date": "2024-04-01",
                "time": "09:00 - 17:00",
                "location": "City Hospital",
                "description": "Annual blood donation drive",
                "status": "upcoming"
            }
        ]
        
        # Add some demo news
        self.news = [
            {
                "title": "New Blood Bank Center Opening",
                "date": "2024-03-15",
                "content": "We are excited to announce the opening of a new center..."
            }
        ]

class BloodBankSystem:
    def __init__(self):
        self.db = Database()
        self.setup_main_window()

    def setup_main_window(self):
        self.root = tk.Tk()
        self.root.title("Blood Bank Management System")
        self.root.geometry("1200x700")
        self.root.configure(bg=COLORS['secondary'])
        
        # Center window on screen
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - 1200) // 2
        y = (screen_height - 700) // 2
        self.root.geometry(f"1200x700+{x}+{y}")

        self.setup_login_page()

    def setup_login_page(self):
        # Clear existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        # Create main frame
        main_frame = tk.Frame(self.root, bg=COLORS['secondary'])
        main_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Logo and Title
        title_frame = tk.Frame(main_frame, bg=COLORS['secondary'])
        title_frame.pack(pady=20)

        # Try to load logo image
        try:
            logo_url = "https://example.com/logo.png"  # Replace with actual logo URL
            logo_image = self.load_image_from_url(logo_url)
            if logo_image:
                logo_label = tk.Label(title_frame, image=logo_image, bg=COLORS['secondary'])
                logo_label.image = logo_image
                logo_label.pack()
        except:
            pass

        title = tk.Label(title_frame, 
                        text="Blood Bank Management System",
                        font=("Arial", 24, "bold"),
                        bg=COLORS['secondary'],
                        fg=COLORS['primary'])
        title.pack(pady=10)

        # Login Form
        login_frame = tk.Frame(main_frame, bg=COLORS['secondary'])
        login_frame.pack(padx=20, pady=20)

        # Username
        username_frame = tk.Frame(login_frame, bg=COLORS['secondary'])
        username_frame.pack(fill="x", pady=5)
        
        tk.Label(username_frame, 
                text="Username:",
                font=("Arial", 12),
                bg=COLORS['secondary'],
                fg=COLORS['text_dark']).pack(side="left")
        
        self.username_entry = tk.Entry(username_frame,
                                     font=("Arial", 12),
                                     width=30)
        self.username_entry.pack(side="left", padx=10)

        # Password
        password_frame = tk.Frame(login_frame, bg=COLORS['secondary'])
        password_frame.pack(fill="x", pady=5)
        
        tk.Label(password_frame,
                text="Password:",
                font=("Arial", 12),
                bg=COLORS['secondary'],
                fg=COLORS['text_dark']).pack(side="left")
        
        self.password_entry = tk.Entry(password_frame,
                                     font=("Arial", 12),
                                     width=30,
                                     show="•")
        self.password_entry.pack(side="left", padx=10)

        # Buttons Frame
        buttons_frame = tk.Frame(login_frame, bg=COLORS['secondary'])
        buttons_frame.pack(pady=20)

        # Login Button
        login_btn = tk.Button(buttons_frame,
                            text="Login",
                            font=("Arial", 12, "bold"),
                            bg=COLORS['primary'],
                            fg=COLORS['text_light'],
                            width=15,
                            command=self.login)
        login_btn.pack(side="left", padx=5)

        # Register Button
        register_btn = tk.Button(buttons_frame,
                               text="Register as Donor",
                               font=("Arial", 12),
                               bg=COLORS['accent'],
                               fg=COLORS['text_light'],
                               width=15,
                               command=self.show_registration)
        register_btn.pack(side="left", padx=5)

        # Bind enter key to login
        self.root.bind('<Return>', lambda e: self.login())

    def load_image_from_url(self, url, size=(100, 100)):
        try:
            response = requests.get(url)
            image_data = BytesIO(response.content)
            image = Image.open(image_data)
            image = image.resize(size, Image.Resampling.LANCZOS)
            return ImageTk.PhotoImage(image)
        except:
            return None

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if not username or not password:
            messagebox.showerror("Error", "Please enter both username and password")
            return

        hashed_password = self.db.hash_password(password)
        
        if username in self.db.users and self.db.users[username]["password"] == hashed_password:
            self.current_user = username
            self.current_role = self.db.users[username]["role"]
            
            if self.current_role == "supervisor":
                self.show_supervisor_dashboard()
            else:
                self.show_donor_dashboard()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def show_registration(self):
        # Will implement in next part
        pass

    def show_supervisor_dashboard(self):
        # Will implement in next part
        pass

    def show_donor_dashboard(self):
        # Will implement in next part
        pass

def main():
    app = BloodBankSystem()
    app.root.mainloop()

if __name__ == "__main__":
    main()