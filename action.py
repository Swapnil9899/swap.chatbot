import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionFetchWeather(Action):
    def name(self):
        return "action_fetch_weather"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        location = tracker.get_slot("location")
        if location:
            api_key = "your_openweather_api_key"
            url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
            response = requests.get(url).json()
            if response.get("weather"):
                weather = response["weather"][0]["description"]
                dispatcher.utter_message(text=f"The weather in {location} is {weather}.")
            else:
                dispatcher.utter_message(text="I couldn't fetch the weather. Please try again.")
        else:
            dispatcher.utter_message(text="Please provide a location.")
        return []
