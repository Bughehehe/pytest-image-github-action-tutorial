from typing import Optional
import requests


def get_weather(temp: int) -> str:
    if temp > 20:
        return "hot"
    else:
        return "cold"


def add(a: float, b: float) -> float:
    return a + b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, username: str, email: str) -> bool:
        if username in self.users:
            raise ValueError("User already exists")
        self.users[username] = email
        return True

    def get_user(self, username: str) -> str:
        return self.users.get(username)


class Database:
    """Simulates basic in memory database"""

    def __init__(self):
        self.data = {}

    def add_user(self, user_id: int, name: str) -> None:
        if user_id in self.data:
            raise ValueError("User already exists")
        self.data[user_id] = name
        # return True

    def get_user(self, user_id: int) -> Optional[str]:  # returns str or None
        return self.data.get(user_id, None)

    def delete_user(self, user_id: int) -> None:
        if user_id in self.data:
            del self.data[user_id]


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_weather_api(city: str) -> dict | None:
    try:
        response = requests.get(f"https://api.weather.com/v1/{city}", timeout=5)
        response.raise_for_status()  # raises HTTPError for 4xx/5xx
        return response.json()
    except requests.exceptions.HTTPError as e:
        print("HTTP error occurred:", e)
    except requests.exceptions.ConnectionError as e:
        print("Connection error occurred:", e)
    except requests.exceptions.Timeout as e:
        print("The request timed out:", e)
    except requests.exceptions.RequestException as e:
        # catches any other requests-related errors
        print("A request error occurred:", e)
    return None
