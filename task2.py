import requests
def get_weather(api_key, city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        temperature = data["main"]["temp"]
        weather_description = data["weather"][0]["description"]
        print(f"Weather in {city}: {temperature}°C, {weather_description}")
    else:
        print("Unable to fetch weather data. Please check the city name or API key.")
        
        


if __name__ == "__main__":
    api_key = "42c785ae7d04d7c93b9afa52e60c4b98"  
    while True:
        city = input("Enter the city name (or type 'exit' to quit): ")
        if city.lower() == 'exit':
            break  
        get_weather(api_key, city)
    
