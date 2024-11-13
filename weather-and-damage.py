import requests
import pandas as pd
import matplotlib.pyplot as plt

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
        
        # Organize weather data into a DataFrame
        weather_df = pd.DataFrame({
            'City': [city],
            'Temperature': [weather_data['main']['temp']],
            'Weather': [weather_data['weather'][0]['description']],
            'Humidity': [weather_data['main']['humidity']],
            'Wind Speed': [weather_data['wind']['speed']]
        })

        # Load asset valuation data
        asset_data = pd.read_csv("asset_valuation.csv")

        # Merge data on city
        merged_df = pd.merge(weather_df, asset_data, on='City')

        # Calculate new values (example: correlation between temperature and asset damage)
        correlation = merged_df['Temperature'].corr(merged_df['Asset Damage'])
        print(f"Correlation between temperature and asset damage: {correlation}")

        # Visualizations
        plt.figure(figsize=(12, 6))

        # Scatter plot: Temperature vs Asset Damage
        plt.subplot(1, 3, 1)
        plt.scatter(merged_df['Temperature'], merged_df['Asset Damage'])
        plt.xlabel('Temperature (°C)')
        plt.ylabel('Asset Damage ($)')
        plt.title('Temperature vs Asset Damage')

        # Scatter plot: Humidity vs Asset Damage
        plt.subplot(1, 3, 2)
        plt.scatter(merged_df['Humidity'], merged_df['Asset Damage'])
        plt.xlabel('Humidity (%)')
        plt.ylabel('Asset Damage ($)')
        plt.title('Humidity vs Asset Damage')

        # Bar plot: Weather Condition Frequency
        plt.subplot(1, 3, 3)
        weather_counts = merged_df['Weather'].value_counts()
        plt.bar(weather_counts.index, weather_counts.values)
        plt.xlabel('Weather Condition')
        plt.ylabel('Frequency')
        plt.title('Weather Condition Frequency')

        plt.tight_layout()
        plt.show()

    else:
        print("Weather data error:", weather_response.status_code)
else:
    print("Geolocation error:", geo_response.status_code)
