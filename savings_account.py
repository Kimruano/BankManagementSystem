from account import Account
from personal_information import PersonalInformation
from account_type import AccountType
import uuid
import time


class SavingsAccount(Account):

    def __init__(self, personal_info: PersonalInformation):
        super().__init__(personal_info)
        self.balance = 0
        self._UUID = str(uuid.uuid1())
        self.monthly_interest = 0.00291666666
        self.yearly_interest = 0.035
        self.type = AccountType.SAVINGS
        self.number_of_withdrawals = 0
        self.first_withdrawal_occured = None

    def deposit(self, amount: float) -> float:
        self.balance = self.balance + amount
        print(f"A deposit of ${amount} has been made.")
        print(f"New balance is ${self.balance}.")
        return self.balance

    def withdrawl(self, amount: float) -> float:
        if self.number_of_withdrawals == 0:
            self.balance = self.balance - amount
            self.first_withdrawal_occured = time.time()
            self.number_of_withdrawals = 1
            print(f"A withdrawal of ${str(amount)} has been made.")
            print(f"New balance is ${self.balance}.")
        elif self.number_of_withdrawals < 3:
            withdrawal_request = time.time()
            if withdrawal_request - self.first_withdrawal_occured > 5:
                self.balance = self.balance - amount
                self.first_withdrawal_occured = withdrawal_request
                self.number_of_withdrawals = 1
                print(f"A withdrawal of ${str(amount)} has been made.")
                print(f"New balance is ${self.balance}.")
            else:
                self.balance = self.balance - amount
                first_withdrawal_occured = time.time()
                self.number_of_withdrawals = self.number_of_withdrawals + 1
                print(f"A withdrawal of ${str(amount)} has been made.")
                print(f"New balance is ${self.balance}.")
        else:
            print("Number of withdrawals allowed has been exceeded.")

        return self.balance

    def get_account_id(self) -> str:
        return self._UUID

    def calculate_monthly_interest(self) -> float:
        print("TOTAL MONTHLY INTEREST")
        total_monthly_interest = self.monthly_interest * self.balance
        return total_monthly_interest

    def calculate_yearly_interest(self) -> float:
        print("TOTAL YEARLY INTEREST")
        total_yearly_interest = self.yearly_interest * self.balance
        return total_yearly_interest
