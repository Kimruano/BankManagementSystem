from personal_information import PersonalInformation
from account_type import AccountType


class Account:
    def __init__(self, personal_info: PersonalInformation):
        self.personal_info = personal_info

    def show_personal_information(self):
        print("ACCOUNT INFORMATION:")
        print(self.personal_info.first_name)
        print(self.personal_info.last_name)
        print(self.personal_info._ssn)
        print(self.personal_info.street_address)
        print(self.personal_info.city)
        print(self.personal_info.state)
        print(self.personal_info.zipcode)
