class Account:
    def __init__(self, acc_no, pin, balance=0):
        self.acc_no = acc_no
        self.pin = pin
        self.balance = balance


class ATM:
    def __init__(self):
        self.accounts = {}

    def add_account(self, acc):
        self.accounts[acc.acc_no] = acc

    def login(self, acc_no, pin):
        if acc_no in self.accounts and self.accounts[acc_no].pin == pin:
            return True
        return False

    def withdraw(self, acc_no, amount):
        acc = self.accounts[acc_no]
        if acc.balance >= amount:
            acc.balance -= amount
            return True
        return False

    def deposit(self, acc_no, amount):
        self.accounts[acc_no].balance += amount
