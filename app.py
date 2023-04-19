from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def home():
    # response = request.get("")

    return render_template("home.html")


@app.route('/location-weather', methods=['GET', 'POST'])
def location_weather():
    location = str(request.form.get("search").replace(" ", "+"))
    response = requests.get("https://nominatim.openstreetmap.org/search?q={location}&format=json&limit=1")
    lat = response.json()[0]['lat']
    lon = response.json()[0]['lon']

    reverse_test = requests.get("https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=jsonv2")

    return render_template("location.html", location=reverse_test, lat=lat, lon=lon)






if __name__ == "__main__":
    app.run(debug=True)


