import requests


class APIClient:
    """Simulates API client"""

    def get_user_data(self, user_id: str) -> dict:
        response = requests.get(f"https://api.example.com/users/{user_id}")
        response.raise_for_status()
        return response.json()


class UserService:
    """Fetch data"""

    def __init__(self, api_client: APIClient):
        self.api_client = api_client

    def get_username(self, user_id: int):
        user_data = self.api_client.get_user_data(user_id)
        return user_data["name"].upper()
