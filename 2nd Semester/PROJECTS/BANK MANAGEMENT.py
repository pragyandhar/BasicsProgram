class bank:
    def __init__(self, balance=0):
        self.balance = balance
        print("Welcome to the Deposit & Withdrawal Machine")

    def details(self, name, accno):
        self.name = name
        self.accno = accno
        return f'''
        NAME: {self.name}
        ACCOUNT NUMBER: {self.accno}
        ACCOUNT BALANCE: {self.balance}
        '''

    def deposit(self):
        amt = float(input("Enter the amount that you need to deposit: "))
        self.balance += amt
        print(f"Rs.{self.balance} is deposited")

    def withdraw(self):
        wd = float(input("Enter the amount which you need to withdraw: "))
        if wd > self.balance:
            print("NOT SUFFICIENT AMOUNT")
        else:
            print(f"Amount withdrawn Rs.{wd}")
            self.balance -= wd

    def checkbalance(self):
        print(f"The amount in your account is Rs.{self.balance}")


# main code
name = input("Enter the name: ")
accno = int(input("Enter the account number: "))
accof = bank()
accof.details(name, accno)
while True:
    ask = '''
    What do you want to do:
    (1) Deposit Money
    (2) Withdraw Money
    (3) Check Balance in your Account
    (4) Exit
    '''
    print(ask)
    a1 = int(input("Enter the choice(1-4): "))
    if a1 == 1:
        accof.deposit()
    elif a1 == 2:
        accof.withdraw()
    elif a1 == 3:
        accof.checkbalance()
    elif a1 == 4:
        print("THANKYOU FOR USING OUR SERVICE")
        break
