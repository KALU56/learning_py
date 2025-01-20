import tkinter as tk
from tkinter import ttk, messagebox
import re
from datetime import datetime
import urllib.request
from PIL import Image, ImageTk
import io

class BloodDonationSystem:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Blood Donation System")
        self.root.geometry("1000x700")
        
        # Define colors
        self.primary_red = "#DC3545"
        self.light_red = "#F8D7DA"
        
        # Load background image
        try:
            # Use a different URL or local image
            url = "https://raw.githubusercontent.com/your-username/your-repo/main/background.jpg"
            # Or use a local file:
            # self.bg_image = ImageTk.PhotoImage(Image.open("path/to/local/background.jpg"))
            image_bytes = urllib.request.urlopen(url).read()
            image = Image.open(io.BytesIO(image_bytes))
            image = image.resize((1000, 700), Image.Resampling.LANCZOS)
            self.bg_image = ImageTk.PhotoImage(image)
            
            # Create background label
            bg_label = tk.Label(self.root, image=self.bg_image)
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception as e:
            print(f"Error loading background: {e}")
            # Create a solid color background as fallback
            bg_label = tk.Label(self.root, bg='#f0f0f0')
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.create_login_frame()
        
    def create_login_frame(self):
        # Create semi-transparent overlay (using solid color instead)
        overlay = tk.Frame(self.root, bg='#000000')
        overlay.place(relx=0, rely=0, relwidth=1, relheight=1)
        overlay.configure(bg='#404040')  # Changed from #00000055 to solid color
        
        # Create modern login container
        login_container = tk.Frame(self.root, bg='white')
        login_container.place(relx=0.5, rely=0.5, anchor='center', width=400, height=500)
        
        # Add rounded corners and shadow effect (using multiple frames)
        for i in range(5):
            shadow = tk.Frame(login_container, bg='#00000011')
            shadow.place(x=-i, y=-i, width=400+i*2, height=500+i*2)
        
        # Logo/Icon at the top
        logo_frame = tk.Frame(login_container, bg='white')
        logo_frame.pack(pady=20)
        
        logo_label = tk.Label(logo_frame, text="🩸", font=('Arial', 50), bg='white')
        logo_label.pack()
        
        # Title
        title_frame = tk.Frame(login_container, bg='white')
        title_frame.pack(pady=10)
        
        tk.Label(title_frame, text="Blood Bank System",
                font=('Arial', 24, 'bold'),
                fg=self.primary_red, bg='white').pack()
        
        tk.Label(title_frame, text="Login to your account",
                font=('Arial', 12),
                fg='gray', bg='white').pack(pady=5)
        
        # User type selection with custom style
        selection_frame = tk.Frame(login_container, bg='white')
        selection_frame.pack(pady=20)
        
        user_type = ttk.Combobox(selection_frame, 
                                values=['Supervisor', 'Donor'],
                                state='readonly', 
                                width=25,
                                font=('Arial', 12))
        user_type.set('Select User Type')
        
        # Style the combobox
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TCombobox', 
                       fieldbackground='white',
                       background='white',
                       selectbackground=self.primary_red,
                       selectforeground='white')
        
        user_type.pack()
        
        # Username field with icon
        username_frame = tk.Frame(login_container, bg='white')
        username_frame.pack(pady=10)
        
        tk.Label(username_frame, text="👤", font=('Arial', 12),
                bg='white').pack(side='left', padx=5)
        username_entry = tk.Entry(username_frame, 
                                font=('Arial', 12),
                                width=25,
                                bd=0,
                                highlightthickness=1,
                                highlightbackground='#ddd')
        username_entry.insert(0, "Username")
        username_entry.pack(side='left')
        
        # Password field with icon
        password_frame = tk.Frame(login_container, bg='white')
        password_frame.pack(pady=10)
        
        tk.Label(password_frame, text="🔒", font=('Arial', 12),
                bg='white').pack(side='left', padx=5)
        password_entry = tk.Entry(password_frame,
                                font=('Arial', 12),
                                width=25,
                                bd=0,
                                show="•",
                                highlightthickness=1,
                                highlightbackground='#ddd')
        password_entry.insert(0, "Password")
        password_entry.pack(side='left')
        
        # Remember me checkbox
        remember_frame = tk.Frame(login_container, bg='white')
        remember_frame.pack(pady=10)
        
        remember_var = tk.BooleanVar()
        remember_cb = tk.Checkbutton(remember_frame,
                                    text="Remember me",
                                    variable=remember_var,
                                    bg='white',
                                    fg=self.primary_red,
                                    selectcolor=self.primary_red)
        remember_cb.pack(side='left')
        
        # Login button with hover effect
        login_button = tk.Button(login_container,
                                text="LOGIN",
                                font=('Arial', 12, 'bold'),
                                bg=self.primary_red,
                                fg='white',
                                bd=0,
                                width=20,
                                height=2,
                                cursor='hand2',
                                command=lambda: self.handle_login(user_type.get()))
        login_button.pack(pady=20)
        
        # Add hover effect
        def on_enter(e):
            login_button['background'] = '#990000'
        
        def on_leave(e):
            login_button['background'] = self.primary_red
        
        login_button.bind("<Enter>", on_enter)
        login_button.bind("<Leave>", on_leave)
        
        # Register link
        register_frame = tk.Frame(login_container, bg='white')
        register_frame.pack(pady=10)
        
        tk.Label(register_frame,
                 text="Don't have an account?",
                 font=('Arial', 10),
                 bg='white',
                 fg='gray').pack(side='left')
        
        register_link = tk.Label(register_frame,
                                text="Register",
                                font=('Arial', 10, 'bold'),
                                bg='white',
                                fg=self.primary_red,
                                cursor='hand2')
        register_link.pack(side='left', padx=5)
        
        # Add hover effect for register link
        def on_enter_link(e):
            register_link['font'] = ('Arial', 10, 'bold', 'underline')
        
        def on_leave_link(e):
            register_link['font'] = ('Arial', 10, 'bold')
        
        register_link.bind("<Enter>", on_enter_link)
        register_link.bind("<Leave>", on_leave_link)
        register_link.bind("<Button-1>", lambda e: self.show_donor_registration())
        
        # Field focus events
        def on_entry_click(event, entry, default_text):
            if entry.get() == default_text:
                entry.delete(0, "end")
                if entry == password_entry:
                    entry.config(show="•")
        
        def on_focusout(event, entry, default_text):
            if entry.get() == '':
                entry.insert(0, default_text)
                if entry == password_entry and entry.get() == default_text:
                    entry.config(show="")
        
        # Bind focus events
        username_entry.bind('<FocusIn>', lambda e: on_entry_click(e, username_entry, "Username"))
        username_entry.bind('<FocusOut>', lambda e: on_focusout(e, username_entry, "Username"))
        password_entry.bind('<FocusIn>', lambda e: on_entry_click(e, password_entry, "Password"))
        password_entry.bind('<FocusOut>', lambda e: on_focusout(e, password_entry, "Password"))
        
        # Initially show password as text since it's the default value
        password_entry.config(show="")
        
    def handle_login(self, user_type):
        if user_type == 'Supervisor':
            self.show_supervisor_dashboard()
        elif user_type == 'Donor':
            self.show_donor_login()
        else:
            messagebox.showerror("Error", "Please select a user type")
            
    def show_donor_login(self):
        # Clear current window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Create login frame
        login_frame = tk.Frame(self.root, bg='white')
        login_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        # Title
        title = tk.Label(login_frame, text="Donor Login",
                        font=('Arial', 24, 'bold'),
                        fg=self.primary_red, bg='white')
        title.pack(pady=20)
        
        # Login fields
        username = tk.StringVar()
        password = tk.StringVar()
        
        tk.Label(login_frame, text="Username:", bg='white').pack()
        tk.Entry(login_frame, textvariable=username, width=30).pack()
        
        tk.Label(login_frame, text="Password:", bg='white').pack()
        tk.Entry(login_frame, textvariable=password, show='*', width=30).pack()
        
        # Login button
        login_btn = tk.Button(login_frame, text="Login",
                             bg=self.primary_red, fg='white',
                             command=lambda: self.authenticate_donor(username.get(), password.get()))
        login_btn.pack(pady=20)
        
        # Register button
        register_btn = tk.Button(login_frame, text="New Donor? Register",
                                bg='gray', fg='white',
                                command=self.show_donor_registration)
        register_btn.pack()

    def authenticate_donor(self, username, password):
        # In a real application, this would check against a database
        # For demonstration, we'll show the donor dashboard
        self.show_donor_dashboard(username)

    def show_donor_registration(self):
        # Clear current window
        for widget in self.root.winfo_children():
            widget.destroy()
            
        # Create main container with scroll
        main_container = tk.Frame(self.root)
        main_container.pack(fill='both', expand=True)
        
        # Create canvas and scrollbar
        canvas = tk.Canvas(main_container)
        scrollbar = ttk.Scrollbar(main_container, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)
        
        # Configure the canvas
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Pack the scrollbar and canvas
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        
        # Add mouse wheel scrolling
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        canvas.bind_all("<MouseWheel>", _on_mousewheel)
        
        # Create registration frame
        reg_frame = tk.Frame(scrollable_frame, bg='white')
        reg_frame.pack(padx=20, pady=20)
        
        # Title
        title = tk.Label(reg_frame, text="Donor Registration",
                        font=('Arial', 24, 'bold'),
                        fg=self.primary_red, bg='white')
        title.pack(pady=20)
        
        # Form fields
        fields = {
            'name': tk.StringVar(),
            'city': tk.StringVar(),
            'email': tk.StringVar(),
            'gender': tk.StringVar(),
            'dob': tk.StringVar(),
            'phone': tk.StringVar(),
            'username': tk.StringVar(),
            'password': tk.StringVar()
        }
        
        # Create form entries
        tk.Label(reg_frame, text="Full Name:", bg='white').pack()
        tk.Entry(reg_frame, textvariable=fields['name'], width=30).pack()
        
        tk.Label(reg_frame, text="City:", bg='white').pack()
        tk.Entry(reg_frame, textvariable=fields['city'], width=30).pack()
        
        tk.Label(reg_frame, text="Email:", bg='white').pack()
        tk.Entry(reg_frame, textvariable=fields['email'], width=30).pack()
        
        tk.Label(reg_frame, text="Gender:", bg='white').pack()
        gender_cb = ttk.Combobox(reg_frame, textvariable=fields['gender'],
                                values=['Male', 'Female'], state='readonly')
        gender_cb.pack()
        
        tk.Label(reg_frame, text="Date of Birth (YYYY-MM-DD):", bg='white').pack()
        tk.Entry(reg_frame, textvariable=fields['dob'], width=30).pack()
        
        tk.Label(reg_frame, text="Phone:", bg='white').pack()
        tk.Entry(reg_frame, textvariable=fields['phone'], width=30).pack()
        
        tk.Label(reg_frame, text="Username:", bg='white').pack()
        tk.Entry(reg_frame, textvariable=fields['username'], width=30).pack()
        
        tk.Label(reg_frame, text="Password:", bg='white').pack()
        tk.Entry(reg_frame, textvariable=fields['password'], show='*', width=30).pack()
        
        # Submit button
        submit_btn = tk.Button(reg_frame, text="Submit",
                             bg=self.primary_red, fg='white',
                             command=lambda: self.validate_registration(fields))
        submit_btn.pack(pady=20)
        
    def validate_registration(self, fields):
        # Email validation
        email_pattern = r'^[A-Za-z0-9+_.-]+@gmail\.com$'
        if not re.match(email_pattern, fields['email'].get()):
            messagebox.showerror("Error", "Email must end with @gmail.com")
            return
        
        # Age validation
        try:
            dob = datetime.strptime(fields['dob'].get(), '%Y-%m-%d')
            age = (datetime.now() - dob).days / 365
            if age < 18:
                messagebox.showerror("Error", "Must be 18 or older to register")
                return
        except ValueError:
            messagebox.showerror("Error", "Invalid date format")
            return
        
        # Phone validation
        phone_pattern = r'^(07|09)\d{8}$'
        if not re.match(phone_pattern, fields['phone'].get()):
            messagebox.showerror("Error", "Phone must be 10 digits and start with 07 or 09")
            return
        
        # Store user credentials (in a real app, this would go to a database)
        self.store_user_credentials(fields['username'].get(), fields['password'].get())
        
        # Show medical form
        self.show_medical_form()
        
    def store_user_credentials(self, username, password):
        # In a real application, this would store to a database
        # For now, we'll just print
        print(f"Stored credentials for user: {username}")
        
    def show_medical_form(self):
        # Clear current window
        for widget in self.root.winfo_children():
            widget.destroy()
            
        # Create medical form frame
        med_frame = tk.Frame(self.root, bg='white')
        med_frame.place(relx=0.5, rely=0.1, anchor='n')
        
        # Title
        title = tk.Label(med_frame, text="Medical Information (Optional)",
                        font=('Arial', 24, 'bold'),
                        fg=self.primary_red, bg='white')
        title.pack(pady=20)
        
        # Medical form fields
        fields = {
            'blood_type': tk.StringVar(),
            'health_status': tk.StringVar(),
            'blood_pressure': tk.StringVar(),
            'sugar': tk.StringVar()
        }
        
        # Create medical form entries
        tk.Label(med_frame, text="Blood Type:", bg='white').pack()
        blood_type_cb = ttk.Combobox(med_frame, textvariable=fields['blood_type'],
                                    values=['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'])
        blood_type_cb.pack()
        
        tk.Label(med_frame, text="Health Status:", bg='white').pack()
        tk.Entry(med_frame, textvariable=fields['health_status'], width=30).pack()
        
        tk.Label(med_frame, text="Blood Pressure:", bg='white').pack()
        tk.Entry(med_frame, textvariable=fields['blood_pressure'], width=30).pack()
        
        tk.Label(med_frame, text="Sugar Level:", bg='white').pack()
        tk.Entry(med_frame, textvariable=fields['sugar'], width=30).pack()
        
        # Submit button
        submit_btn = tk.Button(med_frame, text="Submit Donation Request",
                             bg=self.primary_red, fg='white',
                             command=lambda: self.submit_donation_request(fields))
        submit_btn.pack(pady=20)
        
        # Skip button
        skip_btn = tk.Button(med_frame, text="Skip",
                           bg='gray', fg='white',
                           command=lambda: self.show_donor_dashboard("New Donor"))
        skip_btn.pack(pady=10)

    def submit_donation_request(self, fields):
        # In a real application, this would save to a database
        messagebox.showinfo("Success", "Donation request submitted successfully! Please wait for supervisor review.")
        self.show_donor_dashboard("New Donor")

    def show_supervisor_dashboard(self):
        # Clear current window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Create main container
        container = tk.Frame(self.root)
        container.pack(fill='both', expand=True)
        
        # Create left navigation bar with icons
        nav_bar = tk.Frame(container, bg=self.primary_red, width=200)
        nav_bar.pack(side='left', fill='y')
        nav_bar.pack_propagate(False)
        
        # Title in nav bar
        title_frame = tk.Frame(nav_bar, bg=self.primary_red)
        title_frame.pack(fill='x', pady=20)
        tk.Label(title_frame, text="Blood Bank", font=('Arial', 16, 'bold'),
                 bg=self.primary_red, fg='white').pack()
        
        # Navigation buttons with icons
        nav_buttons = [
            ("📊 Dashboard", self.show_registered_donors),
            ("🩸 Donations", self.show_registered_donors),
            ("📋 Reports", self.show_medical_results_form),
            ("⚙️ Settings", lambda: None),
            ("↪️ Logout", self.handle_logout)
        ]
        
        for text, command in nav_buttons:
            btn = tk.Button(nav_bar, text=text, bg=self.primary_red, fg='white',
                           bd=0, pady=15, font=('Arial', 12),
                           activebackground='#990000', activeforeground='white',
                           command=command)
            btn.pack(fill='x', padx=5, pady=2)
        
        # Create main content area
        main_area = tk.Frame(container, bg='white')
        main_area.pack(side='right', fill='both', expand=True)
        
        # Create top stats section
        stats_frame = tk.Frame(main_area, bg='white')
        stats_frame.pack(fill='x', padx=20, pady=20)
        
        stats = [
            ("Total Donors", "150", "👥"),
            ("Today's Donations", "12", "🩸"),
            ("Pending Requests", "5", "⏳")
        ]
        
        for title, count, icon in stats:
            stat_box = tk.Frame(stats_frame, bg=self.primary_red, padx=20, pady=10)
            stat_box.pack(side='left', padx=10)
            
            tk.Label(stat_box, text=icon, font=('Arial', 24),
                    bg=self.primary_red, fg='white').pack()
            tk.Label(stat_box, text=count, font=('Arial', 24, 'bold'),
                    bg=self.primary_red, fg='white').pack()
            tk.Label(stat_box, text=title, font=('Arial', 12),
                    bg=self.primary_red, fg='white').pack()
        
        # Search section
        search_frame = tk.Frame(main_area, bg='white')
        search_frame.pack(fill='x', padx=20, pady=10)
        
        tk.Entry(search_frame, width=40, font=('Arial', 12)).pack(side='left', padx=5)
        tk.Button(search_frame, text="Search", bg=self.primary_red, fg='white',
                  font=('Arial', 10)).pack(side='left', padx=5)
        
        # Create content frame for donor list
        self.content_frame = tk.Frame(main_area, bg='white')
        self.content_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Show donor list by default
        self.show_registered_donors()

    def show_registered_donors(self):
        # Clear content frame
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # Create table frame with modern styling
        table_frame = tk.Frame(self.content_frame, bg='white')
        table_frame.pack(fill='both', expand=True)
        
        # Add title and new donor button
        header_frame = tk.Frame(table_frame, bg='white')
        header_frame.pack(fill='x', pady=10)
        
        tk.Label(header_frame, text="Registered Donors", font=('Arial', 16, 'bold'),
                 bg='white', fg=self.primary_red).pack(side='left')
        
        tk.Button(header_frame, text="+ New Donor", bg=self.primary_red, fg='white',
                  font=('Arial', 10)).pack(side='right')
        
        # Create scrollable table
        table_container = tk.Frame(table_frame)
        table_container.pack(fill='both', expand=True)
        
        # Create canvas with scrollbar
        canvas = tk.Canvas(table_container, bg='white')
        scrollbar = ttk.Scrollbar(table_container, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='white')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Headers
        headers = ['Name', 'City', 'Email', 'Gender', 'Phone', 'Blood Type', 'Status', 'Actions']
        for i, header in enumerate(headers):
            tk.Label(scrollable_frame, text=header, bg=self.primary_red, fg='white',
                    font=('Arial', 10, 'bold'), padx=10, pady=5, width=15).grid(row=0, column=i, sticky='nsew')
        
        # Sample data
        sample_data = [
            ['John Doe', 'City A', 'john@gmail.com', 'Male', '0712345678', 'A+', 'Pending'],
            ['Jane Doe', 'City B', 'jane@gmail.com', 'Female', '0798765432', 'B-', 'Completed']
        ]
        
        for i, row in enumerate(sample_data, 1):
            for j, value in enumerate(row):
                bg_color = '#F8D7DA' if row[6] == 'Pending' else 'white'
                tk.Label(scrollable_frame, text=value, bg=bg_color,
                        font=('Arial', 10), padx=10, pady=5, width=15).grid(row=i, column=j, sticky='nsew')
            
            # Action buttons
            action_frame = tk.Frame(scrollable_frame, bg='white')
            action_frame.grid(row=i, column=len(row), sticky='nsew')
            
            tk.Button(action_frame, text='View', bg=self.primary_red, fg='white',
                     font=('Arial', 8)).pack(side='left', padx=2)
            tk.Button(action_frame, text='Send Results', bg=self.primary_red, fg='white',
                     font=('Arial', 8)).pack(side='left', padx=2)
        
        # Pack canvas and scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def show_medical_results_form(self, donor=None):
        # Clear content frame
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # Create a canvas with scrollbar
        canvas = tk.Canvas(self.content_frame, bg='white')
        scrollbar = ttk.Scrollbar(self.content_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='white')
        
        # Configure the canvas
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Pack the scrollbar and canvas
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        
        # Create form
        form_frame = tk.Frame(scrollable_frame, bg='white')
        form_frame.pack(padx=20, pady=20, fill='both', expand=True)
        
        # Add mouse wheel scrolling
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        canvas.bind_all("<MouseWheel>", _on_mousewheel)
        
        # Rest of the medical results form code remains the same
        tk.Label(form_frame, text="Send Medical Results", font=('Arial', 18, 'bold'),
                bg='white', fg=self.primary_red).pack(pady=10)
        
        # Form fields
        fields = {
            'donor_email': tk.StringVar(value=donor[2] if donor else ''),
            'blood_type': tk.StringVar(),
            'health_status': tk.StringVar(),
            'blood_pressure': tk.StringVar(),
            'sugar': tk.StringVar(),
            'hiv_status': tk.StringVar(),
            'syphilis_status': tk.StringVar(),
            'hepatitis_b': tk.StringVar(),
            'hepatitis_c': tk.StringVar(),
            'hemoglobin': tk.StringVar(),
            'malaria': tk.StringVar(),
            'donation_status': tk.StringVar(),
            'additional_notes': tk.StringVar()
        }
        
        # Create form entries
        tk.Label(form_frame, text="Donor Email:", bg='white').pack()
        tk.Entry(form_frame, textvariable=fields['donor_email'], width=30).pack()
        
        tk.Label(form_frame, text="Blood Type:", bg='white').pack()
        blood_type_cb = ttk.Combobox(form_frame, textvariable=fields['blood_type'],
                                    values=['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'])
        blood_type_cb.pack()
        
        # Basic health metrics
        tk.Label(form_frame, text="Health Status:", bg='white').pack()
        tk.Entry(form_frame, textvariable=fields['health_status'], width=30).pack()
        
        tk.Label(form_frame, text="Blood Pressure:", bg='white').pack()
        tk.Entry(form_frame, textvariable=fields['blood_pressure'], width=30).pack()
        
        tk.Label(form_frame, text="Sugar Level:", bg='white').pack()
        tk.Entry(form_frame, textvariable=fields['sugar'], width=30).pack()
        
        # Blood test results
        test_frame = tk.LabelFrame(form_frame, text="Blood Test Results", bg='white')
        test_frame.pack(pady=10, fill='x')
        
        # HIV Status
        tk.Label(test_frame, text="HIV Status:", bg='white').pack()
        hiv_cb = ttk.Combobox(test_frame, textvariable=fields['hiv_status'],
                             values=['Negative', 'Positive'], state='readonly')
        hiv_cb.pack()
        
        # Syphilis Status
        tk.Label(test_frame, text="Syphilis Status:", bg='white').pack()
        syphilis_cb = ttk.Combobox(test_frame, textvariable=fields['syphilis_status'],
                                  values=['Negative', 'Positive'], state='readonly')
        syphilis_cb.pack()
        
        # Hepatitis B
        tk.Label(test_frame, text="Hepatitis B:", bg='white').pack()
        hep_b_cb = ttk.Combobox(test_frame, textvariable=fields['hepatitis_b'],
                               values=['Negative', 'Positive'], state='readonly')
        hep_b_cb.pack()
        
        # Hepatitis C
        tk.Label(test_frame, text="Hepatitis C:", bg='white').pack()
        hep_c_cb = ttk.Combobox(test_frame, textvariable=fields['hepatitis_c'],
                               values=['Negative', 'Positive'], state='readonly')
        hep_c_cb.pack()
        
        # Hemoglobin Level
        tk.Label(test_frame, text="Hemoglobin Level (g/dL):", bg='white').pack()
        tk.Entry(test_frame, textvariable=fields['hemoglobin'], width=30).pack()
        
        # Malaria Status
        tk.Label(test_frame, text="Malaria Status:", bg='white').pack()
        malaria_cb = ttk.Combobox(test_frame, textvariable=fields['malaria'],
                                 values=['Negative', 'Positive'], state='readonly')
        malaria_cb.pack()
        
        # Donation Status
        tk.Label(form_frame, text="Donation Status:", bg='white').pack()
        donation_cb = ttk.Combobox(form_frame, textvariable=fields['donation_status'],
                                  values=['Eligible', 'Not Eligible'], state='readonly')
        donation_cb.pack()
        
        # Additional Notes
        tk.Label(form_frame, text="Additional Notes:", bg='white').pack()
        tk.Entry(form_frame, textvariable=fields['additional_notes'], width=30).pack()
        
        # Submit button
        tk.Button(form_frame, text="Send Results", bg=self.primary_red, fg='white',
                 command=lambda: self.send_medical_results(fields)).pack(pady=20)

    def send_medical_results(self, fields):
        # Validate required fields
        required_fields = ['blood_type', 'hiv_status', 'syphilis_status', 
                          'hepatitis_b', 'hepatitis_c', 'donation_status']
        
        for field in required_fields:
            if not fields[field].get():
                messagebox.showerror("Error", f"{field.replace('_', ' ').title()} is required")
                return
        
        # Check eligibility criteria
        if (fields['hiv_status'].get() == 'Positive' or
            fields['syphilis_status'].get() == 'Positive' or
            fields['hepatitis_b'].get() == 'Positive' or
            fields['hepatitis_c'].get() == 'Positive' or
            fields['malaria'].get() == 'Positive'):
            fields['donation_status'].set('Not Eligible')
        
        try:
            hemoglobin = float(fields['hemoglobin'].get())
            if hemoglobin < 12.5:  # Minimum hemoglobin requirement
                fields['donation_status'].set('Not Eligible')
        except ValueError:
            pass
        
        # In a real application, this would save to a database
        messagebox.showinfo("Success", "Medical results sent successfully!")
        self.show_registered_donors()

    def show_donor_dashboard(self, username):
        # Clear current window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Create main container
        container = tk.Frame(self.root)
        container.pack(fill='both', expand=True)
        
        # Create left navigation bar
        nav_bar = tk.Frame(container, bg=self.primary_red, width=200)
        nav_bar.pack(side='left', fill='y')
        nav_bar.pack_propagate(False)
        
        # Navigation buttons
        nav_buttons = [
            ("Medical History", self.show_donor_medical_history),
            ("New Donation Request", lambda: self.show_medical_form()),
            ("Logout", self.handle_logout)
        ]
        
        for text, command in nav_buttons:
            btn = tk.Button(nav_bar, text=text, bg=self.primary_red, fg='white',
                           bd=0, pady=15, command=command)
            btn.pack(fill='x', padx=5, pady=2)
        
        # Create main content area
        self.content_frame = tk.Frame(container, bg='white')
        self.content_frame.pack(side='right', fill='both', expand=True)
        
        # Welcome message
        welcome_frame = tk.Frame(self.content_frame, bg='white')
        welcome_frame.pack(pady=20)
        
        tk.Label(welcome_frame, text=f"Welcome, {username}!",
                 font=('Arial', 24, 'bold'),
                 fg=self.primary_red, bg='white').pack()
        
        # Show medical history by default
        self.show_donor_medical_history()

    def show_donor_medical_history(self):
        # Clear content frame except welcome message
        for widget in self.content_frame.winfo_children()[1:]:
            widget.destroy()
        
        # Create scrollable frame for medical history
        canvas = tk.Canvas(self.content_frame, bg='white')
        scrollbar = ttk.Scrollbar(self.content_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='white')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        
        # Sample medical history (replace with database data)
        history_frame = tk.LabelFrame(scrollable_frame, text="Medical History", bg='white')
        history_frame.pack(padx=20, pady=20, fill='both', expand=True)
        
        # Display medical results
        results = {
            'Blood Type': 'A+',
            'Health Status': 'Good',
            'Blood Pressure': '120/80',
            'Sugar Level': 'Normal',
            'HIV Status': 'Negative',
            'Syphilis Status': 'Negative',
            'Hepatitis B': 'Negative',
            'Hepatitis C': 'Negative',
            'Hemoglobin': '13.5 g/dL',
            'Malaria': 'Negative',
            'Donation Status': 'Eligible',
            'Last Donation Date': '2024-01-15',
            'Additional Notes': 'Regular donor'
        }
        
        for key, value in results.items():
            result_frame = tk.Frame(history_frame, bg='white')
            result_frame.pack(fill='x', padx=10, pady=5)
            
            tk.Label(result_frame, text=f"{key}:", bg='white',
                    font=('Arial', 10, 'bold')).pack(side='left')
            tk.Label(result_frame, text=value, bg='white').pack(side='left', padx=10)

    def save_medical_info(self, fields):
        # Save medical information
        # In a real application, this would save to a database
        print("Medical information saved")
        
        # Show donor dashboard
        self.show_donor_dashboard(fields['username'].get())
        
    def handle_logout(self):
        if messagebox.askyesno("Logout", "Are you sure you want to logout?"):
            self.root.quit()  # This will close the application
        
    def run(self):
        self.root.mainloop()

    def create_gradient_background(self):
        canvas = tk.Canvas(self.root, width=1000, height=700)
        canvas.pack(fill='both', expand=True)
        canvas.create_rectangle(0, 0, 1000, 700, fill=self.primary_red, outline='')

if __name__ == "__main__":
    app = BloodDonationSystem()
    app.run() 