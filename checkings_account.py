from account import Account
from personal_information import PersonalInformation
from account_type import AccountType
import uuid


class CheckingsAccount(Account):

    def __init__(self, personal_info: PersonalInformation):
        super().__init__(personal_info)  # Calls the parent constructor
        self.balance = 0
        self._UUID = uuid.uuid1()
        self.interest = .035
        self.type = AccountType.CHECKINGS

    def deposit(self, amount: int):
        self.balance = self.balance + amount
        print("A deposit has been made of $" + str(amount))
        print("New balance is $" + str(self.balance))

    def withdrawl(self, amount: int):
        if amount < self.balance:
            print("A withdrawl has been made of $" + str(amount))
            self.balance = self.balance - amount
            print("New balance is $" + str(self.balance))
        else:
            print("Withdrawl cannot be approved at this time due to insufficient funds")

    def get_account_id(self):
        return self._UUID
