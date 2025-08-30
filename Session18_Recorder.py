from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.wait import WebDriverWait
from helper import desired_caps
from time import *

appium_server = "http://127.0.0.1:4723"
appium_options = UiAutomator2Options().load_capabilities(desired_caps.contacts2)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.implicitly_wait(5)

el1 = driver.find_element(by=AppiumBy.ID, value="android:id/button2")
el1.click()
el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Create contact")
el2.click()
el3 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"First name\")")
el3.send_keys("Alex")
el4 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Last name\")")
el4.send_keys("Jacob")
el5 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Phone\")")
el5.send_keys("+18881546567")
el6 = driver.find_element(by=AppiumBy.ID, value="com.google.android.contacts:id/toolbar_button")
el6.click()


