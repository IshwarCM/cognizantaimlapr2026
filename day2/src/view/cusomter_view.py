from store.customer_store import CustomerStore


class CustomerView:
    def __init__(self, store: CustomerStore) -> None:
        self.store = store

    def display_customers(self) -> None:
        for customer in self.store.get_all_customers():
            print(customer)