from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
import os
from time import sleep
from helper import desired_caps

cred = {'email': 'monfareddm@yahoo.com ', 'pass': 'test1234'}
appium_server = "http://127.0.0.1:4723"

# =================================================================================
# Install app by appium:
# "appium:app": <APK_PATH> desired capability
# =================================================================================
# Actions: 1.Stop app 2. Clear app data 3. Uninstall & Install app  - (in the beginning )
# =================================================================================
# Required appium:app (APK file):
#   "fullReset": True or False

# =================================================================================
# 1- Combinations:
# =================================================================================
### Fast Reset: Stop: YES / Clear data: YES / Reinstall: NO
# 1. ["noReset": False]
# 2. ["fullReset": False]
# 3. ["noReset": False, "fullReset: False"]
# 4. desired_caps not include ["noReset"] or ["fullReset"]
###
# 5. ["noReset": True] - Stop app: NO / Clear app data: NO / Reinstall: NO
# 6. ["fullReset": True] - Stop: YES / Clear data: YES / Reinstall: YES
# 7. ["noReset": True, "fullReset": False] = ["noReset": True]
# 8. ["noReset": False, "fullReset": True] = ["fullReset": True]
# 9. ["noReset": True, "fullReset: True"] - Error: The 'noReset' and 'fullReset' capabilities are mutually exclusive and should not both be set to true. You probably meant to just use 'fullReset' on its own

caps = {
    "appium:appPackage": "me.clockify.android",
    "appium:appActivity": ".presenter.screens.main.MainActivity",
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "noReset": True,
    # "appium:app": os.path.abspath(os.path.join(os.path.dirname(__file__), 'APK', 'clockify.apk')),
    # "fullReset": True,
}

appium_options = UiAutomator2Options().load_capabilities(caps)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.implicitly_wait(5)
driver.find_element(AppiumBy.XPATH, '//*[@resource-id="loginTypeSwitchOutlinedButton"]').click()
driver.find_element(AppiumBy.XPATH, '//*[@resource-id="emailEditText"]').send_keys(cred['email'])
driver.find_element(AppiumBy.XPATH, '//*[@resource-id="passwordEditText"]').send_keys(cred['pass'])
driver.find_element(AppiumBy.XPATH, '//*[@resource-id="loginButtonButton"]').click()
driver.find_element(AppiumBy.XPATH, '//*[@text="Time Tracker"]')

# =================================================================================
# 2- Store Cache in Chrome Browser:

caps = {
    "appium:appPackage": "com.android.chrome",
    "appium:appActivity": "com.google.android.apps.chrome.Main",
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "noReset": True
}

appium_options = UiAutomator2Options().load_capabilities(caps)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.get("https://app.clockify.me")
driver.switch_to.context('WEBVIEW_chrome')
driver.implicitly_wait(20)
driver.find_element(AppiumBy.XPATH, '//*[@data-test-id="login-manual"]').click()
driver.find_element(AppiumBy.CSS_SELECTOR, '#email').send_keys(cred['email'])
driver.find_element(AppiumBy.CSS_SELECTOR, '#password').click()
# driver.find_element(AppiumBy.CSS_SELECTOR, '#password').send_keys(cred['pass'])
driver.execute_script('mobile: type', {'text': cred['pass']})
driver.find_element(AppiumBy.XPATH, '//*[@data-test-id="login-button"]').click()
driver.find_element(AppiumBy.XPATH, '//*[text()="This week"]')
sleep(3)

# =================================================================================
# 3- mobile: clearApp

caps = {
    "appium:appPackage": "me.clockify.android",
    "appium:appActivity": ".presenter.screens.main.MainActivity",
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "noReset": True,
}

appium_options = UiAutomator2Options().load_capabilities(caps)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.implicitly_wait(5)
driver.find_element(AppiumBy.XPATH, '//*[@text="Time Tracker"]')
sleep(0.5)
driver.execute_script("mobile: clearApp", {'appId': 'me.clockify.android'})
sleep(0.5)
driver.activate_app("me.clockify.android")
driver.find_element(AppiumBy.XPATH, '//*[@resource-id="loginTypeSwitchOutlinedButton"]').click()
driver.find_element(AppiumBy.XPATH, '//*[@resource-id="emailEditText"]').send_keys(cred['email'])
driver.find_element(AppiumBy.XPATH, '//*[@resource-id="passwordEditText"]').send_keys(cred['pass'])
driver.find_element(AppiumBy.XPATH, '//*[@resource-id="loginButtonButton"]').click()
driver.find_element(AppiumBy.XPATH, '//*[@text="Time Tracker"]')

# =================================================================================
# 4- Questions
# - When to use noReset, fullReset and fastReset?
# - How to open chrome without cache?
# - Should I reset the app in teardown stage?

