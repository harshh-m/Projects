weather_data = {
    "mumbai": {"temp": 32, "condition": "Humid"},
    "delhi": {"temp": 38, "condition": "Sunny"},
    "bangalore": {"temp": 24, "condition": "Cloudy"},
    "kolkata": {"temp": 30, "condition": "Rainy"}
}

print("=== Simple Weather App ===")

city = input("Enter city name: ").lower()

if city in weather_data:

    print("\n=== Weather Report ===")

    print(f"City: {city.capitalize()}")
    print(f"Temperature: {weather_data[city]['temp']}°C")
    print(f"Condition: {weather_data[city]['condition']}")

else:
    print("City data not found.")