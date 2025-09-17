balance = 100000  

def check_balance():
    print(f"Your current balance is: ₹{balance}")   

def deposit(amount):
    global balance
    if amount > 0:
        balance += amount
        print(f"Successfully deposited ₹{amount}")
    else:
        print("Deposit amount must be greater than 0")

def withdraw(amount):
    global balance
    if 0 < amount <= balance:
        balance -= amount
        print(f"Successfully withdrawn ₹{amount}")
    else:
        print("Insufficient balance or invalid amount.")


while True:
    print("\n--- Banking Menu ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        check_balance()
    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        deposit(amount)
    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        withdraw(amount)
    elif choice == "4":
        print("Thank you for using Bank System!")
        break
    else:
        print("Invalid choice, try again.")
