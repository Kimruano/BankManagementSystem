from personal_information import PersonalInformation
from account_type import AccountType


class Account:
    def __init__(self, personal_info: PersonalInformation):
        self.personal_info = personal_info

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
