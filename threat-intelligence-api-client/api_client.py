import requests


def get_random_users():
    url = "https://jsonplaceholder.typicode.com/users"

    try:
        response = requests.get(url, timeout=10)

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as error:
        print(f"Request failed: {error}")
        return []


def display_users(users):

    print("========== API RESULTS ==========\n")

    for user in users:

        print(f"Name: {user['name']}")
        print(f"Email: {user['email']}")
        print(f"Company: {user['company']['name']}")
        print("--------------------------------")


users = get_random_users()

display_users(users)