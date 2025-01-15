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
    "admin1": {"password": "admin123", "role": "admin"},
    "manager1": {"password": "manager123", "role": "manager"},
    "staff1": {"password": "staff123", "role": "staff"}
}

# Authentication function
def authenticate_user(username, password):
    user = USERS.get(username)
    if user and user["password"] == password:
        return user["role"]
    return None

# Authorization function
def authorize_user(role, action):
    allowed_actions = ACCESS_RIGHTS.get(role, [])
    if action in allowed_actions:
        print(f"Access granted to perform '{action}' as a {role}.")
    else:
        print(f"Access denied for '{action}' as a {role}.")

# Main application
def main():
    print("Welcome to the Company Portal")
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    # Authenticate user
    role = authenticate_user(username, password)
    if role:
        print(f"Authentication successful. Logged in as {role}.")
        print("Available actions:")
        for i, action in enumerate(ACCESS_RIGHTS[role], start=1):
            print(f"{i}. {action}")
        
        # Prompt user to choose an action
        choice = input("Enter the action you want to perform: ").strip().lower()
        authorize_user(role, choice)
    else:
        print("Authentication failed. Invalid username or password.")

if __name__ == "__main__":
    main()
