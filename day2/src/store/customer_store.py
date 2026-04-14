from typing import List
from faker import Faker
from models.customer import Customer


class CustomerStore:
    def __init__(self) -> None:
        self.customers: List[Customer] = []

    def generate_customers(self, count: int = 100) -> None:
        fake = Faker()
        for _ in range(count):
            self.customers.append(
                Customer(
                    name=fake.name(),
                    email=fake.email(),
                    dob=fake.date_of_birth()
                )
            )

    def add_customer(self, customer: Customer) -> None:
        self.customers.append(customer)

    def get_all_customers(self) -> List[Customer]:
        return self.customers