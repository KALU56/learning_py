# Create the initial bank account file
with open("bank_accounts.txt", "w") as file:
    file.write("1,John Doe,5000\n")
    file.write("2,Jane Smith,3000\n")
    file.write("3,Sam Brown,2000\n")

# Function to add a new customer
def add_customer(account_id, customer_name, balance):
    with open("bank_accounts.txt", "a") as file:
        file.write(f"{account_id},{customer_name},{balance}\n")
    print(f"Customer '{customer_name}' added successfully.")

# Function to view all customers
def view_customers():
    print("Customer Accounts:")
    with open("bank_accounts.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            account_id, customer_name, balance = line.strip().split(",")
            print(f"Account ID: {account_id}, Name: {customer_name}, Balance: {balance}")

# Function to deposit money
def deposit(account_id, amount):
    updated_accounts = []
    account_found = False
    with open("bank_accounts.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            acc_id, customer_name, balance = line.strip().split(",")
            if int(acc_id) == account_id:
                account_found = True
                balance = int(balance) + amount
                print(f"Deposited {amount} to '{customer_name}' account.")
            updated_accounts.append(f"{acc_id},{customer_name},{balance}\n")
    
    if not account_found:
        print(f"Account with ID {account_id} not found.")
    
    with open("bank_accounts.txt", "w") as file:
        file.writelines(updated_accounts)

# Function to withdraw money
def withdraw(account_id, amount):
    updated_accounts = []
    account_found = False
    with open("bank_accounts.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            acc_id, customer_name, balance = line.strip().split(",")
            if int(acc_id) == account_id:
                account_found = True
                if int(balance) >= amount:
                    balance = int(balance) - amount
                    print(f"Withdrew {amount} from '{customer_name}' account.")
                else:
                    print(f"Insufficient funds in '{customer_name}' account.")
            updated_accounts.append(f"{acc_id},{customer_name},{balance}\n")
    
    if not account_found:
        print(f"Account with ID {account_id} not found.")
    
    with open("bank_accounts.txt", "w") as file:
        file.writelines(updated_accounts)

# Function to transfer money between two accounts
def transfer(from_account_id, to_account_id, amount):
    updated_accounts = []
    from_account_found = False
    to_account_found = False
    with open("bank_accounts.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            acc_id, customer_name, balance = line.strip().split(",")
            if int(acc_id) == from_account_id:
                from_account_found = True
                if int(balance) >= amount:
                    balance = int(balance) - amount
                    print(f"Transferred {amount} from '{customer_name}' account.")
                else:
                    print(f"Insufficient funds in '{customer_name}' account for transfer.")
            if int(acc_id) == to_account_id:
                to_account_found = True
                balance = int(balance) + amount
                print(f"Transferred {amount} to '{customer_name}' account.")
            updated_accounts.append(f"{acc_id},{customer_name},{balance}\n")
    
    if not from_account_found:
        print(f"Sender account with ID {from_account_id} not found.")
    if not to_account_found:
        print(f"Receiver account with ID {to_account_id} not found.")
    
    with open("bank_accounts.txt", "w") as file:
        file.writelines(updated_accounts)

# Example Workflow
view_customers()
deposit(1, 500)
view_customers()
withdraw(2, 1500)
view_customers()
transfer(1, 2, 2000)
view_customers()
add_customer(4, "Alice Green", 1000)
view_customers()
