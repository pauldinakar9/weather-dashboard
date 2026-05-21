from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timezone, timedelta

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("API_KEY")


def get_weather(city):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    data = response.json()

    if response.status_code == 200:

        timezone_offset = data['timezone']

        local_time = datetime.now(
            timezone.utc
        ) + timedelta(seconds=timezone_offset)

        return {

            "city": data['name'],
            "country": data['sys']['country'],
            "temp": data['main']['temp'],
            "humidity": data['main']['humidity'],
            "description": data['weather'][0]['description'].title(),
            "wind": data['wind']['speed'],
            "timezone": timezone_offset // 3600,
            "local_time": local_time.strftime('%Y-%m-%d %H:%M:%S'),
            "icon": data['weather'][0]['icon'],
            "main": data['weather'][0]['main']
        }

    else:

        return {

            "city": city,
            "country": "",
            "temp": "--",
            "humidity": "--",
            "description": "City Not Found",
            "wind": "--",
            "timezone": "--",
            "local_time": "--",
            "icon": "01d",
            "main": "Clear"
        }


def get_forecast(city):

    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    data = response.json()

    forecast_data = []

    if response.status_code == 200:

        forecasts = data["list"]

        for i in range(0, 40, 8):

            item = forecasts[i]

            forecast_data.append({

                "date": item["dt_txt"].split(" ")[0],

                "temp": item["main"]["temp"],

                "description": item["weather"][0]["description"].title(),

                "icon": item["weather"][0]["icon"]

            })

    return forecast_data


@app.route('/', methods=['GET', 'POST'])
def home():

    cities = ["Hyderabad", "London", "New York"]

    if request.method == 'POST':

        cities = [

            request.form['city1'],
            request.form['city2'],
            request.form['city3']
        ]

    weather_data = []

    for city in cities:

        weather = get_weather(city)

        weather["forecast"] = get_forecast(city)

        weather_data.append(weather)

    return render_template(
        "index.html",
        weather_data=weather_data,
        cities=cities
    )


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
