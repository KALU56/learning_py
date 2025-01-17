import tkinter as tk
from tkinter import messagebox


# Dummy Data for Login
users = {
    "supervisor": {"password": "admin123", "role": "supervisor"},
    "donor1": {"password": "donor123", "role": "donor", "history": ["Blood Donation on 2024-12-01"]},
    "donor2": {"password": "donor456", "role": "donor", "history": []},
}

donations = []  # List to store donation history


# Login Function
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username in users and users[username]["password"] == password:
        role = users[username]["role"]
        root.destroy()  # Close login window
        if role == "supervisor":
            open_supervisor_dashboard()
        elif role == "donor":
            open_donor_dashboard(username)
    else:
        messagebox.showerror("Error", "Invalid username or password")


# Supervisor Dashboard
def open_supervisor_dashboard():
    supervisor_dashboard = tk.Tk()
    supervisor_dashboard.title("Supervisor Dashboard")
    supervisor_dashboard.geometry("500x400")

    tk.Label(supervisor_dashboard, text="Supervisor Dashboard", font=("Arial", 16)).pack(pady=10)

    def add_donation():
        add_donation_window = tk.Toplevel(supervisor_dashboard)
        add_donation_window.title("Add Donation History")
        add_donation_window.geometry("400x300")

        tk.Label(add_donation_window, text="Donor Username:").pack(anchor="w", padx=20, pady=5)
        donor_entry = tk.Entry(add_donation_window, width=30)
        donor_entry.pack(padx=20)

        tk.Label(add_donation_window, text="Donation Date (YYYY-MM-DD):").pack(anchor="w", padx=20, pady=5)
        date_entry = tk.Entry(add_donation_window, width=30)
        date_entry.pack(padx=20)

        def save_donation():
            donor = donor_entry.get()
            date = date_entry.get()

            if donor in users and users[donor]["role"] == "donor":
                users[donor]["history"].append(f"Blood Donation on {date}")
                donations.append(f"{donor}: {date}")
                messagebox.showinfo("Success", "Donation history added!")
                add_donation_window.destroy()
            else:
                messagebox.showerror("Error", "Invalid donor username!")

        tk.Button(add_donation_window, text="Save", command=save_donation).pack(pady=10)

    def view_donations():
        view_window = tk.Toplevel(supervisor_dashboard)
        view_window.title("All Donations")
        view_window.geometry("400x400")

        tk.Label(view_window, text="All Donations", font=("Arial", 14)).pack(pady=10)
        if donations:
            for donation in donations:
                tk.Label(view_window, text=donation).pack(anchor="w", padx=20)
        else:
            tk.Label(view_window, text="No donations found!").pack()

    def post_news():
        post_news_window = tk.Toplevel(supervisor_dashboard)
        post_news_window.title("Post News")
        post_news_window.geometry("400x300")

        tk.Label(post_news_window, text="Post News", font=("Arial", 14)).pack(pady=10)
        news_entry = tk.Text(post_news_window, width=40, height=10)
        news_entry.pack(pady=10)

        def save_news():
            news = news_entry.get("1.0", "end-1c")
            if news.strip():
                messagebox.showinfo("Success", "News posted successfully!")
                post_news_window.destroy()
            else:
                messagebox.showerror("Error", "News content cannot be empty!")

        tk.Button(post_news_window, text="Post", command=save_news).pack(pady=10)

    tk.Button(supervisor_dashboard, text="Add Donation History", command=add_donation).pack(pady=10)
    tk.Button(supervisor_dashboard, text="View Donations", command=view_donations).pack(pady=10)
    tk.Button(supervisor_dashboard, text="Post News", command=post_news).pack(pady=10)

    supervisor_dashboard.mainloop()


# Donor Dashboard
def open_donor_dashboard(username):
    donor_dashboard = tk.Tk()
    donor_dashboard.title("Donor Dashboard")
    donor_dashboard.geometry("500x400")

    tk.Label(donor_dashboard, text=f"Welcome, {username}!", font=("Arial", 16)).pack(pady=10)

    def view_history():
        history_window = tk.Toplevel(donor_dashboard)
        history_window.title("Donation History")
        history_window.geometry("400x300")

        tk.Label(history_window, text="Your Donation History", font=("Arial", 14)).pack(pady=10)

        history = users[username]["history"]
        if history:
            for record in history:
                tk.Label(history_window, text=record).pack(anchor="w", padx=20)
        else:
            tk.Label(history_window, text="No donation history found!").pack()

    tk.Button(donor_dashboard, text="View Donation History", command=view_history).pack(pady=10)

    donor_dashboard.mainloop()


# Main Login Window
root = tk.Tk()
root.title("Blood Bank Login")
root.geometry("400x300")

tk.Label(root, text="Blood Bank Login", font=("Arial", 16)).pack(pady=20)

tk.Label(root, text="Username:").pack(anchor="w", padx=20)
username_entry = tk.Entry(root, width=30)
username_entry.pack(padx=20)

tk.Label(root, text="Password:").pack(anchor="w", padx=20)
password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack(padx=20)

tk.Button(root, text="Login", width=15, command=login).pack(pady=20)

root.mainloop()
