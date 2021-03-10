class account:
    def __init__(self,accno,name,acctype,balance):
        self.accno=accno
        self.name=name
        self.acctype=acctype
        self.balance=balance
    def deposit(self,balance,amount):
        print("RS.%d credited to your account"%amount)
        print("Final balance is",balance+amount)
    def withdraw(self,balance,amount):
        print("RS. %d debited from your account"%amount)
        print("Final balance is",balance-amount)
    def display(self):
        print("Your Account Number:",self.accno)
        print("Your Name:",self.name)
        print("Your Account Type:",self.acctype)
        print("Your Account Balance:",self.balance)
    def __del__(self):
        print("Object Deleted")
account1=account(1234,"Teena","savings",10000)
account2=account(4567,"Anna","Current",20000)
account1.display()
account1.deposit(10000,20000)
account1.withdraw(20000,4000)
account2.display()
account2.deposit(10000,20000)
account2.withdraw(20000,6000)
del account1
del account2
