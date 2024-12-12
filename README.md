# Weather Events Data Analysis

## About
This project aims to analyze and visualize weather event data sourced from the National Centers for Environmental Information (NCEI). The analysis focuses on various event types, their impacts on human life, and property damage. Using Python, the project creates several visualizations to help understand the frequency, severity, and geographical distribution of these events over a specified period.

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

Direct and indirect deaths by event type.

Injuries over time by event type.

Proportions of different event types.

Damage to property vs. damage to crops.

# Running the Project
once in VS Code, Navagate to Weather_Analysis then to Noaa_Weather_Analysis. Once there select run in the top right corner of the screen, a web page will appear where you can enter in dates and select a state and county. 
- In my data I used 

 State Kentucky / 01/01/2010 to 12/31/2024 / County Magoffin.

- once you enter in this data the screen will show the data requested. in the bottom left Right clink on the CSV download link and copy the link address.
 next you can take this data and under CSV_Alalysis paste it to csv_url (row 6)
 To deactivate the virtual environment when you're done, simply type `deactivate` in your terminal.

## Visualizations
Visualizations of the findings can be viewed on my [Tableau Public workbook]