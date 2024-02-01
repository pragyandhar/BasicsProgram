class bank:
    def __init__(self, name, accno, balance=0):
        self.balance = balance
        # print("Welcome to the Deposit & Withdrawal Machine")

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


class SavingAccount(bank):
    def __init__(self, accno, name, balance, interest_rate=0.02):
        self.interest_rate = interest_rate
        # super() refers to parent class i.e. the inherited class
        super().__init__(accno, name, balance)

    def add_interest(self):
        amt = self.balance * self.interest_rate
        self.balance += amt


class CheckingAccount(bank):
    def __init__(self, accno, name, balance, overlimit_draft=10000):
        super().__init__(accno, name, balance)
        self.overlimit_draft = overlimit_draft

    def withdraw(self, amount):
        if amount <= self.balance + self.overlimit_draft:
            self.balance -= amount
        else:
            print("Insufficient Balance")


# main code
__name__ == "__main__"
