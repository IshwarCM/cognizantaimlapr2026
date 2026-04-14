from faker import Faker

"""
Entry point for the application.
Displays a random name using Faker.
"""

def run():
    fake = Faker()
    print(fake.name())

if __name__ == "__main__":
    run()