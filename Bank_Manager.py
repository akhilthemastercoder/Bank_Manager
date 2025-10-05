class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money!")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")

    def show_balance(self):
        print(f"{self.owner}'s balance: {self.balance}")

# Get user input
owner_name = input("Enter your name: ")
starting_balance = float(input("Enter starting balance: "))

# Create object
user_account = BankAccount(owner_name, starting_balance)

# Menu loop
while True:
    print("\nWhat do you want to do?")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Quit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        user_account.deposit(amount)
    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        user_account.withdraw(amount)
    elif choice == "3":
        user_account.show_balance()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
