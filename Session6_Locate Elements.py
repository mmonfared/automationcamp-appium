from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from time import sleep

desired_caps = {
  "appium:appPackage": "io.appium.android.apis",
  "appium:appActivity": "io.appium.android.apis.ApiDemos",
  "platformName": "Android",
  "appium:automationName": "UiAutomator2"
}

appium_server = "http://127.0.0.1:4723"
appium_options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote(appium_server, options=appium_options)

#1: ACCESSIBILITY_ID
el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Accessibility')
print('BY ACCESSIBILITY_ID: ', el1)

#2: ID
el2 = driver.find_element(by=AppiumBy.ID, value='android:id/text1') #First found element
print('BY ID:', el2.get_attribute('text'))

#3: CLASS_NAME
el3 = driver.find_elements(by=AppiumBy.CLASS_NAME, value='android.widget.TextView')
print(el3[2].get_attribute('text'))

#4: XPATH (attribute):
el4 = driver.find_element(by=AppiumBy.XPATH, value='//*[@content-desc="Accessibility"]')
print('BY XPATH (attribute):', el4.get_attribute('text'))

#5: XPATH (text)
el5 = driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Accessibility"]')
print('BY XPATH (text):', el5.get_attribute('text'))

#6: CSS_SELECTOR
el6 = driver.find_element(by=AppiumBy.CSS_SELECTOR, value='#android\\:id\\/text1:nth-child(1)')
print('BY CSS_SELECTOR:', el6.get_attribute('text'))

#7: ANDROID_UIAUTOMATOR
el7 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("Accessibility")')
print('BY ANDROID_UIAUTOMATOR:', el7.get_attribute('text'))