"""usermodel.py"""


class UserModel:
    """Class for parsing new user data from a form."""

    def __init__(self, first_name: str, last_name: str, email: str, phone_number: str, password: str):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.password = password

    def __repr__(self):
        return (f"UserModel(first_name={self.first_name}, last_name={self.last_name}, "
                f"email={self.email}, phone_number={self.phone_number}, password={self.password})")
