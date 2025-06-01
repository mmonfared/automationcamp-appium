from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from helper import desired_caps
from time import *


appium_server = "http://127.0.0.1:4723"

# =================================================================================
# 1- Read SMS:
# =================================================================================

appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
sms_inbox = driver.execute_script("mobile: listSms")
print(sms_inbox)
sms = sms_inbox['items'][0]['body'] # Welcome to our team!

# =================================================================================
# 2- SMS Validation:
# =================================================================================
# User/Pass : admin/admin
# Default OTP: 568812
# driver.send_sms('<phone>', 'message')

# ===================
# Helper Functions
# ===================

def get_sms_inbox(driver_instance):
    return driver_instance.execute_script("mobile: listSms")

def get_last_sms_body(sms_list):
    return sms_list['items'][0]['body']

def get_last_sms_time(sms_list):
    last_sms_time_full =  sms_list['items'][0]['date'] # 1748204257534
    last_sms_time = int(last_sms_time_full[:10])
    print("Last sms time:", last_sms_time)
    return last_sms_time

def get_device_time(driver_instance):
    device_time =  driver_instance.get_device_time() #  2025-05-31T12:59:27-04:00
    time_object = strptime(device_time, "%Y-%m-%dT%H:%M:%S%z")
    time_epoch = mktime(time_object)
    print("Device time:", int(time_epoch))
    return int(time_epoch)

def wait_for_new_sms(driver_instance):
    current_time = get_device_time(driver_instance)
    for i in range(15):
        sms_inbox = get_sms_inbox(driver_instance)
        last_sms_time = get_last_sms_time(sms_inbox)
        if last_sms_time > current_time:
            print("New SMS received!")
            return get_last_sms_body(sms_inbox)
        else:
            print("Waiting for new SMS..." + str(15-i) + ' seconds...')
            sleep(1)
            i -= 1
    raise Exception("No new SMS received in 15 seconds")

appium_options = UiAutomator2Options().load_capabilities(desired_caps.otp_app)
driver = webdriver.Remote(appium_server, options=appium_options)

# Login Page
username_field = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().className("android.widget.EditText").instance(0)')
password_field = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().className("android.widget.EditText").instance(1)')
login_button = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button')
sleep(0.5)
username_field.send_keys("admin")
password_field.send_keys("admin")
sleep(0.5)
login_button.click()

# Simulating receiving OTP
sleep(2)
driver.send_sms('100012', 'AutomationCamp OTP Code: 568812')

### Read SMS

# sleep(5)
# sms_inbox = driver.execute_script("mobile: listSms")
# last_sms_body = sms_inbox['items'][0]['body']

last_sms_body = wait_for_new_sms(driver)
otp_code = last_sms_body.replace('AutomationCamp OTP Code: ', '')

# OTP page
sleep(0.5)
driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Enter OTP"]')
driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText').send_keys(otp_code)
verify_otp = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("Verify OTP")')
verify_otp.click()
driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Welcome to AutomationCamp!"]')






