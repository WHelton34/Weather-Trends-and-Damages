import requests
import pandas as pd

# Define the API endpoint
url = "https://services.dat.noaa.gov/arcgis/rest/services/nws_damageassessmenttoolkit/DamageViewer/FeatureServer/0/query"

# Specify your city
city_name = "Lexington"
state_code = "KY"
country_code = "US"

# Define query parameters
params = {
    "where": f"city = '{city_name}' AND state = '{state_code}' AND country = '{country_code}'",
    "outFields": "*",
    "f": "json",
    "time_start": "2023-01-01T00:00:00Z",
    "time_end": "2023-12-31T23:59:59Z"
}

# Send the query
response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print(data)
    
    # Convert JSON data to DataFrame
    df = pd.json_normalize(data['features'])
    
    # Display the first few rows of the DataFrame
    print(df.head())
    
    # Save the DataFrame to a CSV file
    df.to_csv("asset_damage_data.csv", index=False)
else:
    print("Error:", response.status_code)
