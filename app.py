from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def home():


    return render_template("home.html")


@app.route('/location-weather', methods=['GET', 'POST'])
def location_weather():
    return render_template("location.html", location='brazil')






if __name__ == "__main__":
    app.run(debug=True)


