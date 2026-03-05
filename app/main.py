import requests
from dotenv import load_dotenv
import os


load_dotenv()

API_KEY = os.getenv("API_KEY")

URL = "https://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"


def get_weather() -> None:
    result = requests.get(URL, params={"key": API_KEY, "q": FILTERING})
    print("Performing request to Weather API for city Paris...")
    print(
        f"{result.json()["location"]["name"]}/"
        f"{result.json()["location"]["country"]} "
        f"{result.json()["location"]["localtime"]}"
        f" Weather {result.json()["current"]["temp_c"]} "
        f"Celsius"
    )


if __name__ == "__main__":
    get_weather()
