import requests
from io import BytesIO
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
import re

# Dummy Data for Login
users = {
    "supervisor": {"password": "admin123", "role": "supervisor"},
    "donor1": {"password": "donor123", "role": "donor", "history": ["Blood Donation on 2024-12-01"]},
    "donor2": {"password": "donor456", "role": "donor", "history": []},
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
        elif role == "donor":
            open_donor_dashboard(username)
    else:
        messagebox.showerror("Error", "Invalid username or password")

# Supervisor Dashboard
def open_supervisor_dashboard(username):
    dashboard = tk.Tk()
    dashboard.title("Supervisor Dashboard")
    dashboard.geometry("800x600")
    tk.Label(dashboard, text="Supervisor Dashboard", font=("Arial", 20, "bold"), fg="white", bg="#8B0000").pack(fill="x")
    tk.Label(dashboard, text="Add donation history and manage donors.", font=("Arial", 14), fg="#8B0000").pack(pady=10)
    
    tk.Button(dashboard, text="Manage Donors", font=("Arial", 12), bg="#DC143C", fg="white", command=lambda: manage_donors(dashboard)).pack(pady=5)
    tk.Button(dashboard, text="Post News", font=("Arial", 12), bg="#DC143C", fg="white", command=lambda: print("Post News")).pack(pady=5)
    
    dashboard.configure(bg="#FFCCCC")
    dashboard.mainloop()

def manage_donors(dashboard):
    manage_window = tk.Toplevel(dashboard)
    manage_window.title("Manage Donors")
    manage_window.geometry("600x400")

    donor_list = tk.Listbox(manage_window, height=10, width=50)
    for donor in donors:
        donor_list.insert(tk.END, donor.get('name', 'Unknown Donor'))
    donor_list.pack(pady=10)

    def update_donation_history():
        selected_donor_index = donor_list.curselection()
        if selected_donor_index:
            selected_donor = donors[selected_donor_index[0]]
            donor_name = selected_donor.get('name', 'Unknown Donor')
            new_donation = f"Blood Donation on {simpledialog.askstring('Date', 'Enter donation date (DD/MM/YY):')}"
            selected_donor['history'].append(new_donation)
            messagebox.showinfo("Success", f"Donation history updated for {donor_name}.")
        else:
            messagebox.showerror("Error", "Please select a donor.")

    tk.Button(manage_window, text="Update Donation History", font=("Arial", 12), bg="#8B0000", fg="white", command=update_donation_history).pack(pady=20)

# Donor Dashboard
def open_donor_dashboard(username):
    dashboard = tk.Tk()
    dashboard.title("Donor Dashboard")
    dashboard.geometry("800x600")
    tk.Label(dashboard, text="Donor Dashboard", font=("Arial", 20, "bold"), fg="white", bg="#8B0000").pack(fill="x")
    tk.Label(dashboard, text=f"Welcome, {username}!", font=("Arial", 14), fg="#8B0000").pack(pady=10)
    
    tk.Button(dashboard, text="View Donation History", font=("Arial", 12), bg="#DC143C", fg="white",
              command=lambda: messagebox.showinfo("History", "\n".join(users[username]["history"]))).pack(pady=5)
    
    tk.Button(dashboard, text="Profile", font=("Arial", 12), bg="#DC143C", fg="white", command=lambda: print("Edit Profile")).pack(pady=5)
    tk.Button(dashboard, text="Settings", font=("Arial", 12), bg="#DC143C", fg="white", command=lambda: print("Settings")).pack(pady=5)
    
    dashboard.configure(bg="#FFCCCC")
    dashboard.mainloop()

# Donor Registration Form
def open_donor_registration(dashboard):
    register_window = tk.Toplevel(dashboard)
    register_window.title("Donor Registration")
    register_window.geometry("500x600")
    
    tk.Label(register_window, text="Donor Registration", font=("Arial", 18, "bold")).pack(pady=10)

    # Donor Fields
    donor_fields = {
        "Name": "name", "Father Name": "father_name", "Surname": "surname", "Title": "title", "Date of Birth (DD/MM/YY)": "dob",
        "Age": "age", "Sex": "sex", "Occupation": "occupation", "City": "city", "Sub-city/Region": "sub_city", "Zone": "zone",
        "Woreda": "woreda", "Kebele": "kebele", "Residence Tel": "residence_tel", "Cellphone": "cellphone", "Organization": "organization",
        "Email": "email", "P.O. Box": "po_box"
    }
    
    donor_data = {}
    
    for label, field in donor_fields.items():
        tk.Label(register_window, text=f"{label}:", font=("Arial", 12)).pack(anchor="w", padx=10)
        donor_data[field] = tk.Entry(register_window, font=("Arial", 12), width=30)
        donor_data[field].pack(pady=5)

    # Validate and Register Button
    def register_donor():
        # Validate the fields
        if not re.match(r"^\d{10}$", donor_data["residence_tel"].get()):
            messagebox.showerror("Error", "Residence Tel must be 10 digits.")
            return
        if not re.match(r"^\d{10}$", donor_data["cellphone"].get()):
            messagebox.showerror("Error", "Cellphone must be 10 digits.")
            return
        if not re.match(r"^[a-zA-Z0-9._%+-]+@gmail\.com$", donor_data["email"].get()):
            messagebox.showerror("Error", "Email must end with @gmail.com.")
            return
        if len(donor_data["po_box"].get()) > 10:
            messagebox.showerror("Error", "P.O. Box cannot exceed 10 characters.")
            return

        # Create Donor Entry and add to donor list
        donor_info = {field: donor_data[field].get() for field in donor_fields.values()}
        donors.append(donor_info)
        messagebox.showinfo("Success", "Donor Registered Successfully!")
        register_window.destroy()

    tk.Button(register_window, text="Register Donor", font=("Arial", 12), bg="#8B0000", fg="white", command=register_donor).pack(pady=20)

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
