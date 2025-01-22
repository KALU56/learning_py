import tkinter as tk
from tkinter import ttk, messagebox
from io import BytesIO
import requests
from PIL import Image, ImageTk
import re
from datetime import datetime

# Global Data Storage
users = {
    "supervisor": {"password": "admin123", "role": "supervisor"},
}
donors = []
events = []
blood_inventory = {
    "A+": 0, "A-": 0,
    "B+": 0, "B-": 0,
    "AB+": 0, "AB-": 0,
    "O+": 0, "O-": 0
}

class BloodBankSystem:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Blood Bank Management System")
        self.root.geometry("800x600")
        self.setup_login_window()

    def fetch_image(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                img_data = BytesIO(response.content)
                return Image.open(img_data)
        except Exception as e:
            print(f"Error fetching image: {e}")
        return None

    def setup_login_window(self):
        # Background Image
        bg_image_url = "https://images.pexels.com/photos/4531306/pexels-photo-4531306.jpeg"
        bg_image = self.fetch_image(bg_image_url)
        if bg_image:
            bg_image = bg_image.resize((800, 600))
            self.bg_photo = ImageTk.PhotoImage(bg_image)
            bg_label = tk.Label(self.root, image=self.bg_photo)
            bg_label.place(relwidth=1, relheight=1)

        # Login Form
        form_frame = tk.Frame(self.root, bg="#FFCCCC", bd=2, relief="ridge")
        form_frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=300)

        tk.Label(form_frame, text="Blood Bank Login", font=("Arial", 18, "bold"), 
                bg="#8B0000", fg="white").pack(pady=10, fill="x")

        tk.Label(form_frame, text="Username:", font=("Arial", 12), 
                bg="#FFCCCC").pack(anchor="w", padx=20)
        self.username_entry = tk.Entry(form_frame, font=("Arial", 12), width=30)
        self.username_entry.pack(pady=5)

        tk.Label(form_frame, text="Password:", font=("Arial", 12), 
                bg="#FFCCCC").pack(anchor="w", padx=20)
        self.password_entry = tk.Entry(form_frame, font=("Arial", 12), show="*", width=30)
        self.password_entry.pack(pady=5)

        tk.Button(form_frame, text="Login", font=("Arial", 12), bg="#8B0000", 
                 fg="white", width=20, command=self.login).pack(pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in users and users[username]["password"] == password:
            self.root.destroy()
            SupervisorDashboard(username)
        else:
            messagebox.showerror("Error", "Invalid username or password")

class SupervisorDashboard:
    def __init__(self, username):
        self.window = tk.Tk()
        self.window.title("Supervisor Dashboard")
        self.window.geometry("1000x700")
        self.setup_dashboard(username)

    def setup_dashboard(self, username):
        # Header
        header = tk.Frame(self.window, bg="#8B0000", height=60)
        header.pack(fill="x")
        tk.Label(header, text=f"Welcome, {username}", font=("Arial", 16), 
                fg="white", bg="#8B0000").pack(side="left", padx=20)

        # Main Content Area
        content = tk.Frame(self.window)
        content.pack(fill="both", expand=True, padx=20, pady=10)

        # Left Panel - Quick Stats
        left_panel = tk.Frame(content, relief="ridge", bd=2)
        left_panel.pack(side="left", fill="y", padx=10)
        
        tk.Label(left_panel, text="Blood Inventory", font=("Arial", 14, "bold")).pack(pady=10)
        for blood_type, quantity in blood_inventory.items():
            tk.Label(left_panel, text=f"{blood_type}: {quantity} units",
                    font=("Arial", 12)).pack(pady=5)

        # Right Panel - Action Buttons and Data
        right_panel = tk.Frame(content)
        right_panel.pack(side="right", fill="both", expand=True)

        # Action Buttons
        btn_frame = tk.Frame(right_panel)
        btn_frame.pack(fill="x", pady=10)

        buttons = [
            ("Register Donor", self.open_donor_registration),
            ("View Donations", self.view_donations),
            ("Manage Events", self.manage_events),
            ("Update Inventory", self.update_inventory)
        ]

        for text, command in buttons:
            tk.Button(btn_frame, text=text, font=("Arial", 12), bg="#DC143C",
                     fg="white", command=command).pack(side="left", padx=5)

        # Data Table
        self.setup_data_table(right_panel)

    def setup_data_table(self, parent):
        columns = ("D/N", "Name", "Blood Type", "Volume", "Date", "Status")
        self.tree = ttk.Treeview(parent, columns=columns, show="headings")
        
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        self.tree.pack(fill="both", expand=True, pady=10)
        self.update_table()

    def update_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for donor in donors:
            self.tree.insert("", "end", values=(
                donor.get("donor_number", ""),
                f"{donor.get('first_name', '')} {donor.get('surname', '')}",
                donor.get("blood_type", ""),
                donor.get("volume", ""),
                donor.get("date", ""),
                donor.get("status", "")
            ))

    def open_donor_registration(self):
        DonorRegistrationForm(self.window, self.update_table)

    def view_donations(self):
        DonationViewer(self.window)

    def manage_events(self):
        EventManager(self.window)

    def update_inventory(self):
        InventoryManager(self.window)

class DonorRegistrationForm:
    def __init__(self, parent, callback):
        self.window = tk.Toplevel(parent)
        self.window.title("Donor Registration")
        self.window.geometry("600x800")
        self.callback = callback
        self.setup_form()

    def setup_form(self):
        # Create scrollable canvas
        canvas = tk.Canvas(self.window)
        scrollbar = tk.Scrollbar(self.window, orient="vertical", command=canvas.yview)
        self.scrollable_frame = tk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Form fields
        self.fields = {}
        field_list = [
            "First Name", "Surname", "Date of Birth", "Age", "Sex",
            "Blood Type", "Phone", "Email", "Address", "City",
            "Emergency Contact", "Previous Donations", "Medical History"
        ]

        for field in field_list:
            tk.Label(self.scrollable_frame, text=field, font=("Arial", 12)).pack(anchor="w", padx=10)
            if field in ["Medical History"]:
                self.fields[field] = tk.Text(self.scrollable_frame, height=4, width=40)
            else:
                self.fields[field] = tk.Entry(self.scrollable_frame, width=40)
            self.fields[field].pack(padx=10, pady=5)

        tk.Button(self.scrollable_frame, text="Submit", command=self.submit_form,
                 bg="#8B0000", fg="white", font=("Arial", 12)).pack(pady=20)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def submit_form(self):
        # Validate and save donor information
        donor_info = {field: widget.get() for field, widget in self.fields.items()
                     if isinstance(widget, tk.Entry)}
        donor_info["Medical History"] = self.fields["Medical History"].get("1.0", tk.END)
        donor_info["donor_number"] = f"DN{len(donors)+1:04d}"
        donor_info["date"] = datetime.now().strftime("%Y-%m-%d")
        donor_info["status"] = "Pending"
        
        donors.append(donor_info)
        self.callback()
        messagebox.showinfo("Success", "Donor registered successfully!")
        self.window.destroy()

def main():
    app = BloodBankSystem()
    app.root.mainloop()

if __name__ == "__main__":
    main()