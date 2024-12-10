import pandas as pd
import matplotlib.pyplot as plt
import requests

# URL of the CSV file
csv_url = "https://www.ncdc.noaa.gov/stormevents/csv?eventType=ALL&beginDate_mm=01&beginDate_dd=01&beginDate_yyyy=2012&endDate_mm=12&endDate_dd=31&endDate_yyyy=2012&county=MAGOFFIN%3A153&hailfilter=0.00&tornfilter=0&windfilter=000&sort=DT&submitbutton=Search&statefips=21%2CKENTUCKY"

# Send a GET request to the URL and save the content to a local file
response = requests.get(csv_url)
csv_file_path = "storm_events.csv"
with open(csv_file_path, "wb") as file:
    file.write(response.content)

print("CSV file downloaded successfully!")

# Load CSV data into a DataFrame
df = pd.read_csv(csv_file_path)

# Convert the BEGIN_DATE column to datetime format
df['BEGIN_DATE'] = pd.to_datetime(df['BEGIN_DATE'])

# Group by EVENT_TYPE and BEGIN_DATE, then calculate the sum of relevant columns
grouped_df = df.groupby(['EVENT_TYPE', 'BEGIN_DATE']).agg({
    'DEATHS_DIRECT': 'sum',
    'DEATHS_INDIRECT': 'sum',
    'INJURIES_DIRECT': 'sum',
    'INJURIES_INDIRECT': 'sum',
    'DAMAGE_PROPERTY_NUM': 'sum',
    'DAMAGE_CROPS_NUM': 'sum'
}).reset_index()

# Plot the data
fig, ax = plt.subplots(3, 1, figsize=(12, 18))

# Plot Deaths over Time
for event_type in grouped_df['EVENT_TYPE'].unique():
    event_data = grouped_df[grouped_df['EVENT_TYPE'] == event_type]
    ax[0].plot(event_data['BEGIN_DATE'], event_data['DEATHS_DIRECT'], label=f'{event_type} - Direct Deaths')
    ax[0].plot(event_data['BEGIN_DATE'], event_data['DEATHS_INDIRECT'], label=f'{event_type} - Indirect Deaths', linestyle='--')
ax[0].set_title('Deaths by Event Type Over Time')
ax[0].set_xlabel('Date')
ax[0].set_ylabel('Number of Deaths')
ax[0].legend()
ax[0].tick_params(axis='x', rotation=45)

# Plot Injuries over Time
for event_type in grouped_df['EVENT_TYPE'].unique():
    event_data = grouped_df[grouped_df['EVENT_TYPE'] == event_type]
    ax[1].plot(event_data['BEGIN_DATE'], event_data['INJURIES_DIRECT'], label=f'{event_type} - Direct Injuries')
    ax[1].plot(event_data['BEGIN_DATE'], event_data['INJURIES_INDIRECT'], label=f'{event_type} - Indirect Injuries', linestyle='--')
ax[1].set_title('Injuries by Event Type Over Time')
ax[1].set_xlabel('Date')
ax[1].set_ylabel('Number of Injuries')
ax[1].legend()
ax[1].tick_params(axis='x', rotation=45)

# Plot Damages over Time
for event_type in grouped_df['EVENT_TYPE'].unique():
    event_data = grouped_df[grouped_df['EVENT_TYPE'] == event_type]
    ax[2].plot(event_data['BEGIN_DATE'], event_data['DAMAGE_PROPERTY_NUM'], label=f'{event_type} - Property Damage')
    ax[2].plot(event_data['BEGIN_DATE'], event_data['DAMAGE_CROPS_NUM'], label=f'{event_type} - Crop Damage', linestyle='--')
ax[2].set_title('Damages by Event Type Over Time')
ax[2].set_xlabel('Date')
ax[2].set_ylabel('Damage ($)')
ax[2].legend()
ax[2].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()
