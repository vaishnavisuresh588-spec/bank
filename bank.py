initial_balance = float(input("Enter initial balance: "))
transaction_type = input("Enter transaction type (deposit/withdraw): ").lower()
amount = float(input("Enter amount: "))

if transaction_type == "deposit":
    updated_balance = initial_balance + amount
elif transaction_type == "withdraw":
    if amount > initial_balance:
        print("Insufficient balance!")
        updated_balance = initial_balance
    else:
        updated_balance = initial_balance - amount
else:
    print("Invalid transaction type!")
    updated_balance = initial_balance

print("Updated balance is:", updated_balance)