import json

with open('bank_details') as f:
    data = json.load(f)

    for state in data['bank_details']:
        pin = int(input('provide a correct pin'))
        name = input('please enter your name')
        deposite_amount = int(input('enter the amount you want to deposite'))
        withdraw_amount = int(input('enter the amount you want to withdraw'))


class Bank:
    def __init__(self):
        self.pin = pin
        self.name = name
        self.balance = 0

    def deposite(self, name, amount, bank_details):
        self.name = name
        if self.name == bank_details['name']:
            if self.pin == bank_details['pin']:
                self.balance = self.balance + amount

    def withdraw(self, money_takeout, pin, bank_details):

        if self.name == bank_details['name']:
            if self.pin == bank_details['pin']:
                if money_takeout < self.balance:

                    self.balance = self.balance - money_takeout
                    print(f'you have taken out{money_takeout}')
                else:
                    print('you have not enough money')

    def total_balance(self):
        return self.balance


user = Bank()
user.deposite(deposite_amount)
print(f'your total balance is:::: {user.total_balance()}')
user.withdraw(withdraw_amount, pin)
print(f'after withdrawing your money left::::{user.total_balance()}')



