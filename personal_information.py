
class PersonalInformation:
    def __init__(self, first_name, last_name, ssn, phone_number, email, street_address, city, state, zipcode):
        self.first_name = first_name
        self.last_name = last_name
        self._ssn = ssn
        self.phone_number = phone_number
        self.email = email
        self.street_address = street_address
        self.city = city
        self.state = state
        self.zipcode = zipcode
