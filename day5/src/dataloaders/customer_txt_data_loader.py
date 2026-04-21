# create customer txt data loader implementation from customer data loader abstract class

from src.models.customer import Customer
from src.models.full_name import FullName
from src.dataloaders.customer_data_loader import CustomerDataLoader
from src.stores.customer_store_impl import CustomerStoreImpl


class CustomerTXTDataLoader(CustomerDataLoader):
    def load_data(self, file_path, customer_store: CustomerStoreImpl):
        with open(file_path, 'r') as file:
            lines = file.readlines()

        customer_data = {}

        for line in lines:
            line = line.strip()

            # Blank line indicates end of one customer record
            if not line:
                if customer_data:
                    self._create_and_add_customer(customer_data, customer_store)
                    customer_data = {}
                continue

            key, value = line.split(":", 1)
            customer_data[key.strip()] = value.strip()

        # Handle last customer (if file does not end with blank line)
        if customer_data:
            self._create_and_add_customer(customer_data, customer_store)

    def _create_and_add_customer(self, data, customer_store):
        customer = Customer(
            customer_id=int(data["customer_id"]),
            name=FullName(
                first_name=data["first_name"],
                last_name=data["last_name"]
            ),
            email=data["email"],
            phone_no=data["phone_no"]
        )

        customer_store.add_customer(customer)