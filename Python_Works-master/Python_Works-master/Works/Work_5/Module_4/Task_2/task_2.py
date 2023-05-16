import deal


@deal.inv(lambda account: account.balance >= 0)
class BankAccount:
    def __init__(self):
        self.balance = 0
        self.account_number = 11

    @deal.pre(lambda self, amount: amount > 0)
    def deposit(self, amount):
        self.balance += amount
        return f"{amount} средств успешно зачислены на счет {self.account_number}"

    @deal.pre(lambda self, amount: amount > 0)
    def withdraw(self, amount):
        if self.balance < amount:
            raise ValueError("Недостаточно средств на счете")
        self.balance -= amount
        return f"{amount} средств успешно сняты с счета {self.account_number}"

    def check_balance(self):
        return f"Баланс счета {self.account_number}: {self.balance}"


# Пример 1
account1 = BankAccount()

deposit_amount = 500
account1.deposit(deposit_amount)

print(account1.check_balance())

# Пример 2
print()
account2 = BankAccount()
account2.deposit(1000)

withdraw_amount = 250
account2.withdraw(250)

print(account2.check_balance())

# Пример 3
print()
accounts = [
    BankAccount(),
    BankAccount(),
    BankAccount(),
]

accounts[0].deposit(50)
accounts[1].deposit(200)
accounts[2].deposit(1000)
accounts[2].withdraw(10000)

for account in accounts:
    print(account.check_balance())
