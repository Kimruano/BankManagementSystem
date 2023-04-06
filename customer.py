from personal_information import PersonalInformation
from account_type import AccountType
from checkings_account import CheckingsAccount
from savings_account import SavingsAccount
from credit_card_account import CreditCardAccount


class Customer:

    def __init__(self, personal_info: PersonalInformation):
        self.personal_info = personal_info
        self.accounts = []

    def show_personal_information(self) -> None:
        print(f"""
ACCOUNT INFORMATION:
First Name: {self.personal_info.first_name}
Last Name: {self.personal_info.last_name}
Street Address: {self.personal_info.street_address}
City: {self.personal_info.city}
State: {self.personal_info.state}
Zipcode: {self.personal_info.zipcode}
            """)

    def edit_personal_information(self, edited_info: dict) -> str:
        print("UPDATED INFORMATION:")
        if "first_name" in edited_info:
            self.personal_info.first_name = edited_info["first_name"]
        if "last_name" in edited_info:
            self.personal_info.last_name = edited_info["last_name"]
        if "street_address" in edited_info:
            self.personal_info.street_address = edited_info["street_address"]
        if "city" in edited_info:
            self.personal_info.city = edited_info["city"]
        if "state" in edited_info:
            self.personal_info.state = edited_info["state"]
        if "zipcode" in edited_info:
            self.personal_info.zipcode = edited_info["zipcode"]

    def open_account(self, account_type: AccountType) -> bool:
        if account_type == AccountType.CHECKINGS:
            new_account = CheckingsAccount(self.personal_info)
            self.accounts.append(new_account)
            return True
        elif account_type == AccountType.SAVINGS:
            new_account = SavingsAccount(self.personal_info)
            self.accounts.append(new_account)
            return True
        elif account_type == AccountType.CREDITCARD:
            new_account = CreditCardAccount(self.personal_info)
            self.accounts.append(new_account)
            return True
        else:
            return False

    def close_account(self, account_uuid: str) -> bool:
        for account in self.accounts:
            if account_uuid == account.get_account_id():
                self.accounts.remove(account)
                print("Account has been closed.")
                return True
            else:
                print("An account with that ID does not exist.")
                return False

    def select_account(self, type: AccountType) -> None:
        for account in self.accounts:
            if type == account.type:
                return account
        print(f"Account type {type} not found")

    def list_accounts(self) -> None:
        print("LIST OF ACCOUNTS:")
        for account in self.accounts:
            print(account.type.name)
