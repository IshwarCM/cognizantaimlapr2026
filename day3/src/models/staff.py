"""create class staff inherit from person class and associative with role attribute"""

from persons import Person
from .role import Role


class Staff(Person):
    """a class representing a staff member in the hospital system"""

    def __init__(self, adharCardNo: str, MobileNo: str, role: Role):
        super().__init__(adharCardNo, MobileNo)
        self.role = role

    def __str__(self):
        return f"Staff with Adhar Card No: {self._Person__adharCardNo}, Mobile No: {self._Person__MobileNo}, and Role: {self.role.name}"