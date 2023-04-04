from customer import Customer
from personal_information import PersonalInformation
from account_type import AccountType

kim_personal = PersonalInformation("kimberly", "ruano", "123456", "1234141351",
                                   "nagmafop@gmail.com", "2935 Topaz Lane", "Farmers Branch", "Texas", "75234")
kim = Customer(kim_personal)

# kim.show_personal_information()

# new_info = {"first_name": "Kim"}
# updated_last_name_and_city = {"last_name": "Oreos", "city": "Cypress"}

# kim.editPersonalInformation(new_info)
# kim.editPersonalInformation(updated_last_name_and_city)
# kim.show_personal_information()
kim.open_account(AccountType.CHECKINGS)
# print(kim.accounts[0])
# kim.accounts[0].show_personal_information()

# Testing deposit and withdrawl functions
# kim.accounts[0].deposit(10000)
# kim.accounts[0].withdrawl(2000)
# kim.accounts[0].withdrawl(9000)

# Testing UUID
# print(kim.accounts[0].UUID)
# kim.selectAccount("adadad")

kim_checking_account = kim.select_account(AccountType.CHECKINGS)
# kim_checking_account.deposit(10000)
# print(kim_checking_account.balance)

kim.list_accounts()

# kim_checking_account.UUID
