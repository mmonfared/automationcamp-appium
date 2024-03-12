from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from time import sleep

# adb shell dumpsys activity top | grep "ACTIVITY"

desired_caps = {
  "appium:appPackage": "com.android.deskclock",
  "appium:appActivity": "com.android.deskclock.DeskClock",
  "platformName": "Android",
  "appium:automationName": "UiAutomator2"
}

appium_server = "http://127.0.0.1:4723"
appium_options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote(appium_server, options=appium_options)
el = driver.find_element(by=AppiumBy.XPATH, value='//*[@text="ALARM"]')
el.click()
driver.find_element(AppiumBy.XPATH, value='(//android.widget.Switch[@resource-id="com.android.deskclock:id/onoff"])[1]').click()

print("Alarm set")
sleep(3)
driver.quit()