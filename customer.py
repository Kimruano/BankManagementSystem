from personal_information import PersonalInformation
from account_type import AccountType
from checkings_account import CheckingsAccount
# from savings_account import SavingsAccount


class Customer:

    def __init__(self, personal_info: PersonalInformation):  # constructor
        self.personal_info = personal_info
        self.accounts = []

    def show_personal_information(self):
        print("CUSTOMER INFORMATION")
        print(self.personal_info.first_name)
        print(self.personal_info.last_name)
        print(self.personal_info._ssn)
        print(self.personal_info.street_address)
        print(self.personal_info.city)
        print(self.personal_info.state)
        print(self.personal_info.zipcode)

    def edit_personal_information(self, edited_info: dict):
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

    def open_account(self, account_type: AccountType):
        if account_type == AccountType.CHECKINGS:
            new_account = CheckingsAccount(self.personal_info)
            self.accounts.append(new_account)
        # else:
        #     new_account = SavingsAccount(self.personal_info)
        #     self.accounts.append(new_account)

    def close_account(self, account_id: str):
        for account in self.accounts:
            if account_id == account.get_account_id():
                accounts.remove()

        pass

    def select_account(self, type: AccountType):
        for account in self.accounts:
            if type == account.type:
                return account

        print(f"Account type {type} not found")

    def list_accounts(self):
        for account in self.accounts:
            print(account.type.name)
