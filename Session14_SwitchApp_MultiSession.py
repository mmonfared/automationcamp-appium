from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from helper import desired_caps
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


appium_server = "http://127.0.0.1:4723"

# =================================================================================
# 1. Activate App
appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)

# Open APIDemos
driver = webdriver.Remote(appium_server, options=appium_options)
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Views')))

# Open WDIO
driver.activate_app(desired_caps.wdio['appium:appPackage'])
wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Drag')))

# Switch to APIDemos
driver.activate_app('io.appium.android.apis')
wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Views')))

driver.quit()

# =================================================================================
# 2. Start Session

appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)

# Open APIDemos
driver = webdriver.Remote(appium_server, options=appium_options)
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Views')))

# Open WDIO
driver.start_session(desired_caps.wdio)
wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Drag')))

# Switch to APIDemos
driver.start_session(desired_caps.apidemos)
wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Views')))

driver.quit()
# =================================================================================
# 3. 2 driver instances

caps1 = {
    "platformName": "Android",
    "appium:options": {
        "appPackage": "io.appium.android.apis",
        "appActivity": ".ApiDemos",
        "automationName": "UiAutomator2",
        "udid": "emulator-5554",
        "systemPort": "8201"
    }
}
caps2 = {
    "appium:appPackage": "com.wdiodemoapp",
    "appium:appActivity": ".MainActivity",
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "appium:udid": "emulator-5556",
    "appium:systemPort": "8202"
}

# Open APIDemos
appium_options1 = UiAutomator2Options().load_capabilities(caps1)
driver1 = webdriver.Remote(appium_server, options=appium_options1)
wait1 = WebDriverWait(driver1, 10)
wait1.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Views')))

# Open WDIO
appium_options2 = UiAutomator2Options().load_capabilities(caps2)
driver2 = webdriver.Remote(appium_server, options=appium_options2)
wait2 = WebDriverWait(driver2, 10)
wait2.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Drag')))

# Switch between apps
driver1.find_element(AppiumBy.ACCESSIBILITY_ID, 'Views').click() #APIDemos
driver2.find_element(AppiumBy.ACCESSIBILITY_ID, 'Drag').click() #WDIO 

