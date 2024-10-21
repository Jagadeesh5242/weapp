import requests
from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

API_KEY = '9358ba2a4f81684a8b15a99a4708369a'  # Replace with your actual API key

# MongoDB setup
mongo_client = MongoClient("mongodb://mongo:27017")
db = mongo_client.weather_db


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


def get_weather_for_city(city):
    URL = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    response = requests.get(URL)

    if response.status_code == 200:
        data = response.json()
        print(f"Weather data for {city}: {data}")
        return process_weather_data(data, city)  # Pass city here
    else:
        print(f"Error fetching data for {city}: {response.status_code}")
        return None


def process_weather_data(data, city):
    temp_kelvin = data['main']['temp']
    temp_celsius = kelvin_to_celsius(temp_kelvin)
    main_condition = data['weather'][0]['main']
    timestamp = data['dt']

    print(f"Processed Data - Temp: {temp_celsius}°C, Condition: {main_condition}, Time: {timestamp}")

    weather_entry = {
        'city': city,  # Now this will be defined
        'temp_celsius': temp_celsius,
        'condition': main_condition,
        'timestamp': timestamp
    }

    # Store the weather data in MongoDB
    db.weather_data.insert_one(weather_entry)

    return weather_entry


@app.route('/weather/<city>', methods=['GET'])
def weather(city):
    weather_data = get_weather_for_city(city)
    if weather_data:
        return jsonify(weather_data), 200
    else:
        return jsonify({'error': 'Could not fetch weather data'}), 500


if __name__ == '__main__':
    app.run(debug=True)
