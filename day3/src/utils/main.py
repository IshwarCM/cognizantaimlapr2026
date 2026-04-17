import os 
import sys 

# Add project root to Python path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(PROJECT_ROOT)

from src.models.persons import Person
from src.models.role import Role
from src.models.staff import Staff
from src.models.persons import Person
from configuration.logger_configuration import configure_logger
logger = configure_logger()

def create_person():
    person = Person(adharCardNo="1234-5678-9012", MobileNo="9876543210")
    return person


def create_staff():
    role = Role(name="Doctor", description="Responsible for diagnosing and treating patients.")
    staff_member = Staff(adharCardNo="1234-5678-9012", MobileNo="9876543210", role=role)
    return staff_member

if __name__ == "__main__":
    person = create_person()
    print(person)
    try:
        inp = input("Enter new mobile number: ")
        person.MobileNo = inp
        print("Updated person:", person)
    except Exception as e:
        logger.error(f"{e}")