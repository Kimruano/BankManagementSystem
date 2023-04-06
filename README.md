# BankManagementSystem

## Overview
This is an object oriented programming (OOP) bank management system project. 

The entities are: 
- Personal Information
- Customer
- Account Type
- Account
- Checkings Account
- Credit Card Account
- Savings Account

## Personal Information
The Personal Information class holds customer's information which is needed in order to create an account.
## Customer
The Customer class is made up of the following methods:
- show_personal_information
- edit_personal_information
- open_account
- close_account
- select_account
- list_account

These are common actions a customer might want to execute.
## Account Type
The Account Type class helps identify the different account types.
## Account
The Account class is the parent class. It can show the customer's personal information.
## Checkings Account
The Checking Account is a child class which inherits from the Account class. It contains the following methods:
- deposit
- withdrawal
- get_account_id
- calculate_monthly_interest
- calculate_yearly_interest
- make_credit_card_payment 
## Credit Card Account
The Credit Card Account is a child class which inherits from the Account class and the Checkings Account class. It contains the following methods:
- make_a_purchase
- make_a_payment
    - This method takes a CheckingsAccount object which allows a withdrawl to happen when a payment is made
- check_available_credit
## Savings Account
The Savings Account is a child class which inherits from the Account class. This class contains a predifned interest rate and number of withdrawals allowed within a certain time. It contains the following methods:
- deposit
- withdrawal
- get_account_id
- calculate_monthly_interest
- calculate_yearly_interest



