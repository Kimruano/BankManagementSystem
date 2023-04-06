from account import Account
from personal_information import PersonalInformation
from account_type import AccountType
from checkings_account import CheckingsAccount


class CreditCardAccount(Account):

    def __init__(self, personal_info: PersonalInformation):
        super().__init__(personal_info)
        self.current_balance = 0.00
        self.interest_rate = .03
        self.available_credit = 10000.00
        self.type = AccountType.CREDITCARD

    def make_a_purchase(self, purchase_amount: float) -> float:
        if self.current_balance < self.available_credit:
            self.current_balance = self.current_balance + purchase_amount
            self.available_credit = self.available_credit - purchase_amount
            print(
                f"Purchase amount of ${str(purchase_amount)} has been approved.")
        else:
            print("Purchase cannot be completed at this time.")
        return self.current_balance

    def make_a_payment(self, payment_amount: float, bank_account: CheckingsAccount) -> float:
        if bank_account.make_credit_card_payment(payment_amount) == True:
            self.current_balance = self.current_balance - payment_amount
            self.available_credit = self.available_credit + payment_amount
            print(f"A payment has been made for ${str(payment_amount)}.")
        return self.current_balance

    def check_available_credit(self) -> float:
        return self.available_credit
