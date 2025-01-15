def withdraw_money(available_balance, withdraw_amount):
    if withdraw_amount <= available_balance:
        remaining_balance = available_balance - withdraw_amount
        print(f"Withdrawal successful. Remaining balance: {remaining_balance:.2f}")
        return remaining_balance  # Update the available balance
    else:
        print("You cannot withdraw because the amount is greater than the available balance.")
        return available_balance  # No change to available balance

# Welcome message and menu options
print("Welcome to our bank system")
print("1. Check your balance")
print("2. Withdraw money")
print("3. Exit")

# Set the initial available balance
available_balance = float(input("Enter the available balance: "))

# Main program logic
position_choice = int(input("Enter your choice: "))

if position_choice == 1:
    # Option to check balance
    print(f"Your current balance is: {available_balance:.2f}")
elif position_choice == 2:
    # Option to withdraw money
    withdraw_amount = float(input("Enter the withdrawal amount: "))
    if withdraw_amount > 0 and withdraw_amount < available_balance:
        available_balance = withdraw_money(available_balance, withdraw_amount)
        print(f"Updated available balance: {available_balance:.2f}")
    else:
        print(f"Withdrawal amount must be greater than zero and sorry your available_balance is {available_balance}.")
elif position_choice == 3:
    # Option to exit
    print("Thank you for using our bank system. Goodbye!")
else:
    # Handle invalid choice
    print("Invalid choice. Please select a valid option.")
