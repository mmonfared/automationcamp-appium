from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from time import sleep

# How to set chrome driver binary in appium? 
# method 1: `appium server --allow-insecure chromedriver_autodownload`
# method 2: Copy driver binary manually to:
# /USER_HOME/.appium/node_modules/appium-uiautomator2-driver/node_modules/appium-chromedriver/chromedriver/win
# method 3: add "chromedriverExecutable": "<DRIVER_PATH>" to desired caps appium options

desired_caps = {
    "platformName": "Android",
    "browserName": "Chrome",
    "appium:options": {
        "automationName": "UiAutomator2",
        # "chromedriverExecutable": "C:/chromedriver.exe"
    }
}
appium_server = "http://127.0.0.1:4723"
appium_options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.get("https://play1.automationcamp.ir/forms.html")
driver.find_element(by=AppiumBy.CSS_SELECTOR, value="#notes").send_keys("AutomationCamp")
