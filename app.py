from flask import Flask, render_template, request
import requests
from config import apikey

app = Flask(__name__)


@app.route('/')
def home():

    return render_template("home.html")


@app.route('/location-weather', methods=['GET', 'POST'])
def location_weather():
    location = str(request.form.get("search")) 

    param = {"q": location}
    
    response = requests.get(url="https://nominatim.openstreetmap.org/search?format=json&limit=1", params=param)

    if response.status_code == 200:
        lat = response.json()[0]['lat']
        lon = response.json()[0]['lon']
        params = {"lat": lat, "lon": lon, "appid": apikey}
        weather_response = requests.get("https://api.openweathermap.org/data/2.5/weather?units=metric", params=params)

        if weather_response.status_code == 200:
            weather_description = weather_response.json()['weather'][0]['description']

            weather_icon = weather_response.json()['weather'][0]['icon']

            current_temperature = weather_response.json()['main']['temp']
            humidity = weather_response.json()['main']['humidity']
            pressure = weather_response.json()['main']['pressure']
            
            
            return render_template("location.html", location=location, description=weather_description, temp=current_temperature, humidity=humidity, pressure=pressure, icon=weather_icon)




if __name__ == "__main__":
    app.run(debug=True)


