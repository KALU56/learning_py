import tkinter as tk
from tkinter import ttk, messagebox
from io import BytesIO
import requests
from PIL import Image, ImageTk
import re

# Dummy Data for Login and Donor Management
users = {
    "supervisor": {"password": "admin123", "role": "supervisor"},
}

donors = []

def fetch_image(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            img_data = BytesIO(response.content)
            return Image.open(img_data)
    except Exception as e:
        print(f"Error fetching image: {e}")
    return None

# Login Function
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username in users and users[username]["password"] == password:
        role = users[username]["role"]
        root.destroy()
        if role == "supervisor":
            open_supervisor_dashboard(username)
    else:
        messagebox.showerror("Error", "Invalid username or password")

# Supervisor Dashboard
def open_supervisor_dashboard(username):
    dashboard = tk.Tk()
    dashboard.title("Supervisor Dashboard")
    dashboard.geometry("900x600")

    # Dashboard Header
    tk.Label(dashboard, text=f"Welcome, {username}", font=("Arial", 16), fg="white", bg="#8B0000").pack(fill="x")

    # Buttons for actions
    btn_frame = tk.Frame(dashboard)
    btn_frame.pack(pady=10)

    tk.Button(btn_frame, text="Register New Donor", font=("Arial", 12), bg="#DC143C", fg="white", 
              command=lambda: open_donor_registration(dashboard)).grid(row=0, column=0, padx=10)
    tk.Button(btn_frame, text="View All Donations", font=("Arial", 12), bg="#DC143C", fg="white", 
              command=lambda: view_all_donations(dashboard)).grid(row=0, column=1, padx=10)
    tk.Button(btn_frame, text="Event Announcements", font=("Arial", 12), bg="#DC143C", fg="white", 
              command=lambda: manage_events(dashboard)).grid(row=0, column=2, padx=10)

    # Table to display summary
    columns = ("D/N", "Name", "B/P", "Volume", "Donation Type", "Remark")
    tree = ttk.Treeview(dashboard, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=150)

    tree.pack(fill="both", expand=True, pady=10)

    # Populate with donor data
    for donor in donors:
        tree.insert("", "end", values=(
            donor.get("donor_number", ""),
            donor.get("first_name", "") + " " + donor.get("surname", ""),
            donor.get("blood_pressure", ""),
            donor.get("volume", ""),
            donor.get("donation_type", ""),
            donor.get("remark", "")
        ))

    dashboard.mainloop()

# Donor Registration Form
def open_donor_registration(dashboard):
    register_window = tk.Toplevel(dashboard)
    register_window.title("Donor Registration")
    register_window.geometry("600x700")

    # Scrollable Frame
    canvas = tk.Canvas(register_window)
    scrollbar = tk.Scrollbar(register_window, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    donor_fields = {
        "First Name": "first_name", "Father Name": "father_name", "Surname": "surname", "Title": "title", 
        "Date of Birth (DD/MM/YY)": "dob", "Age": "age", "Sex": "sex", "Occupation": "occupation", 
        "City": "city", "Sub-city/Region": "sub_city", "Blood Pressure (B/P)": "blood_pressure", 
        "Volume": "volume", "Donation Type": "donation_type", "Remark": "remark"
    }

    donor_data = {}
    for label, field in donor_fields.items():
        tk.Label(scrollable_frame, text=label, font=("Arial", 12)).pack(anchor="w", padx=10, pady=5)
        donor_data[field] = tk.Entry(scrollable_frame, font=("Arial", 12), width=30)
        donor_data[field].pack(pady=5)

    def validate_and_submit():
        if not re.match(r"\d{2}/\d{2}/\d{4}", donor_data["dob"].get()):
            messagebox.showerror("Error", "Invalid date format. Use DD/MM/YYYY.")
            return

        if donor_data["blood_pressure"].get() not in ["Normal", "normal"]:
            messagebox.showinfo("Info", "Blood pressure not normal. Thank you for coming!")
            return

        donor_info = {field: donor_data[field].get() for field in donor_fields.values()}
        donors.append(donor_info)
        messagebox.showinfo("Success", "Donor Registered Successfully!")
        register_window.destroy()

    tk.Button(scrollable_frame, text="Submit", font=("Arial", 12), bg="#8B0000", fg="white", 
              command=validate_and_submit).pack(pady=20)

# View All Donations
def view_all_donations(dashboard):
    view_window = tk.Toplevel(dashboard)
    view_window.title("All Donations")
    view_window.geometry("800x600")

    columns = ("D/N", "Name", "B/P", "Volume", "Donation Type", "Remark")
    tree = ttk.Treeview(view_window, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=150)

    tree.pack(fill="both", expand=True, pady=10)

    for donor in donors:
        tree.insert("", "end", values=(
            donor.get("donor_number", ""),
            donor.get("first_name", "") + " " + donor.get("surname", ""),
            donor.get("blood_pressure", ""),
            donor.get("volume", ""),
            donor.get("donation_type", ""),
            donor.get("remark", "")
        ))

# Event Announcements
def manage_events(dashboard):
    event_window = tk.Toplevel(dashboard)
    event_window.title("Event Announcements")
    event_window.geometry("500x400")

    tk.Label(event_window, text="Post New Event", font=("Arial", 14)).pack(pady=10)
    event_title = tk.Entry(event_window, font=("Arial", 12), width=40)
    event_title.pack(pady=5)

    event_desc = tk.Text(event_window, font=("Arial", 12), width=40, height=10)
    event_desc.pack(pady=10)

    def post_event():
        title = event_title.get()
        desc = event_desc.get("1.0", "end").strip()
        if not title or not desc:
            messagebox.showerror("Error", "Both fields are required.")
            return
        messagebox.showinfo("Success", "Event posted successfully!")
        event_window.destroy()

    tk.Button(event_window, text="Post Event", font=("Arial", 12), bg="#8B0000", fg="white", 
              command=post_event).pack(pady=10)

# Main Login Window
root = tk.Tk()
root.title("Blood Bank Login")
root.geometry("800x600")

bg_image_url = "https://images.pexels.com/photos/4531306/pexels-photo-4531306.jpeg?auto=compress&cs=tinysrgb&w=800"
bg_image = fetch_image(bg_image_url)
if bg_image:
    bg_image = bg_image.resize((800, 600))
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(relwidth=1, relheight=1)

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
