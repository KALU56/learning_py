import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from .data_manager import DataManager
from tkcalendar import DateEntry

class DonorDashboard:
    def __init__(self, root, donor_id):
        self.root = root
        self.donor_id = donor_id
        self.data_manager = DataManager()
        self.setup_dashboard()

    def setup_dashboard(self):
        self.dashboard_frame = tk.Frame(self.root)
        self.dashboard_frame.pack(fill=tk.BOTH, expand=True)

        # Create tabs
        self.tab_control = ttk.Notebook(self.dashboard_frame)
        
        # Schedule tab
        self.schedule_tab = ttk.Frame(self.tab_control)
        self.setup_schedule_tab()
        
        # History tab
        self.history_tab = ttk.Frame(self.tab_control)
        self.setup_history_tab()
        
        # Messages tab
        self.messages_tab = ttk.Frame(self.tab_control)
        self.setup_messages_tab()

        self.tab_control.add(self.schedule_tab, text='Schedule Donation')
        self.tab_control.add(self.history_tab, text='Donation History')
        self.tab_control.add(self.messages_tab, text='Messages')
        self.tab_control.pack(expand=1, fill="both")

        # Logout button
        tk.Button(self.dashboard_frame, text="Logout", 
                 command=self.logout).pack(pady=10)

    def setup_schedule_tab(self):
        tk.Label(self.schedule_tab, text="Select Date:").pack(pady=5)
        self.date_entry = DateEntry(self.schedule_tab, 
                                  mindate=datetime.now().date(),
                                  date_pattern='yyyy-mm-dd')
        self.date_entry.pack()

        tk.Label(self.schedule_tab, text="Select Time:").pack(pady=5)
        times = ['09:00', '10:00', '11:00', '14:00', '15:00', '16:00']
        self.time_var = tk.StringVar(value=times[0])
        time_menu = tk.OptionMenu(self.schedule_tab, self.time_var, *times)
        time_menu.pack()

        tk.Button(self.schedule_tab, text="Schedule Appointment", 
                 command=self.schedule_appointment).pack(pady=10)

    def setup_history_tab(self):
        self.history_tree = ttk.Treeview(self.history_tab, 
                                       columns=('Date', 'Blood Type', 'Status'))
        self.history_tree.heading('Date', text='Date')
        self.history_tree.heading('Blood Type', text='Blood Type')
        self.history_tree.heading('Status', text='Status')
        self.history_tree.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        self.load_donation_history()

    def setup_messages_tab(self):
        self.messages_tree = ttk.Treeview(self.messages_tab, 
                                        columns=('Date', 'Type', 'Message'))
        self.messages_tree.heading('Date', text='Date')
        self.messages_tree.heading('Type', text='Type')
        self.messages_tree.heading('Message', text='Message')
        self.messages_tree.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        self.load_messages()

    def schedule_appointment(self):
        date_str = self.date_entry.get()
        time_str = self.time_var.get()
        date_time = f"{date_str}T{time_str}:00"

        appointment_id = self.data_manager.add_appointment(
            self.donor_id, date_time)
        messagebox.showinfo("Success", 
                          f"Appointment scheduled! ID: {appointment_id}")

    def load_donation_history(self):
        data = self.data_manager.load_data()
        donor_data = data['donors'][self.donor_id]
        
        for donation in donor_data['donation_history']:
            self.history_tree.insert('', 'end', values=(
                donation['date'],
                donation['blood_type'],
                donation['status']
            ))

    def load_messages(self):
        data = self.data_manager.load_data()
        
        for message_id, message in data['messages'].items():
            if message['receiver'] == self.donor_id:
                self.messages_tree.insert('', 'end', values=(
                    message['timestamp'],
                    message['type'],
                    message['content']
                ))

    def logout(self):
        self.dashboard_frame.destroy()
        from .login_system import LoginSystem
        LoginSystem(self.root)