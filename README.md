# Weather Events Data Analysis

## About
This project aims to analyze and visualize weather event data sourced from the National Centers for Environmental Information (NCEI). The analysis focuses on various event types, their impacts on human life, and property damage. Using Python, the project creates several visualizations to help understand the frequency, severity, and geographical distribution of these events over a specified period.

## Data Sources
The data used in this project is obtained from the NCEI Storm Events Database. The specific dataset can be accessed and downloaded via the following URL:
- [NCEI Storm Events CSV](https://www.ncdc.noaa.gov/stormevents/csv?eventType=ALL&beginDate_mm=01&beginDate_dd=01&beginDate_yyyy=2011&endDate_mm=12&endDate_dd=31&endDate_yyyy=2012&county=MAGOFFIN%3A153&hailfilter=0.00&tornfilter=0&windfilter=000&sort=DT&submitbutton=Search&statefips=21%2CKENTUCKY)

API:
- https://www.ncdc.noaa.gov/cdo-web/token
## Installation

### Prerequisites
Ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/).

### Steps to Install on Windows, macOS, and Linux

1. **Clone the Repository**

## Create a Virtual Environment

python -m venv env

## Activate the Virtual Environment

Windows:
.\env\Scripts\activate

## macOS/Linux:

source env/bin/activate

## Install Dependencies

pip install -r requirements.txt

## Additional Steps for Linux Users
On some Linux distributions, you might need to install additional packages for Python to interact with system libraries. Use the following commands:

sudo apt-get update
sudo apt-get install python3-dev python3-pip python3-venv

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
After completing the installation steps, you can run the analysis and generate the visualizations using:

python analysis_script.py
This command will execute the script, process the data, and display the generated visualizations.