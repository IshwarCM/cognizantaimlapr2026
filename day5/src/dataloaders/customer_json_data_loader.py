# create customer json data loader implementation from customer data loader abstract class

import json
from src.models.customer import Customer
from src.models.full_name import FullName
from src.dataloaders.customer_data_loader import CustomerDataLoader
from src.stores.customer_store_impl import CustomerStoreImpl

class CustomerJSONDataLoader(CustomerDataLoader):
    def load_data(self, file_path, customer_store: CustomerStoreImpl):
        with open(file_path, 'r') as file:
            data = json.load(file)

        for record in data:
            customer_id = int(record['customer_id'])
            first_name = record['first_name']
            last_name = record['last_name']
            email = record['email']
            phone_no = record['phone_no']

            full_name = FullName(
                first_name=first_name,
                last_name=last_name
            )

            customer = Customer(
                customer_id=customer_id,
                name=full_name,
                email=email,
                phone_no=phone_no
            )

            customer_store.add_customer(customer)