import tkinter as tk
from tkinter import ttk
from .login_system import LoginSystem
from . import GUI_THEME

class BloodBankApp:
    def __init__(self):
        self.root = tk.Tk()
        self.setup_main_window()
        self.start_application()

    def setup_main_window(self):
        # Configure main window
        self.root.title("Blood Bank Management System")
        self.root.geometry("800x600")
        
        # Apply theme
        style = ttk.Style()
        style.configure("TButton",
                       background=GUI_THEME['BUTTON_COLOR'],
                       foreground=GUI_THEME['BUTTON_TEXT_COLOR'],
                       font=(GUI_THEME['FONT_FAMILY'], GUI_THEME['NORMAL_SIZE']))
        
        style.configure("TLabel",
                       font=(GUI_THEME['FONT_FAMILY'], GUI_THEME['NORMAL_SIZE']))
        
        # Create main header
        header = tk.Label(self.root,
                         text="Welcome to Blood Bank Management System",
                         font=(GUI_THEME['FONT_FAMILY'], GUI_THEME['HEADING_SIZE'], 'bold'),
                         fg=GUI_THEME['PRIMARY_COLOR'])
        header.pack(pady=20)

    def start_application(self):
        LoginSystem(self.root)
        self.root.mainloop()

def main():
    app = BloodBankApp()

if __name__ == "__main__":
    main()