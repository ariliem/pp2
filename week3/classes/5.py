class Bank:
    
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, summa):
        self.balance = self.balance + summa

    def withdraw(self,summa):
        if summa < self.balance:
            self.balance = self.balance - summa
        else:
            print("У вас недостаточно денег на счету!")
        
    def check(self):
        print(self.owner, self.balance)

name = input()

money = int(input())
Bereke = Bank(name,money)

x = int(input())
Bereke.deposit(x)

Bereke.check()

y = int(input())
Bereke.withdraw(y)

Bereke.check()
