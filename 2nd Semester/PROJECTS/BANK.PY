from bankcalc import *
accounts = []
while True:
    print("="*40)
    print(f"\tWELCOME TO TOKAC BANK")
    print("="*40)
    a = f'''
    Select the option for the account you want to open
    (1) Savings Account
    (2) Current Account
    '''
    print(a)
    b = int(input("Enter your choice: "))
    if b == 1:
        accounts.append(SavingAccount())
    break
