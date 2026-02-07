class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient Funds"
        else:
            self.balance -= amount
            return self.balance
initial_balance, withdraw_amount = map(int, input().split())
acc = Account("User", initial_balance)
print(acc.withdraw(withdraw_amount))
