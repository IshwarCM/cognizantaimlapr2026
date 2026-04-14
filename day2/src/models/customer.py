from datetime import date


class Customer:
    def __init__(self, name: str, email: str, dob: date):
        self.name = name
        self.email = email
        self.dob = dob

    def __str__(self) -> str:
        return f"Customer(name='{self.name}', email='{self.email}', dob={self.dob})"
