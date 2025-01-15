def withdraw_money(available_balance, withdraw_amount):
    if withdraw_amount <= available_balance:
        remaining_balance = available_balance - withdraw_amount
        print(f"Withdrawal successful. Remaining balance: {remaining_balance}")
        return remaining_balance  # Update the available balance
    else:
        print("You cannot withdraw because the amount is greater than the available balance.")
        return available_balance  # No change to available balance

# Set the initial available balance
available_balance = float(input("Enter the available balance: "))

# Get the withdrawal amount from the user
withdraw_amount = float(input("Enter the withdrawal amount: "))

# Perform the withdrawal
available_balance = withdraw_money(available_balance, withdraw_amount)

# Optionally, you can display the updated balance
print(f"Updated available balance: {available_balance}")
