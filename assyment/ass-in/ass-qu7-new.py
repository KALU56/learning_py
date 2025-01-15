# Define roles and their access rights
ACCESS_RIGHTS = {
    "super_admin": ["settings", "management", "development", "maintenance"],
    "admin": ["user_management", "support"],
    "manager": ["report", "profile"],
    "staff": ["profile"]
}

# Mock user database
USERS = {
    "superadmin": {"password": "super123", "role": "super_admin"},
    "admin1": {"password": " ", "role": "admin"},
    "manager1": {"password": "manager123", "role": "manager"},
    "staff1": {"password": "staff123", "role": "staff"}
}

# Authentication function
def authenticate_user(username, password):
    user = USERS.get(username)
    if user and user["password"] == password:
        return username, user["role"]
    return None, None

# Authorization function
def authorize_user(role, action):
    allowed_actions = ACCESS_RIGHTS.get(role, [])
    if action in allowed_actions:
        print(f"Access granted to perform '{action}' as a {role}.")
    else:
        print(f"Access denied for '{action}' as a {role}.")

# Change password function
def change_password(username):
    new_password = input("Enter new password: ")
    confirm_password = input("Confirm new password: ")
    if new_password == confirm_password:
        USERS[username]["password"] = new_password
        print("Password updated successfully!")
    else:
        print("Passwords do not match. Try again.")

# Change username function
def change_username(username):
    new_username = input("Enter new username: ")
    if new_username in USERS:
        print("Username already exists. Please choose a different username.")
    else:
        USERS[new_username] = USERS.pop(username)
        print(f"Username updated successfully! Your new username is '{new_username}'.")
        return new_username

# Main application
def main():
    print("Welcome to the Company Portal")
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    # Authenticate user
    username, role = authenticate_user(username, password)
    if role:
        print(f"Authentication successful. Logged in as {role}.")
        while True:
            print("\nAvailable options:")
            print("1. Perform an action")
            print("2. Change password")
            print("3. Change username")
            print("4. Logout")
            option = input("Choose an option: ").strip()
            
            if option == "1":
                print("Available actions:")
                for i, action in enumerate(ACCESS_RIGHTS[role], start=1):
                    print(f"{i}. {action}")
                choice = input("Enter the action you want to perform: ").strip().lower()
                authorize_user(role, choice)
            elif option == "2":
                change_password(username)
            elif option == "3":
                username = change_username(username)
            elif option == "4":
                print("Logging out. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")
    else:
        print("Authentication failed. Invalid username or password.")

if __name__ == "__main__":
       main()
