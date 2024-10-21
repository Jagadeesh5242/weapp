# app/data_fetcher.py
import requests
import os


class WeatherFetcher:
    def __init__(self, api_key, cities):
        self.api_key = api_key
        self.cities = cities
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def fetch_weather(self):
        weather_data = {}
        for city in self.cities:
            params = {
                'q': city,
                'appid': self.api_key
            }
            response = requests.get(self.base_url, params=params)
            if response.status_code == 200:
                data = response.json()
                weather_data[city] = data
        return weather_data
