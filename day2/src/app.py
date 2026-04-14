from faker import Faker
from datetime import date

from store.customer_store import CustomerStore
from view.customer_view import CustomerView
from models.customer import Customer


def main() -> None:
    store = CustomerStore()
    view = CustomerView(store)

    fake = Faker()

    for _ in range(5):
        customer = Customer(
            name=fake.name(),
            email=fake.email(),
            dob=date.today()
        )
        store.add_customer(customer)

    view.display_customers()


if __name__ == "__main__":
    main()