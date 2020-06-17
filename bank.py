name = input('enter your name')
pin = int(input('provide a correct pin'))
if pin == 1234:
    deposite_amount = int(input('enter the amount you want to deposite'))
    withdraw_amount = int(input('enter the amount you want to withdraw'))


    class Bank:
        def __init__(self):
            self.balance = 0

        def deposite(self, name, amount):
            self.name = name

            self.balance = self.balance + amount

        def withdraw(self, money_takeout):

            if money_takeout < self.balance:
                self.balance = self.balance - money_takeout
                print(f'you have taken out{money_takeout}')
            else:
                print('you have not enough money')

        def total_balance(self):
            return self.balance


    user = Bank()
    user.deposite(name, deposite_amount)
    print(f'your total balance is:::: {user.total_balance()}')
    user.withdraw(withdraw_amount)
    print(f'after withdrawing your money left::::{user.total_balance()}')


else:
    print(f'you enter the incorrect pin')





