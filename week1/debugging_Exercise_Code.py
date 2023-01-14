class BankAccount:
    """
    Represents a bank account that the user can deposit money to and  withdraw money from.
    """

    def __init__(self, account_ID, balance):
        """Creates a bank account object with an account ID and balance."""
        self._account_ID = account_ID
        self._balance = balance

    def get_account_ID(self):
        """Returns the account ID."""
        return self._account_ID

    def set_account_ID(self, new_ID):
        """Sets the account ID to a new value."""
        self._account_ID = new_ID

    def get_balance(self):
        """Returns the current balance."""
        return self._balance

    def deposit(self, amount):
        """Deposits the specified amount into the account."""
        print("In deposit, balance is", self._balance)
        print("Another deposit", amount)
        self._balance += amount

    def withdraw(self, amount):
        """Withdraws the specified amount from the account."""
        print("In withdraw(), balance is", self._balance)
        print("Withdrawing the amount ", str(amount))
        self._balance -= amount


# Create 3 bank accounts
 b1 = BankAccount(42, 500)
b2 = BankAccount(45, 900)
b3 = BankAccount(91, 1000)

# collect them in a list
bank_accounts = [b1, b2, b3]

# give interest to everyone who has more than minimum balance
for b in bank_accounts:
    print("Inside for loop, value for b is",b)
    balance = b.get_balance()
    if balance > 500:
        b.deposit(balance * 0.010)
        print("A/c no: " + str(b.get_account_ID()) ,": You have earned interest on your savings!")
    else:
        print("A/c no: " + str(b.get_account_ID()) , ": Sorry you need to meet minimum balance to earn interest")

for b in bank_accounts:
    #objectName.methodName(parameters)
    b.withdraw(1)
    print("A/c no." + str(b.get_account_ID()), "has balance of $" + str(b.get_balance()))
