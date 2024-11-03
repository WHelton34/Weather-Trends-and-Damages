import requests
import pandas as pd

# Your API key here
api_key = "1bc5f6c932a96b283e4e26d1f4d91bc2"
# City, state, and country code
city = "Lexington"
state_code = "KY"
country_code = "us"

# Fetch geolocation data
geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state_code},{country_code}&limit=1&appid={api_key}"
geo_response = requests.get(geo_url)

if geo_response.status_code == 200:
    geo_data = geo_response.json()
    lat = geo_data[0]['lat']
    lon = geo_data[0]['lon']
    
    # Fetch weather data
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    weather_response = requests.get(weather_url)
    
    if weather_response.status_code == 200:
        weather_data = weather_response.json()
        print(weather_data)
        
        # Fetch damage data
        damage_url = "https://services.dat.noaa.gov/arcgis/rest/services/nws_damageassessmenttoolkit/DamageViewer/FeatureServer"
        damage_response = requests.get(damage_url)
        
        if damage_response.status_code == 200:
            damage_data = damage_response.json()
            print(damage_data)
            
            # Organize data into a DataFrame
            weather_df = pd.DataFrame({
                'City': [city],
                'Temperature': [weather_data['main']['temp']],
                'Weather': [weather_data['weather'][0]['description']],
                'Humidity': [weather_data['main']['humidity']],
                'Wind Speed': [weather_data['wind']['speed']]
            })
            print(weather_df)
        else:
            print("Damage data error:", damage_response.status_code)
    else:
        print("Weather data error:", weather_response.status_code)
else:
    print("Geolocation error:", geo_response.status_code)



