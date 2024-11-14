import requests
import pandas as pd
import matplotlib.pyplot as plt

# Function to fetch weather data
def fetch_weather_data(city, state_code, country_code, api_key):
    geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state_code},{country_code}&limit=1&appid={api_key}"
    geo_response = requests.get(geo_url)
    if geo_response.status_code == 200:
        geo_data = geo_response.json()
        lat = geo_data[0]['lat']
        lon = geo_data[0]['lon']
        
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=imperial"
        weather_response = requests.get(weather_url)
        if weather_response.status_code == 200:
            return weather_response.json(), lat, lon
        else:
            print(f"Weather API response code: {weather_response.status_code}")
            print(f"Weather API response content: {weather_response.content}")
    else:
        print(f"Geo API response code: {geo_response.status_code}")
        print(f"Geo API response content: {geo_response.content}")
    return None, None, None

# API key and city details
api_key = "Add API Here"
city = "Add city name"
state_code = "add state code"
country_code = "US"

# Fetch weather data
weather_data, lat, lon = fetch_weather_data(city, state_code, country_code, api_key)
if weather_data:
    weather_df = pd.DataFrame({
        'City': [city],
        'Temperature (F)': [weather_data['main']['temp']],
        'Weather': [weather_data['weather'][0]['description']],
        'Humidity (%)': [weather_data['main']['humidity']],
        'Wind Speed (mph)': [weather_data['wind']['speed']],
        'Latitude': [lat],
        'Longitude': [lon]
    })
    
    # Save DataFrame to CSV
    csv_file_path = 'weather_data_imperial.csv'
    weather_df.to_csv(csv_file_path, index=False)
    print(f"Weather data saved to {csv_file_path}")
    
    # Visualize the weather data
    plt.figure(figsize=(10, 6))
    plt.bar(weather_df['Weather'], weather_df['Temperature (F)'], color='blue', alpha=0.7)
    plt.xlabel('Weather Condition')
    plt.ylabel('Temperature (°F)')
    plt.title('Weather Condition vs Temperature (F)')
    plt.show()

    print(weather_df)
else:
    print("Failed to fetch weather data.")

