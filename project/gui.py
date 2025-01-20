import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO

# Dummy Data for Login
users = {
    "supervisor": {"password": "admin123", "role": "supervisor"},
    "donor1": {"password": "donor123", "role": "donor", "history": ["Blood Donation on 2024-12-01"]},
    "donor2": {"password": "donor456", "role": "donor", "history": []},
}

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
    tk.Button(dashboard, text="Post News", font=("Arial", 12), bg="#DC143C", fg="white", command=lambda: print("Post News")).pack(pady=5)
    dashboard.configure(bg="#FFCCCC")
    dashboard.mainloop()

# Donor Dashboard
def open_donor_dashboard(username):
    dashboard = tk.Tk()
    dashboard.title("Donor Dashboard")
    dashboard.geometry("800x600")
    tk.Label(dashboard, text="Donor Dashboard", font=("Arial", 20, "bold"), fg="white", bg="#8B0000").pack(fill="x")
    tk.Label(dashboard, text=f"Welcome, {username}!", font=("Arial", 14), fg="#8B0000").pack(pady=10)
    tk.Button(dashboard, text="View Donation History", font=("Arial", 12), bg="#DC143C", fg="white",
              command=lambda: messagebox.showinfo("History", "\n".join(users[username]["history"]))).pack(pady=5)
    dashboard.configure(bg="#FFCCCC")
    dashboard.mainloop()

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
