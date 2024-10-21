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
