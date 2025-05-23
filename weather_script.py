import requests

def get_weather():
    url = "http://api.weatherapi.com/v1/current.json?key=4d3f455d0deb4362a69151009252305&q=Santiago&aqi=no"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        location = data['location']['name']
        country = data['location']['country']
        temp_c = data['current']['temp_c']
        condition = data['current']['condition']['text']
        humidity = data['current']['humidity']
        wind_kph = data['current']['wind_kph']

        print(f"Clima actual en {location}, {country}:")
        print(f"Temperatura: {temp_c}°C")
        print(f"Condición: {condition}")
        print(f"Humedad: {humidity}%")
        print(f"Viento: {wind_kph} km/h")
    except requests.RequestException as e:
        print("Error al obtener los datos del clima:", e)
    except KeyError:
        print("Error al procesar los datos del clima.")

if __name__ == "__main__":
    get_weather()