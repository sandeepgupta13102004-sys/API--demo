import requests
USER_API_URL = "http://127.0.0.1.5001/students"


def get_user_from_api(user_id):
    response = requests.get(f"{USER_API_URL}/{user_id}") 

    if response.status_code == 200:
        return response.json()

    return None

