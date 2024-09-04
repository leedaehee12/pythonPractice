from flask import Flask, request, render_template
from api import get_weather , get_weather_forecast

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    # weather_info = get_weather(city)
    weather_info = get_weather_forecast(city)
    
    if weather_info:
        return render_template('weather.html', weather=weather_info)
    else:
        return "Failed to retrieve weather data.", 500

if __name__ == '__main__':
    app.run(debug=True)
