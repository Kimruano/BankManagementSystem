from account import Account
from personal_information import PersonalInformation
from account_type import AccountType
import uuid


class CheckingsAccount(Account):

    def __init__(self, personal_info: PersonalInformation):
        super().__init__(personal_info)
        self.balance = 0
        self._UUID = str(uuid.uuid1())
        self.monthly_interest = 0.0025
        self.yearly_interest = 0.03
        self.type = AccountType.CHECKINGS

    def deposit(self, amount: float) -> float:
        self.balance = self.balance + amount
        print(f"A deposit of ${amount} has been made.")
        print(f"New balance is ${self.balance}.")
        return self.balance

    def withdrawal(self, amount: float) -> float:
        if amount <= self.balance:
            print(f"A withdrawal of ${str(amount)} has been made.")
            self.balance = self.balance - amount
            print(f"New balance is ${self.balance}.")
        else:
            print("Withdrawal cannot be approved at this time due to insufficient funds.")
        return self.balance

    def get_account_id(self) -> str:
        return self._UUID

    def calculate_monthly_interest(self) -> float:
        print("TOTAL MONTHLY INTEREST:")
        total_monthly_interest = self.monthly_interest * self.balance
        return total_monthly_interest

    def calculate_yearly_interest(self) -> float:
        print("TOTAL YEARLY INTEREST:")
        total_yearly_interest = self.yearly_interest * self.balance
        return total_yearly_interest

    def make_credit_card_payment(self, amount) -> bool:
        if self.balance >= amount:
            self.balance = self.balance - amount
            print(
                f"{str(amount)} has been withdrawn. Payment was processed successfully.")
            credit_card_payment_successful = True
        else:
            print("Payment cannot be processed.")
            credit_card_payment_successful = False
        return credit_card_payment_successful
