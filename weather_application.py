import requests
import os

from dotenv import load_dotenv

# Load API Key from .env file
load_dotenv()
weatherstack_api_key = os.getenv("WEATHERSTACK_API_KEY")


# get weather function
def get_weather(city):
    base_url = "http://api.weatherstack.com/current"
    params = {
        "access_key": weatherstack_api_key,
        "query": city,
    }

    # make the API request
    response = requests.get(base_url, params=params)

    # check if request is success (code 200)
    if response.status_code == 200:
        data = response.json()

        #print(data) # use this to check for response from server

        # extract relevant info from response
        temperature = data['current']['temperature']
        weather_descriptions = data["current"]["weather_descriptions"][0]

        # return info to use it later if needed
        return temperature, weather_descriptions, city
    else:
        # account for status code other than 200 (failed request)
        print(f"Sorry, unable to connect to service and get data for {city}")


def user_input():
    print("Hello, welcome to the weather application")
    city_name = input("Please enter your city: ")
    return city_name


def display_data(city, temperature, weather_descriptions):
    # print weather info to terminal from response
    print(f"Current temperature in {city}: {temperature}°C")
    print(f"Weather conditions: {weather_descriptions}")


city = user_input()
weather_data = get_weather(city)
temperature, weather_descriptions, city = weather_data
display_data(city, temperature, weather_descriptions)
