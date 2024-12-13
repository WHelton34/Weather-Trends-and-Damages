# Weather Events Data Analysis

## About
This project aims to analyze and visualize weather event data sourced from the National Centers for Environmental Information (NCEI). The analysis focuses on various event types, their impacts on human life, property damage and damage to crops. Using Python, the project creates several visualizations to help understand the frequency, severity, and geographical distribution of these events over a specified period.

## Data Sources
The data used in this project is obtained from the NCEI Storm Events Database. The specific dataset can be accessed and downloaded via the following URL:
- https://www.ncdc.noaa.gov/stormevents/csv?eventType=ALL&beginDate_mm=01&beginDate_dd=01&beginDate_yyyy=2010&endDate_mm=12&endDate_dd=31&endDate_yyyy=2024&county=MAGOFFIN%3A153&hailfilter=0.00&tornfilter=0&windfilter=000&sort=DT&submitbutton=Search&statefips=21%2CKENTUCKY

API:
- https://home.openweathermap.org/users/sign_up

Once you sign up the website will send you an API Key needed for the Quick Current Weather file. 
## Installation

### Prerequisites
Ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/).

### Steps to Install on Windows, macOS, and Linux

1. **Clone the Repository**
```
https://github.com/WHelton34/Weather-Trends-and-Damages.git
```
2. **Create a Virtual Environment**
```
python -m venv myenv
```
3. **Activate the Virtual Environment**

Windows:
```
.\myenv\Scripts\activate
```
On macOS/Linux:
```
source myenv/bin/activate
```
4. **Install Dependencies**
```
pip install -r requirements.txt
```
## Additional Steps for Linux Users
On some Linux distributions, you might need to install additional packages for Python to interact with system libraries. Use the following commands:
```
sudo apt-get update
sudo apt-get install python3-dev python3-pip python3-venv
```
# Summary of the Project
The Weather Events Data Analysis project involves the following key steps:

Data Collection: Fetching the weather event data from NCEI's Storm Events Database.

Data Cleaning and Preparation: Parsing the CSV data, handling missing values, and preparing it for analysis.

Data Analysis and Visualization: Using libraries like pandas, matplotlib, and seaborn to create various visualizations such as bar plots, line plots, scatter plots, and pie charts. These visualizations display:

The number of different event types.

Deaths by event type.

Damage to property.

Damage to crops.

Weather Events over Time.

# Running the Project

To run Noaa_Weather_Analysis Navagate to the Weather_Analysis tab in VS code. then to Noaa_Weather_Analysis. Once there select run in the top right corner of the screen, a web page will appear where you can enter in dates and select a state and county. 
- In my data I used 

 State Kentucky / 01/01/2010 to 12/31/2024 / County Magoffin.

- once you enter in this data the screen will show the data requested. in the bottom left of the screen you will see a CSV link. Right click on the CSV download link and copy the link address.
 next you can take this data and under CSV_Alalysis paste it to csv_url (row 6) and now you can click Run in the top right corner of the screen. this will produce the csv file Storm_events and automaticaly clean the data and create Cleaned_Data csv. 

- to run the Quick_Current_Weather file you must first go to the provided API link and create an account. you will them recive a email with the API key. Using that key you can now copy and paste it into row 27 in Quick_Current_Weather along with the city and state code (ex:KY, TN, WV). This will give you basic information from the JSON file used by the API website and in the terminal show you a overview of the weather in the selected location. 

 To deactivate the virtual environment when you're done, simply type `deactivate` in your terminal.

## Visualizations
Visualizations of the findings can be viewed on my [Tableau Public workbook] https://public.tableau.com/app/profile/william.helton/viz/WeatherTrendsAnalysis/Sheet1

## Summary of Findings

### Damage to Crops
In my data I was able to determine that in the county of Magoffin most crop damage is due to Thunderstorms in the area and the next leading causes all include wind as well. my data showes a small percentage of damage caused by floodig in the area as well. With this data in hand and easily visible it can be inferred that a great way to reduce the damage to crops and incrrease yeild would be to Cover the soil with crop residues or cover crops to protect it from erosive winds and/or Install windbreaks, hedgerows, or vegetative wind barriers to reduce wind exposure for sensitive crops.

### Damage to Property
looking over the date here we can see that Flooding is a major cause for Damage to property in magoffin county, with this information its clear that im proved Drainage and Storm Drains as well as Waterway overflow should be focused on to improve this statistic and create a safer area to live. Due to a devistating tornad in 2012 the data also showes a Massive amount of damage, Around 25 million USD, to the county. Even though it seems to be an isolated event, It showes that preperations should be made and actions taken to help protect the county from further tornado damage. 

### Weather Event Over Time
In this tab we can see a visualization of the diffrent weather events and how many occured on a month to month basis from 2010 to 2024. This is a great way to observe the weather of the area and could be used to help predict future weather events based off trends found in this visualization. 

## Code Louisville Data Analysis Capstone Requirements
**Category 1: Loading Data:**
- Read TWO data files (JSON, CSV, ). 

**Category 2: Clean and Operate the Data While Combining Them:**
- Clean your data and perform a pandas merge with your two data sets, then calculate some new values based on the new data set.  

**Category 3: Visualize/Present Your Data:**
- Make a Tableau dashboard to display your data
  
**Category 4: Best Practices:**
- Utilize a virtual environment and include instructions in your README on how the user should set one up

**Category 5: Interpretation of Your Data:**
- Annotate your .py files with well-written comments and a clear README.md (only applicable if you’re not using a jupyter notebook).