from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO)

# Define the download directory
download_directory = "/path/to/download/directory"  # Change to your desired directory

# Initialize WebDriver with Chrome options to handle CSV downloads
options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": download_directory,  # Change to your desired directory
    "download.prompt_for_download": False,
}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Function to fetch the CSV URL and trigger download
def fetch_csv_url(driver):
    driver.get("https://www.ncdc.noaa.gov/stormevents/choosedates.jsp?statefips=-999%2CALL")
    driver.implicitly_wait(30)  # Adjust this value as needed
    wait = WebDriverWait(driver, 60)  # Increase the explicit wait time

    try:
        state_select_element = wait.until(EC.presence_of_element_located((By.NAME, "statefips")))
        logging.info("State dropdown located.")
        
        state_select = Select(state_select_element)
        state_select.select_by_value("-999,ALL")
        logging.info("Selected 'All States and Areas'.")
    except Exception as e:
        logging.error(f"Exception: {e}")
        return None

    # Handle unexpected alerts
    try:
        alert = driver.switch_to.alert
        alert_text = alert.text
        logging.info(f"Alert text: {alert_text}")
        alert.accept()  # Accept the alert
    except Exception as e:
        logging.info("No alert present.")

    # Wait for checkboxes to be present
    try:
        wait.until(EC.presence_of_all_elements_located((By.XPATH, "//input[@type='checkbox']")))
        logging.info("Checkboxes are present.")
    except Exception as e:
        logging.error(f"Exception waiting for checkboxes to be present: {e}")
        return None

    # Wait for checkboxes to be visible
    try:
        wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//input[@type='checkbox']")))
        logging.info("Checkboxes are visible.")
    except Exception as e:
        logging.error(f"Exception waiting for checkboxes to be visible: {e}")
        return None

    # Print available checkbox values to debug
    checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
    for checkbox in checkboxes:
        logging.info(f"Checkbox value: {checkbox.get_attribute('value')}")

    # Select specific event types
    event_types = [
        "All Events", "Astronomical Low Tide", "Avalanche", "Blizzard", "Coastal Flood", "Cold/Wind Chill", 
        "Debris Flow", "Dense Fog", "Dense Smoke", "Drought", "Dust Devil", "Dust Storm", "Excessive Heat", 
        "Extreme Cold/Wind Chill", "Flash Flood", "Flood", "Freezing Fog", "Frost/Freeze", "Funnel Cloud", "Hail", 
        "Heat", "Heavy Rain", "Heavy Snow", "High Surf", "High Wind", "Hurricane (Typhoon)", "Ice Storm", 
        "Lake-Effect Snow", "Lakeshore Flood", "Lightning", "Marine Hail", "Marine High Wind", "Marine Strong Wind", 
        "Marine Thunderstorm Wind", "Rip Current", "Seiche", "Sleet", "Sneakerwave", "Storm Surge/Tide", "Strong Wind", 
        "Thunderstorm Wind", "Tornado", "Tropical Depression", "Tropical Storm", "Tsunami", "Volcanic Ash", "Waterspout", 
        "Wildfire", "Winter Storm", "Winter Weather"
    ]
    for event in event_types:
        try:
            checkbox = driver.find_element(By.XPATH, f"//input[@type='checkbox' and @value='{event}']")
            checkbox.click()
            logging.info(f"Selected checkbox for event '{event}'.")
        except Exception as e:
            logging.error(f"Exception selecting checkbox for event '{event}': {e}")

    driver.find_element(By.NAME, "startDate").clear()
    driver.find_element(By.NAME, "startDate").send_keys("07/01/2023")
    logging.info("Begin date set.")

    driver.find_element(By.NAME, "endDate").clear()
    driver.find_element(By.NAME, "endDate").send_keys("07/31/2024")
    logging.info("End date set.")

    time.sleep(5)
    
    try:
        pass
    finally:
        driver.quit()

    return download_directory

# Function to process the downloaded CSV file and visualize data
def process_and_visualize_csv(download_directory):
    csv_file = [f for f in os.listdir(download_directory) if f.endswith('.csv')][0]
    csv_path = os.path.join(download_directory, csv_file)
    
    df = pd.read_csv(csv_path)
    print(df.head())
    
    import matplotlib.pyplot as plt

    df['EVENT_TYPE'].value_counts().plot(kind='bar', figsize=(12, 6))
    plt.title('Number of Each Event Type')
    plt.xlabel('Event Type')
    plt.ylabel('Count')
    plt.xticks(rotation=90)
    plt.show()

def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        download_directory = fetch_csv_url(driver)
    finally:
        driver.quit()
    
    process_and_visualize_csv(download_directory)

if __name__ == "__main__":
    main()

