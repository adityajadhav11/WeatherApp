from flask import Flask, render_template, request # type: ignore
import requests # type: ignore

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
API_KEY = '1f43cb78cbb425068a741dd51e3d6e3e'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    if request.method == "POST":
        city = request.form.get("city")
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                "city": city,
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"].capitalize(),
                "humidity": data["main"]["humidity"],
                "pressure": data["main"]["pressure"],
            }
        else:
            weather_data = {"error": "City not found or an error occurred."}
    return render_template("index.html", weather=weather_data)

if __name__ == "__main__":
    app.run(debug=False)
