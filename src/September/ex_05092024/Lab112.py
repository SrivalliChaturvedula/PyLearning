class Bank:
    def __init__(self, account_number, balance):
        self.balance = balance
        self.__account_number = account_number

    def deposit(self, amount):
        self.balance = self.balance + amount

    def checkBalance(self):
        print(self.balance)

    def show_me_account_number(self, is_auth):
        if is_auth == True:
            print(self.__account_number)
        else:
            print("Not authorized")


icici = Bank(12345, 234)
icici.deposit(100)
icici.checkBalance()
icici.show_me_account_number(False)


