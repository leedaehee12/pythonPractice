import requests
import config

def get_weather(city):
    api_key = config.API_KEY
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        if response.status_code == 200:
            return {
                'city': data['location']['name'],
                'temperature': data['current']['temp_c'],
                'condition': data['current']['condition']['text']
            }
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None
