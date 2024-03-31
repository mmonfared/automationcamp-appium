from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from time import sleep
from helper import desired_caps
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


appium_server = "http://127.0.0.1:4723"

# =================================================================================
# Type of waits:
# - Pause
# - Implicitly
# - Explicitly
# - Fluent

# =================================================================================
# 1. Pause
print("Start")
sleep(2)
print("End after 2 seconds")

# =================================================================================
# 2. Implicitly Wait
appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)

driver.implicitly_wait(10)

driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'App').click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Loader').click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Throttle').click()
driver.find_element(AppiumBy.XPATH, '//*[@text="POPULATE"]').click()
driver.find_element(AppiumBy.XPATH, '//*[@resource-id="android:id/text1" and @text="Data A"]')

driver.quit()

# =================================================================================
# 3. Explicitly Wait - Visibility of Element
appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'App').click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Loader').click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Throttle').click()
driver.find_element(AppiumBy.XPATH, '//*[@text="POPULATE"]').click()

wait = WebDriverWait(driver, 10)
element = wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, '//*[@resource-id="android:id/text1" and @text="Data A"]')), "Data A cannot be found after 10 seconds")
print(element.text)

driver.quit()

# =================================================================================
# 4. Explicitly Wait - Invisibility of Element
appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'App').click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Loader').click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Throttle').click()
driver.find_element(AppiumBy.XPATH, '//*[@text="POPULATE"]').click()
sleep(1) # For demo purpose

wait = WebDriverWait(driver, 10)

# wait.until_not(EC.visibility_of_element_located((AppiumBy.XPATH, '//*[@resource-id="android:id/text1" and @text="Data Z"]')))

wait.until(EC.invisibility_of_element_located((AppiumBy.XPATH, '//*[@resource-id="android:id/text1" and @text="Data Z"]')))

driver.quit()
# =================================================================================
# 5. Explicitly Wait - Text/Value/Attribute to be present in element
appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'App').click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Loader').click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Throttle').click()
driver.find_element(AppiumBy.XPATH, '//*[@text="POPULATE"]').click()
sleep(1) # For demo purpose

wait = WebDriverWait(driver, 10)

wait.until(EC.text_to_be_present_in_element((AppiumBy.XPATH, '//(*[@resource-id="android:id/text1"])[1]'), 'Data A'))

driver.quit()








