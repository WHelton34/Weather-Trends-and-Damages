from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Navigate to NOAA Storm Events Database form
driver.get("https://www.ncdc.noaa.gov/stormevents/choosedates.jsp?statefips=-999%2CALL")

# Increase the implicit wait time
driver.implicitly_wait(30)  # Adjust this value as needed

# Wait for the dropdown to be available
wait = WebDriverWait(driver, 60)  # Increase the explicit wait time
state_select_element = wait.until(EC.presence_of_element_located((By.NAME, "statefips")))

# Select "All States and Areas"
state_select = Select(state_select_element)
try:
    state_select.select_by_value("-999,ALL")
except Exception as e:
    print(f"Exception: {e}")

# Wait for checkboxes to be visible
wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//input[@type='checkbox']")))

# Print available checkbox values to debug
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
for checkbox in checkboxes:
    print(f"Checkbox value: {checkbox.get_attribute('value')}")

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
    except Exception as e:
        print(f"Exception selecting checkbox for event '{event}': {e}")

# Input Begin Date
driver.find_element(By.NAME, "startDate").clear()
driver.find_element(By.NAME, "startDate").send_keys("07/01/2023")

# Input End Date
driver.find_element(By.NAME, "endDate").clear()
driver.find_element(By.NAME, "endDate").send_keys("07/31/2024")

# Wait for a few seconds to see the result
time.sleep(5)

# Close the WebDriver
driver.quit()
