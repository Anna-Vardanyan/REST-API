import requests
import random
from faker import Faker

API_BASE_URL = "http://localhost:8000"
faker = Faker()

def post_data(endpoint, data):
    response = requests.post(f"{API_BASE_URL}/{endpoint}/", json=data)
    if response.status_code == 201:
        print(f"Successfully created {endpoint[:-1]}: {response.json()}")
        return response.json()
    else:
        print(f"Failed to create {endpoint[:-1]}: {response.status_code} - {response.text}")
        return None


def load_operators(count=7):
    operators = []
    for _ in range(count):
        operator = {
            "name": faker.company(),
            "operator_code": faker.unique.bothify(text="???###"),
            "number_count": faker.random_int(min=1000, max=10000),
        }
        created_operator = post_data("operators", operator)
        if created_operator:
            operators.append(created_operator)
    return operators


def load_subscribers(count=20):
    subscribers = []
    for _ in range(count):
        subscriber = {
            "passport_data": faker.unique.bothify(text="##??????"),
            "full_name": faker.name(),
            "address": faker.address(),
        }
        created_subscriber = post_data("subscribers", subscriber)
        if created_subscriber:
            subscribers.append(created_subscriber)
    return subscribers


def load_connections(operators, subscribers, count=20):
    operators = requests.get(f"{API_BASE_URL}/operators/", params={"page": 0, "page_size": 10}).json()
    subscribers = requests.get(f"{API_BASE_URL}/subscribers/", params={"page": 0, "page_size": 50}).json()
    connections = []
    for _ in range(count):
        operator = random.choice(operators)
        subscriber = random.choice(subscribers)
        connection = {
            "operator_id": operator["id"],
            "subscriber_id": subscriber["id"],
            "phone_number": faker.phone_number(),
            "tariff_plan": faker.random_element(["Basic", "Standard", "Premium"]),
            "debt": faker.random.uniform(0, 100),
            "installation_date": faker.date_this_decade().strftime("%Y-%m-%d"),
        }
        created_connection = post_data("connections", connection)
        if created_connection:
            connections.append(created_connection)
    return connections


def main():
    print("Loading data...")
    operators = load_operators(10)
    subscribers = load_subscribers(50)
    connections = load_connections(operators, subscribers, 50)
    print("Data loading completed.")

if __name__ == "__main__":
    main()