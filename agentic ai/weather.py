
import json
from urllib.request import urlopen
from urllib.parse import urlencode

def get_weather(city):
    try:
        # Find the city coordinates
        url = "https://geocoding-api.open-meteo.com/v1/search?"
        params = urlencode({"name": city, "count": 1})
        
        with urlopen(url + params, timeout=10) as response:
            location_data = json.loads(response.read())

        if not location_data.get("results"):
            print("City not found. Please try again.")
            return

        location = location_data["results"][0]
        lat = location["latitude"]
        lon = location["longitude"]

        # Get current weather
        url = "https://api.open-meteo.com/v1/forecast?"
        params = urlencode({
            "latitude": lat,
            "longitude": lon,
            "current": (
                "temperature_2m,relative_humidity_2m,"
                "apparent_temperature,precipitation,"
                "weather_code,wind_speed_10m"
            ),
            "timezone": "auto"
        })

        with urlopen(url + params, timeout=10) as response:
            data = json.loads(response.read())

        current = data["current"]

        weather_codes = {
            0: "Clear sky",
            1: "Mainly clear",
            2: "Partly cloudy",
            3: "Overcast",
            45: "Fog",
            48: "Fog",
            51: "Light drizzle",
            53: "Moderate drizzle",
            55: "Heavy drizzle",
            61: "Light rain",
            63: "Moderate rain",
            65: "Heavy rain",
            71: "Light snow",
            73: "Moderate snow",
            75: "Heavy snow",
            80: "Rain showers",
            81: "Moderate rain showers",
            82: "Heavy rain showers",
            95: "Thunderstorm",
            96: "Thunderstorm with hail",
            99: "Thunderstorm with heavy hail"
        }

        print("\n" + "=" * 35)
        print(f"WEATHER REPORT: {location['name']}")
        print(f"Country: {location.get('country', 'Unknown')}")
        print("=" * 35)
        print(f"Local time     : {current['time']}")
        print(f"Condition      : {weather_codes.get(current['weather_code'], 'Other conditions')}")
        print(f"Temperature    : {current['temperature_2m']} °C")
        print(f"Feels like     : {current['apparent_temperature']} °C")
        print(f"Humidity       : {current['relative_humidity_2m']} %")
        print(f"Precipitation  : {current['precipitation']} mm")
        print(f"Wind speed     : {current['wind_speed_10m']} km/h")
        print("=" * 35)
        print("Weather data by Open-Meteo.com\n")

    except Exception as error:
        print(f"Error fetching weather: {error}")


while True:
    city = input("Enter city name (or 'exit' to quit): ").strip()

    if city.lower() == "exit":
        print("Goodbye!")
        break

    if city:
        get_weather(city)
    else:
        print("Please enter a city name.")
