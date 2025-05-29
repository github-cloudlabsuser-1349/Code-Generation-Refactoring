import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        main = data.get('main', {})
        weather = data.get('weather', [{}])[0]
        print(f"Weather in {city}:")
        print(f"Temperature: {main.get('temp', 'N/A')}°F")
        print(f"Humidity: {main.get('humidity', 'N/A')}%")
        print(f"Condition: {weather.get('main', 'N/A')}")
        print(f"Description: {weather.get('description', 'N/A').title()}")
    else:
        print("Failed to fetch weather data. Please check the city name or API key.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    #api_key = input("Enter your OpenWeatherMap API key: ")
    api_key = "aad2321125274b2c9a58d0fcce511e8c"
    get_weather(city, api_key)