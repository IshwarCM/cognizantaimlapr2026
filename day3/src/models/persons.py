"""Person model definition"""

import re


class Person:
    """a class representing a person in the hospital system"""

    def __init__(self, adharCardNo: str, MobileNo: str):
        self.__adharCardNo = adharCardNo
        self.__MobileNo = MobileNo

    @property
    def MobileNo(self):
        return self.__MobileNo
    
        
    @MobileNo.setter
    def MobileNo(self, value):
        if not re.fullmatch(r'\d{10}', value):
            raise ValueError("Mobile number must be a 10-digit numeric string.")
        self.__MobileNo = value


    def __str__(self):
        return f"Person with Adhar Card No: {self.__adharCardNo} and Mobile No: {self.__MobileNo}"