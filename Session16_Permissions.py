from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.wait import WebDriverWait
from helper import desired_caps
from selenium.webdriver.support import expected_conditions as EC
from time import *

# ============================================================
# List of Common Android Permissions
# ============================================================
# Reference: https://developer.android.com/reference/android/Manifest.permission

# android.permission.CAMERA
# android.permission.ACCESS_FINE_LOCATION
# android.permission.ACCESS_COARSE_LOCATION
# android.permission.ACCESS_BACKGROUND_LOCATION
# android.permission.READ_CONTACTS
# android.permission.CALL_PHONE
# android.permission.READ_PHONE_STATE
# android.permission.SEND_SMS
# android.permission.RECEIVE_SMS
# android.permission.READ_SMS
# android.permission.RECORD_AUDIO
# android.permission.READ_CALENDAR
# android.permission.WRITE_CALENDAR
# android.permission.BODY_SENSORS
# android.permission.BLUETOOTH_CONNECT
# android.permission.BLUETOOTH_SCAN
# android.permission.POST_NOTIFICATIONS
# android.permission.NEARBY_WIFI_DEVICES

# =============================================================
# Clear app:
# adb shell pm clear ir.automationcamp.permissions
# =============================================================
# How to grant Permissions:

# 1. adb shell pm grant <PACKAGE_NAME> <PERMISSION_NAME>
#    adb shell pm grant ir.automationcamp.permissions android.permission.CAMERA
# 2. driver.execute_script('mobile: shell', {
#   'command': 'pm',
#   'args': ['grant', '<PACKAGE_NAME>', '<PERMISSION_NAME>']
#   })
# > NOTE: appium --allow-insecure=adb_shell  OR  appium --relaxed-security
# 3. Add "autoGrantPermissions": True" to desired capabilities
# =============================================================
# How to revoke Permissions (not system granted):

# 1. adb shell pm revoke <PACKAGE_NAME> <PERMISSION_NAME>
#    adb shell pm revoke ir.automationcamp.permissions android.permission.CAMERA
# 2. driver.execute_script('mobile: shell', {
#   'command': 'pm',
#   'args': ['revoke', '<PACKAGE_NAME>', '<PERMISSION_NAME>']
#   })
# =============================================================
# List down all permissions

# adb shell dumpsys package <PACKAGE_NAME> | grep permission
# adb shell dumpsys package ir.automationcamp.permissions | grep permission

# =============================================================
# Locators
# =============================================================
# App Locators
camera_button = "ir.automationcamp.permissions:id/buttonCamera"
location_fine_button = "ir.automationcamp.permissions:id/buttonLocationFine"
location_course_button = "ir.automationcamp.permissions:id/buttonLocationCoarse"
contacts_button = "ir.automationcamp.permissions:id/buttonContacts"
microphone_button = "ir.automationcamp.permissions:id/buttonMicrophone"
bluetooth_button = "ir.automationcamp.permissions:id/buttonBluetooth"

# Android Locators
grant_dilog = "com.android.permissioncontroller:id/grant_dialog"
while_using_the_app = "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
permission_allow_button = "com.android.permissioncontroller:id/permission_allow_button"
camera_permission_granted = '//android.widget.Toast[@text="Permission Camera is granted"]'
app_already_has_camera_permission = '//*[@text="App already has access to Camera"]'
app_already_has_location_fine_permission = '//*[@text="App already has access to Location (fine)"]'
app_already_has_microphone_permission = '//*[@text="App already has access to Microphone"]'

# # =============================================================
# # Configurations
# # =============================================================
appium_server = "http://127.0.0.1:4723"
appium_options = UiAutomator2Options().load_capabilities(desired_caps.permissions_app)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)
#
# # =============================================================
# # Grant Programmatically
# # =============================================================
driver.execute_script('mobile: shell', {
  'command': 'pm',
  'args': ['grant', 'ir.automationcamp.permissions', 'android.permission.CAMERA']
  })

driver.find_element(by=AppiumBy.ID, value=camera_button).click()
wait.until(EC.presence_of_element_located((AppiumBy.XPATH, app_already_has_camera_permission)))
#
# # =============================================================
# # Revoke Programmatically
# # =============================================================
driver.execute_script('mobile: shell', {
  'command': 'pm',
  'args': ['revoke', 'ir.automationcamp.permissions', 'android.permission.CAMERA']
  })
driver.activate_app('ir.automationcamp.permissions') # App get reset after revoke
driver.find_element(by=AppiumBy.ID, value=camera_button).click()
wait.until(EC.presence_of_element_located((AppiumBy.ID, while_using_the_app)))

# =============================================================
# AutoGrantAll
# =============================================================
appium_server = "http://127.0.0.1:4723"
# Add "autoGrantPermissions": True" to desired capabilities

caps = desired_caps.permissions_app
caps["autoGrantPermissions"] = True
appium_options = UiAutomator2Options().load_capabilities(caps)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)

driver.find_element(by=AppiumBy.ID, value=camera_button).click()
wait.until(EC.presence_of_element_located((AppiumBy.XPATH, app_already_has_camera_permission)))

driver.find_element(by=AppiumBy.ID, value=location_fine_button).click()
wait.until(EC.presence_of_element_located((AppiumBy.XPATH, app_already_has_location_fine_permission)))

driver.find_element(by=AppiumBy.ID, value=microphone_button).click()
wait.until(EC.presence_of_element_located((AppiumBy.XPATH, app_already_has_microphone_permission)))
