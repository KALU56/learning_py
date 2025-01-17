import tkinter as tk
from tkinter import messagebox

root = tk.Tk()  # Correct capitalization
root.title("Login")
root.geometry("400x400")

username_label = tk.Label(root, text="Username")
username_label.grid(row=0, column=0)

username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1)

password_label = tk.Label(root, text="Password")
password_label.grid(row=1, column=0)

password_entry = tk.Entry(root, show="*")  # Add 'show' to mask password input
password_entry.grid(row=1, column=1)
dashbord=tk.Tk()
dashbord.title("Dashbord")
dashbord.geometry("400x400")


def login():
    username = username_entry.get()
    password = password_entry.get()
    # if username == "admin" and password == "admin":
    #     print("Login successful")
    # else:
    #     print("Login failed")
    if not username or not password:
        messagebox.showerror("error","Please enter both username and password")
    
    else:
        root.distroy()
        dashbord.mainloop()
   
login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=2, column=0)

root.mainloop()
