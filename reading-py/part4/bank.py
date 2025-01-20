# Function to create a new account
def create_account():
    print("\nCreate a New Account")
    name = input("Enter your full name: ")
    account_number = input("Enter a unique account number: ")
    
    # Check if account already exists
    try:
        with open("accounts.txt", mode="r") as file:
            accounts = file.readlines()
            for account in accounts:
                details = account.strip().split(", ")
                if details[1] == account_number:
                    print("Account with this number already exists!")
                    return
    except FileNotFoundError:
        pass  # If the file doesn't exist, it's fine to create a new one.

    balance = float(input("Enter initial deposit amount: "))
    if balance < 0:
        print("Initial deposit cannot be negative.")
        return
    
    # Save the account details to the file
    with open("accounts.txt", mode="a") as file:
        file.write(f"{name}, {account_number}, {balance}\n")
    
    print(f"Account created successfully for {name} with Account Number: {account_number}.")

# Function to view account balance
def check_balance():
    account_number = input("\nEnter your account number: ")
    
    try:
        with open("accounts.txt", mode="r") as file:
            accounts = file.readlines()
            for account in accounts:
                details = account.strip().split(", ")
                if details[1] == account_number:
                    print(f"Account Balance: {details[2]}")
                    return
            print("Account not found!")
    except FileNotFoundError:
        print("No accounts found!")

# Function to deposit money into an account
def deposit():
    account_number = input("\nEnter your account number: ")
    
    try:
        with open("accounts.txt", mode="r") as file:
            accounts = file.readlines()
            for i, account in enumerate(accounts):
                details = account.strip().split(", ")
                if details[1] == account_number:
                    deposit_amount = float(input("Enter deposit amount: "))
                    if deposit_amount > 0:
                        new_balance = float(details[2]) + deposit_amount
                        accounts[i] = f"{details[0]}, {details[1]}, {new_balance}\n"
                        with open("accounts.txt", mode="w") as file:
                            file.writelines(accounts)
                        print(f"Deposited {deposit_amount}. New balance: {new_balance}.")
                        return
                    else:
                        print("Deposit amount must be positive.")
                        return
            print("Account not found!")
    except FileNotFoundError:
        print("No accounts found!")

# Function to withdraw money from an account
def withdraw():
    account_number = input("\nEnter your account number: ")
    
    try:
        with open("accounts.txt", mode="r") as file:
            accounts = file.readlines()
            for i, account in enumerate(accounts):
                details = account.strip().split(", ")
                if details[1] == account_number:
                    withdraw_amount = float(input("Enter withdrawal amount: "))
                    if withdraw_amount > 0:
                        current_balance = float(details[2])
                        if withdraw_amount <= current_balance:
                            new_balance = current_balance - withdraw_amount
                            accounts[i] = f"{details[0]}, {details[1]}, {new_balance}\n"
                            with open("accounts.txt", mode="w") as file:
                                file.writelines(accounts)
                            print(f"Withdrew {withdraw_amount}. New balance: {new_balance}.")
                            return
                        else:
                            print("Insufficient funds!")
                            return
                    else:
                        print("Withdrawal amount must be positive.")
                        return
            print("Account not found!")
    except FileNotFoundError:
        print("No accounts found!")

# Function to transfer funds between two accounts
def transfer():
    sender_account = input("\nEnter your account number: ")
    try:
        with open("accounts.txt", mode="r") as file:
            accounts = file.readlines()
            sender_found = False
            for i, account in enumerate(accounts):
                details = account.strip().split(", ")
                if details[1] == sender_account:
                    sender_found = True
                    recipient_account = input("Enter recipient's account number: ")
                    recipient_found = False
                    for j, recipient in enumerate(accounts):
                        recipient_details = recipient.strip().split(", ")
                        if recipient_details[1] == recipient_account:
                            recipient_found = True
                            transfer_amount = float(input("Enter transfer amount: "))
                            if transfer_amount > 0:
                                sender_balance = float(details[2])
                                if transfer_amount <= sender_balance:
                                    new_sender_balance = sender_balance - transfer_amount
                                    sender_name = details[0]
                                    recipient_name = recipient_details[0]
                                    recipient_balance = float(recipient_details[2])
                                    new_recipient_balance = recipient_balance + transfer_amount

                                    # Update the balances in the accounts
                                    accounts[i] = f"{sender_name}, {details[1]}, {new_sender_balance}\n"
                                    accounts[j] = f"{recipient_name}, {recipient_details[1]}, {new_recipient_balance}\n"

                                    with open("accounts.txt", mode="w") as file:
                                        file.writelines(accounts)

                                    print(f"Transferred {transfer_amount} from {sender_account} to {recipient_account}.")
                                    print(f"New balance of {sender_account}: {new_sender_balance}.")
                                    print(f"New balance of {recipient_account}: {new_recipient_balance}.")
                                    return
                                else:
                                    print("Insufficient funds!")
                                    return
                            else:
                                print("Transfer amount must be positive.")
                                return
                    if not recipient_found:
                        print("Recipient account not found.")
                    return
            if not sender_found:
                print("Sender account not found!")
    except FileNotFoundError:
        print("No accounts found!")

# Main menu
def main_menu():
    while True:
        print("\nWelcome to the Bank System")
        print("1. Create a New Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Funds")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            create_account()
        elif choice == '2':
            check_balance()
        elif choice == '3':
            deposit()
        elif choice == '4':
            withdraw()
        elif choice == '5':
            transfer()
        elif choice == '6':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1 to 6.")

# Run the program
if __name__ == "__main__":
    main_menu()
