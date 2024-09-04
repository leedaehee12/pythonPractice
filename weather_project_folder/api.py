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

def get_weather_forecast(city):
    api_key = config.API_KEY
    url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&hours=5"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        forecast = []

        if response.status_code == 200 and 'forecast' in data:
            # 시간별 예보 데이터를 가져옵니다.
            forecast_data = data['forecast']['forecastday'][0]['hour']

            for entry in forecast_data[:5]:  # 처음 5개의 시간별 예보만 표시
                forecast.append({
                    'time': entry['time'],
                    'temperature': entry['temp_c'],
                    'condition': entry['condition']['text']
                })

            # 이제 반환할 데이터를 설정합니다.
            return {
                'city': data['location']['name'],
                'temperature': forecast[0]['temperature'],  # 첫 번째 시간의 온도를 현재 온도로 사용
                'condition': forecast[0]['condition'],  # 첫 번째 시간의 날씨 상태를 현재 상태로 사용
                'forecast': forecast  # 시간별 예보 데이터 추가
            }
        else:
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None
