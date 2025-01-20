import tkinter as tk
from tkinter import ttk, messagebox
from .data_manager import DataManager
from . import CONFIG

class DonorRegistration:
    def __init__(self, root, callback):
        self.root = root
        self.callback = callback
        self.data_manager = DataManager()
        self.setup_registration_window()

    def setup_registration_window(self):
        self.reg_frame = tk.Frame(self.root)
        self.reg_frame.pack(padx=20, pady=20)

        # Personal Information
        tk.Label(self.reg_frame, text="Personal Information", 
                font=('Arial', 12, 'bold')).pack()

        # Create StringVar for blood type
        self.blood_type_var = tk.StringVar(value=CONFIG['BLOOD_TYPES'][0])

        fields = [
            ('Full Name:', 'name'),
            ('Age:', 'age'),
            ('Weight (kg):', 'weight'),
            ('Blood Type:', 'blood_type'),
            ('Phone:', 'phone'),
            ('Email:', 'email'),
            ('Username:', 'username'),
            ('Password:', 'password')
        ]

        self.entries = {}
        for label, field in fields:
            tk.Label(self.reg_frame, text=label).pack()
            if field == 'password':
                entry = tk.Entry(self.reg_frame, show="*")
            elif field == 'blood_type':
                entry = tk.OptionMenu(self.reg_frame, self.blood_type_var, 
                                    *CONFIG['BLOOD_TYPES'])
                self.entries[field] = self.blood_type_var
            else:
                entry = tk.Entry(self.reg_frame)
            entry.pack()
            if field != 'blood_type':
                self.entries[field] = entry

        # Register button
        tk.Button(self.reg_frame, text="Register", 
                 command=self.register).pack(pady=10)
        
        # Back button
        tk.Button(self.reg_frame, text="Back to Login", 
                 command=self.back_to_login).pack()

    def register(self):
        try:
            age = int(self.entries['age'].get())
            weight = float(self.entries['weight'].get())
            
            if age < CONFIG['MIN_DONOR_AGE'] or age > CONFIG['MAX_DONOR_AGE']:
                messagebox.showerror("Error", "Age must be between 18 and 65")
                return
            
            if weight < CONFIG['MIN_WEIGHT']:
                messagebox.showerror("Error", "Weight must be at least 50 kg")
                return

        except ValueError:
            messagebox.showerror("Error", "Please enter valid age and weight")
            return

        donor_data = {
            'name': self.entries['name'].get(),
            'age': age,
            'weight': weight,
            'blood_type': self.blood_type_var.get(),
            'phone': self.entries['phone'].get(),
            'email': self.entries['email'].get(),
            'username': self.entries['username'].get(),
            'password': self.entries['password'].get(),
            'donation_history': [],
            'next_eligible_date': None
        }

        donor_id = self.data_manager.add_donor(donor_data)
        messagebox.showinfo("Success", 
                          f"Registration successful! Your donor ID is: {donor_id}")
        self.back_to_login()

    def back_to_login(self):
        self.reg_frame.destroy()
        self.callback()