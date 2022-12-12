
class Account(object):
    def __init__(self, firstname: str, lastname: str, phonenumber: int , email:str, password: str, cpassword: str):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__phonenumber = phonenumber
        self.__email = email
        self.__password = password
        self.__cpassword = cpassword

    @property
    def firstname(self):
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname):
        self.__firstname = firstname

    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname):
        self.__lastname = lastname

    @property
    def phonenumber(self):
        return self.__phonenumber

    @phonenumber.setter
    def phonenumber(self, phonenumber):
        self.__phonenumber = phonenumber

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def cpassword(self):
        return self.__cpassword

    @cpassword.setter
    def cpassword(self, cpassword):
        self.__cpassword = cpassword

    @property
    def password_match(self) -> bool:
        return self.__password == self.__cpassword

    """ @password_match.setter
    def password_match(self, password: str, cpassword: str):
        if password == cpassword:
            self.__password = password
            self.__cpassword = cpassword
        else:
            raise ValueError("Passwords do not match") """