import pandas as pd
import matplotlib.pyplot as plt

# Download the CSV file
csv_url = "https://www.ncdc.noaa.gov/stormevents/csv?eventType=ALL&beginDate_mm=07&beginDate_dd=01&beginDate_yyyy=2023&endDate_mm=07&endDate_dd=31&endDate_yyyy=2024&county=MAGOFFIN%3A153&hailfilter=0.00&tornfilter=0&windfilter=000&sort=DT&submitbutton=Search&statefips=21%2CKENTUCKY"

# Load CSV data into a DataFrame
df = pd.read_csv(csv_url)

# Display first few rows of the DataFrame
print(df.head())

# Example Visualization
# Plot a histogram of the event types
df['EVENT_TYPE'].value_counts().plot(kind='bar', figsize=(12, 6))
plt.title('Number of Each Event Type')
plt.xlabel('Event Type')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.show()
