class BankAccount:
    def __init__(self, card_holder, card_number, amount_of_money):
        self.card_holder = card_holder
        self.card_number = card_number
        self.amount_of_money = amount_of_money

    def withdrawal(self, other):
        self.amount_of_money -= other

    def deposit(self, other):
        self.amount_of_money += other

    def __str__(self):
        return f"{self.card_holder} with number of card {self.card_number} has {self.amount_of_money}"


bank_account = BankAccount("Vasyl", "4441", 500)
print(bank_account)
bank_account.withdrawal(150)
print(bank_account)
bank_account.deposit(200)
print(bank_account)
