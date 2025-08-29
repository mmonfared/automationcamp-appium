from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.wait import WebDriverWait
from helper import desired_caps
from time import *

# ============================================================
# List of Common Android Permissions
# ============================================================
# 1. Give permission > Session 16
# 2. driver.toggle_location_services() # Toggle location
# 3. current_location = driver.location # Get current location
# 4. driver.set_location(lat, lon)


appium_server = "http://127.0.0.1:4723"
appium_options = UiAutomator2Options().load_capabilities(desired_caps.maps)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.implicitly_wait(5)
driver.find_element(by=AppiumBy.XPATH, value="//*[@text='SKIP']").click()

# driver.toggle_location_services()

current_location = driver.location
print("Current Location: ", current_location)

driver.find_element(AppiumBy.ID, 'com.google.android.apps.maps:id/mylocation_button').click()

driver.set_location(29.935754, 52.889680)

driver.find_element(AppiumBy.ID, 'com.google.android.apps.maps:id/mylocation_button').click()

sleep(3)

new_location = driver.location
print("New Location: ", new_location)



