import tkinter as tk
from tkinter import ttk, messagebox

# Function to handle registration
def register():
    # Collect all form data
    data = {
        "First Name": first_name.get(),
        "Father Name": father_name.get(),
        "Sex": sex.get(),
        "Age": age.get(),
        "Department": department.get(),
        "Highest Education Level": highest_education_level.get(),
        "Hobbies": ", ".join([hobby for hobby, var in hobbies.items() if var.get()]),
        "Remark": remark.get()
    }
    # Check if mandatory fields are filled
    if not data["First Name"] or not data["Father Name"] or data["Sex"] == "None" or data["Department"] == "Select Department":
        messagebox.showerror("Error", "Please fill all mandatory fields!")
        return
    # Show success message
    messagebox.showinfo("Success", "Registration Successful!\n" + "\n".join([f"{k}: {v}" for k, v in data.items()]))

# Function to clear form
def clear():
    first_name.delete(0, tk.END)
    father_name.delete(0, tk.END)
    sex.set("None")
    age.set(0)
    department.set("Select Department")
    highest_education_level.set("Select Level")
    for var in hobbies.values():
        var.set(False)
    remark.delete(0, tk.END)

# Root window
root = tk.Tk()
root.title("Employee Registration Form")
root.geometry("600x600")

# Form title
tk.Label(root, text="Employee Registration Form", font=("Arial", 20)).grid(row=0, column=0, columnspan=3, pady=10)

# Form fields
# First Name
tk.Label(root, text="First Name").grid(row=1, column=0, padx=10, pady=5, sticky="w")
first_name = tk.Entry(root)
first_name.grid(row=1, column=1, columnspan=2, padx=10, pady=5)

# Father Name
tk.Label(root, text="Father's Name").grid(row=2, column=0, padx=10, pady=5, sticky="w")
father_name = tk.Entry(root)
father_name.grid(row=2, column=1, columnspan=2, padx=10, pady=5)

# Sex
tk.Label(root, text="Sex").grid(row=3, column=0, padx=10, pady=5, sticky="w")
sex = tk.StringVar(value="None")
tk.Radiobutton(root, text="Male", value="Male", variable=sex).grid(row=3, column=1, padx=10, pady=5)
tk.Radiobutton(root, text="Female", value="Female", variable=sex).grid(row=3, column=2, padx=10, pady=5)

# Age
tk.Label(root, text="Age").grid(row=4, column=0, padx=10, pady=5, sticky="w")
age = tk.IntVar(value=0)
tk.Spinbox(root, from_=0, to=100, textvariable=age).grid(row=4, column=1, columnspan=2, padx=10, pady=5)

# Department
tk.Label(root, text="Department").grid(row=5, column=0, padx=10, pady=5, sticky="w")
department = ttk.Combobox(root, values=["Select Department", "SE", "HR", "IT", "Marketing", "Finance"])
department.set("Select Department")
department.grid(row=5, column=1, columnspan=2, padx=10, pady=5)

# Highest Education Level
tk.Label(root, text="Highest Education Level").grid(row=6, column=0, padx=10, pady=5, sticky="w")
highest_education_level = ttk.Combobox(root, values=["Select Level", "High School", "Bachelor's", "Master's", "PhD"])
highest_education_level.set("Select Level")
highest_education_level.grid(row=6, column=1, columnspan=2, padx=10, pady=5)

# Hobbies
tk.Label(root, text="Hobbies").grid(row=7, column=0, padx=10, pady=5, sticky="w")
hobbies = {
    "Playing Football": tk.BooleanVar(),
    "Playing Cricket": tk.BooleanVar(),
    "Reading": tk.BooleanVar(),
    "Writing": tk.BooleanVar()
}
col = 1
for hobby, var in hobbies.items():
    tk.Checkbutton(root, text=hobby, variable=var).grid(row=7, column=col, padx=5, pady=5, sticky="w")
    col += 1

# Remark
tk.Label(root, text="Remark").grid(row=8, column=0, padx=10, pady=5, sticky="w")
remark = tk.Entry(root)
remark.grid(row=8, column=1, columnspan=2, padx=10, pady=5)

# Buttons
tk.Button(root, text="Register", bg="green", fg="white", command=register).grid(row=9, column=0, padx=10, pady=20)
tk.Button(root, text="Clear", bg="red", fg="white", command=clear).grid(row=9, column=1, padx=10, pady=20)

# Start main loop
root.mainloop()
