import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from .data_manager import DataManager
from . import CONFIG, MESSAGE_TYPES

class SupervisorDashboard:
    def __init__(self, root):
        self.root = root
        self.data_manager = DataManager()
        self.setup_dashboard()

    def setup_dashboard(self):
        self.dashboard_frame = tk.Frame(self.root)
        self.dashboard_frame.pack(fill=tk.BOTH, expand=True)

        # Create tabs
        self.tab_control = ttk.Notebook(self.dashboard_frame)
        
        # Create different tabs
        self.inventory_tab = ttk.Frame(self.tab_control)
        self.appointments_tab = ttk.Frame(self.tab_control)
        self.donors_tab = ttk.Frame(self.tab_control)
        self.camps_tab = ttk.Frame(self.tab_control)
        
        # Setup each tab
        self.setup_inventory_tab()
        self.setup_appointments_tab()
        self.setup_donors_tab()
        self.setup_camps_tab()

        # Add tabs to notebook
        self.tab_control.add(self.inventory_tab, text='Blood Inventory')
        self.tab_control.add(self.appointments_tab, text='Appointments')
        self.tab_control.add(self.donors_tab, text='Donors')
        self.tab_control.add(self.camps_tab, text='Donation Camps')
        
        self.tab_control.pack(expand=1, fill="both")

        # Logout button
        tk.Button(self.dashboard_frame, text="Logout", 
                 command=self.logout).pack(pady=10)

    def setup_inventory_tab(self):
        tk.Label(self.inventory_tab, text="Blood Inventory", 
                font=('Arial', 12, 'bold')).pack(pady=10)

        self.inventory_tree = ttk.Treeview(self.inventory_tab, 
                                         columns=('Blood Type', 'Units Available'))
        self.inventory_tree.heading('Blood Type', text='Blood Type')
        self.inventory_tree.heading('Units Available', text='Units Available')
        self.inventory_tree.pack(pady=10, padx=10)

        update_frame = ttk.Frame(self.inventory_tab)
        update_frame.pack(pady=10)

        self.blood_type_var = tk.StringVar(value=CONFIG['BLOOD_TYPES'][0])
        ttk.OptionMenu(update_frame, self.blood_type_var, 
                      *CONFIG['BLOOD_TYPES']).pack(side=tk.LEFT)

        self.units_entry = ttk.Entry(update_frame, width=10)
        self.units_entry.pack(side=tk.LEFT, padx=5)

        ttk.Button(update_frame, text="Add Units", 
                  command=lambda: self.update_inventory(1)).pack(side=tk.LEFT, padx=5)
        ttk.Button(update_frame, text="Remove Units", 
                  command=lambda: self.update_inventory(-1)).pack(side=tk.LEFT)

        self.refresh_inventory()

    def setup_appointments_tab(self):
        self.appointments_tree = ttk.Treeview(self.appointments_tab,
                                            columns=('ID', 'Date', 'Donor', 'Status'))
        self.appointments_tree.heading('ID', text='ID')
        self.appointments_tree.heading('Date', text='Date')
        self.appointments_tree.heading('Donor', text='Donor')
        self.appointments_tree.heading('Status', text='Status')
        self.appointments_tree.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        actions_frame = ttk.Frame(self.appointments_tab)
        actions_frame.pack(pady=10)

        ttk.Button(actions_frame, text="Approve", 
                  command=self.approve_appointment).pack(side=tk.LEFT, padx=5)
        ttk.Button(actions_frame, text="Reject", 
                  command=self.reject_appointment).pack(side=tk.LEFT)

        self.refresh_appointments()

    def setup_donors_tab(self):
        self.donors_tree = ttk.Treeview(self.donors_tab,
                                      columns=('ID', 'Name', 'Blood Type', 'Status'))
        self.donors_tree.heading('ID', text='ID')
        self.donors_tree.heading('Name', text='Name')
        self.donors_tree.heading('Blood Type', text='Blood Type')
        self.donors_tree.heading('Status', text='Status')
        self.donors_tree.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        message_frame = ttk.Frame(self.donors_tab)
        message_frame.pack(pady=10, padx=10, fill=tk.X)

        self.message_type_var = tk.StringVar(value=list(MESSAGE_TYPES.values())[0])
        ttk.OptionMenu(message_frame, self.message_type_var, 
                      *MESSAGE_TYPES.values()).pack(side=tk.LEFT)

        self.message_entry = ttk.Entry(message_frame, width=50)
        self.message_entry.pack(side=tk.LEFT, padx=5)

        ttk.Button(message_frame, text="Send Message", 
                  command=self.send_message).pack(side=tk.LEFT)

        self.refresh_donors()

    def setup_camps_tab(self):
        form_frame = ttk.Frame(self.camps_tab)
        form_frame.pack(pady=10, padx=10)

        ttk.Label(form_frame, text="Camp Name:").grid(row=0, column=0, pady=5)
        self.camp_name_entry = ttk.Entry(form_frame)
        self.camp_name_entry.grid(row=0, column=1)

        ttk.Label(form_frame, text="Location:").grid(row=1, column=0, pady=5)
        self.camp_location_entry = ttk.Entry(form_frame)
        self.camp_location_entry.grid(row=1, column=1)

        ttk.Label(form_frame, text="Date:").grid(row=2, column=0, pady=5)
        self.camp_date_entry = ttk.Entry(form_frame)
        self.camp_date_entry.grid(row=2, column=1)

        ttk.Button(form_frame, text="Register Camp", 
                  command=self.register_camp).grid(row=3, column=0, columnspan=2, pady=10)

        self.camps_tree = ttk.Treeview(self.camps_tab,
                                     columns=('Name', 'Location', 'Date', 'Status'))
        self.camps_tree.heading('Name', text='Name')
        self.camps_tree.heading('Location', text='Location')
        self.camps_tree.heading('Date', text='Date')
        self.camps_tree.heading('Status', text='Status')
        self.camps_tree.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        self.refresh_camps()

    def update_inventory(self, multiplier):
        try:
            units = int(self.units_entry.get()) * multiplier
            blood_type = self.blood_type_var.get()
            self.data_manager.update_blood_inventory(blood_type, units)
            self.refresh_inventory()
            messagebox.showinfo("Success", 
                              f"Updated inventory for {blood_type}")
        except ValueError:
            messagebox.showerror("Error", 
                               "Please enter a valid number of units")

    def refresh_inventory(self):
        data = self.data_manager.load_data()
        self.inventory_tree.delete(*self.inventory_tree.get_children())
        for blood_type, units in data['blood_inventory'].items():
            self.inventory_tree.insert('', 'end', values=(blood_type, units))

    def refresh_appointments(self):
        data = self.data_manager.load_data()
        self.appointments_tree.delete(*self.appointments_tree.get_children())
        for appt_id, appt in data['appointments'].items():
            donor_name = data['donors'][appt['donor_id']]['name']
            self.appointments_tree.insert('', 'end', values=(
                appt_id,
                appt['date_time'],
                donor_name,
                appt['status']
            ))

    def refresh_donors(self):
        data = self.data_manager.load_data()
        self.donors_tree.delete(*self.donors_tree.get_children())
        for donor_id, donor in data['donors'].items():
            self.donors_tree.insert('', 'end', values=(
                donor_id,
                donor['name'],
                donor['blood_type'],
                'Active'
            ))

    def refresh_camps(self):
        data = self.data_manager.load_data()
        self.camps_tree.delete(*self.camps_tree.get_children())
        for camp_id, camp in data['donation_camps'].items():
            self.camps_tree.insert('', 'end', values=(
                camp['name'],
                camp['location'],
                camp['date'],
                camp['status']
            ))

    def approve_appointment(self):
        selected = self.appointments_tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select an appointment")
            return
        
        appt_id = self.appointments_tree.item(selected[0])['values'][0]
        data = self.data_manager.load_data()
        data['appointments'][appt_id]['status'] = 'approved'
        self.data_manager.save_data(data)
        self.refresh_appointments()

    def reject_appointment(self):
        selected = self.appointments_tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select an appointment")
            return
        
        appt_id = self.appointments_tree.item(selected[0])['values'][0]
        data = self.data_manager.load_data()
        data['appointments'][appt_id]['status'] = 'rejected'
        self.data_manager.save_data(data)
        self.refresh_appointments()

    def send_message(self):
        selected = self.donors_tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a donor")
            return
        
        donor_id = self.donors_tree.item(selected[0])['values'][0]
        message_content = self.message_entry.get()
        if not message_content:
            messagebox.showwarning("Warning", "Please enter a message")
            return

        self.data_manager.add_message(
            'supervisor',
            donor_id,
            self.message_type_var.get(),
            message_content
        )
        messagebox.showinfo("Success", "Message sent successfully")
        self.message_entry.delete(0, tk.END)

    def register_camp(self):
        camp_data = {
            'name': self.camp_name_entry.get(),
            'location': self.camp_location_entry.get(),
            'date': self.camp_date_entry.get(),
            'status': 'scheduled'
        }

        data = self.data_manager.load_data()
        camp_id = f"C{len(data['donation_camps']) + 1:04d}"
        data['donation_camps'][camp_id] = camp_data
        self.data_manager.save_data(data)
        
        self.refresh_camps()
        messagebox.showinfo("Success", "Donation camp registered successfully")
        
        # Clear entries
        self.camp_name_entry.delete(0, tk.END)
        self.camp_location_entry.delete(0, tk.END)
        self.camp_date_entry.delete(0, tk.END)

    def logout(self):
        self.dashboard_frame.destroy()
        from .login_system import LoginSystem
        LoginSystem(self.root)