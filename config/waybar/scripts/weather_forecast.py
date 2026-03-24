import json
import requests

CITY = ""
API_KEY = ""
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric&lang=ru"

icons = {
    "Clear": "☀️",
    "Clouds": "☁️",
    "Rain": "🌧️",
    "Drizzle": "🌦️",
    "Thunderstorm": "⛈️",
    "Snow": "❄️",
    "Mist": "🌫️",
    "Smoke": "🌫️",
    "Haze": "🌫️",
    "Dust": "🌫️",
    "Fog": "🌫️",
}

try:
    r = requests.get(URL)
    data = r.json()
    
    if data.get("cod") == 200:
        main_weather = data["weather"][0]["main"]
        icon = icons.get(main_weather, "🌡️")
        temp = round(data["main"]["temp"])
        desc = data["weather"][0]["description"].capitalize()
        
        output = {
            "text": f"{icon} {temp}°C",
            "tooltip": f"{desc}\nОщущается как: {round(data['main']['feels_like'])}°C\nВлажность: {data['main']['humidity']}%"
        }
        print(json.dumps(output))
    else:
        print(json.dumps({"text": "⌛", "tooltip": f"Ожидание активации ключа или ошибка: {data.get('message')}"}))

except Exception as e:
    print(json.dumps({"text": "断", "tooltip": f"Ошибка сети: {str(e)}"}))

