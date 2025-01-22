import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from io import BytesIO
import requests
from PIL import Image, ImageTk
import re

# Dummy Data for Login and Donor Registration
users = {
    "supervisor": {"password": "admin123", "role": "supervisor"},
}

donors = []

# Function to fetch and convert the image
def fetch_image(url):
    response = requests.get(url)
    if response.status_code == 200:
        img_data = BytesIO(response.content)
        return Image.open(img_data)
    else:
        raise Exception("Failed to fetch image from URL")

# Login Function
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username in users and users[username]["password"] == password:
        role = users[username]["role"]
        root.destroy()  # Close login window
        if role == "supervisor":
            open_supervisor_dashboard(username)
    else:
        messagebox.showerror("Error", "Invalid username or password")

# Supervisor Dashboard
def open_supervisor_dashboard(username):
    dashboard = tk.Tk()
    dashboard.title("Supervisor Dashboard")
    dashboard.geometry("800x600")
    tk.Label(dashboard, text="Supervisor Dashboard", font=("Arial", 20, "bold"), fg="white", bg="#8B0000").pack(fill="x")
    
    tk.Button(dashboard, text="Register New Donor", font=("Arial", 12), bg="#DC143C", fg="white", command=lambda: open_donor_registration(dashboard)).pack(pady=5)
    tk.Label(dashboard, text="Donation Information Table", font=("Arial", 14)).pack(pady=10)

    # Create a Treeview for displaying donation information
    columns = ("D/N", "Name", "B/P", "Volume", "Screened By", "HGB", "Checked By", "Donation Type", "Bleed Time", "ABO & Rh", "Remark")
    tree = ttk.Treeview(dashboard, columns=columns, show="headings")
    
    for col in columns:
        tree.heading(col, text=col)

    tree.pack(fill="both", expand=True)

    dashboard.mainloop()

# Donor Registration Form
def open_donor_registration(dashboard):
    register_window = tk.Toplevel(dashboard)
    register_window.title("Donor Registration")
    register_window.geometry("600x600")

    # Add Scrollable Frame
    canvas = tk.Canvas(register_window)
    scrollbar = tk.Scrollbar(register_window, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Donor Fields (List of fields to register)
    donor_fields = {
        "First Name": "first_name", "Father Name": "father_name", "Surname": "surname", "Title": "title", 
        "Date of Birth (DD/MM/YY)": "dob", "Age": "age", "Sex": "sex", "Occupation": "occupation", 
        "City": "city", "Sub-city/Region": "sub_city", "Zone": "zone", "Woreda": "woreda", 
        "Kebele": "kebele", "Residence Tel": "residence_tel", "Cellphone": "cellphone", "Organization": "organization",
        "Email": "email", "P.O. Box (optional)": "po_box", "Donor Number": "donor_number"
    }

    donor_data = {}
    
    for label, field in donor_fields.items():
        tk.Label(scrollable_frame, text=f"{label}:", font=("Arial", 12)).pack(anchor="w", padx=10, pady=5)
        donor_data[field] = tk.Entry(scrollable_frame, font=("Arial", 12), width=30)
        donor_data[field].pack(pady=5)

    # Donation Information Fields (Blood pressure, volume, type, etc.)
    donation_fields = {
        "Blood Pressure (B/P)": "blood_pressure", "Volume": "volume", "Screened By": "screened_by",
        "HGB": "hgb", "Checked By": "checked_by", "Donation Type": "donation_type", "Bleed Time (start-end)": "bleed_time",
        "ABO & Rh": "abo_rh", "Remark": "remark"
    }
    
    donation_data = {}
    
    for label, field in donation_fields.items():
        tk.Label(scrollable_frame, text=f"{label}:", font=("Arial", 12)).pack(anchor="w", padx=10, pady=5)
        donation_data[field] = tk.Entry(scrollable_frame, font=("Arial", 12), width=30)
        donation_data[field].pack(pady=5)

    def validate_and_submit():
        # Validation of Blood Pressure
        if "Blood Pressure" in donation_data and donation_data["blood_pressure"].get() not in ["Normal", "Normal"]:
            messagebox.showinfo("Info", "Blood pressure not normal. Thank you for coming!")
            return

        # Create Donor Entry and add to donor list
        donor_info = {field: donor_data[field].get() for field in donor_fields.values()}
        donation_info = {field: donation_data[field].get() for field in donation_fields.values()}
        donor_info.update(donation_info)
        donors.append(donor_info)

        messagebox.showinfo("Success", "Donor Registered Successfully!")
        register_window.destroy()

    # Submit Button
    tk.Button(scrollable_frame, text="Submit", font=("Arial", 12), bg="#8B0000", fg="white", command=validate_and_submit).pack(pady=20)

    # Pack the canvas and scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

# Main Login Window
root = tk.Tk()
root.title("Blood Bank Login")
root.geometry("800x600")

# Fetch and set the background image
url = "https://images.pexels.com/photos/4531306/pexels-photo-4531306.jpeg?auto=compress&cs=tinysrgb&w=400"
bg_image = fetch_image(url)
bg_image = bg_image.resize((800, 600))  # Resize to match the window size
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

# Overlay form
form_frame = tk.Frame(root, bg="#FFCCCC", bd=2, relief="ridge")
form_frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=300)

# Title
tk.Label(form_frame, text="Blood Bank Login", font=("Arial", 18, "bold"), bg="#8B0000", fg="white").pack(pady=10, fill="x")

# Username
tk.Label(form_frame, text="Username:", font=("Arial", 12), bg="#FFCCCC").pack(anchor="w", padx=20)
username_entry = tk.Entry(form_frame, font=("Arial", 12), width=30)
username_entry.pack(pady=5)

# Password
tk.Label(form_frame, text="Password:", font=("Arial", 12), bg="#FFCCCC").pack(anchor="w", padx=20)
password_entry = tk.Entry(form_frame, font=("Arial", 12), show="*", width=30)
password_entry.pack(pady=5)

# Login Button
tk.Button(form_frame, text="Login", font=("Arial", 12), bg="#8B0000", fg="white", width=20, command=login).pack(pady=20)

root.mainloop()
