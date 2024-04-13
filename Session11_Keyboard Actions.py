from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from time import sleep

from helper import desired_caps

appium_server = "http://127.0.0.1:4723"

# =================================================================================
# https://developer.android.com/reference/android/view/KeyEvent
# Back: 4 | Home: 3 | App_Switch: 187 | Search: 84 | Enter: 66 |  Tab: 61
# 'H': 36 | 'E': 33 | 'L': 40 | 'O': 43 |
# driver.keyevent()
# driver.press_keycode()
# driver.hide_keyboard()
# driver.is_keyboard_shown()
# driver.long_press_keycode()

# =================================================================================
# Set Text (Send Keys)
appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Views').click()
list_view = driver.find_element(by=AppiumBy.ID, value='android:id/list')
driver.execute_script('mobile: swipeGesture', {
    'elementId': list_view,
    'direction': 'up',
    'percent': 1.0,
})
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'TextFields').click()
driver.find_element(AppiumBy.ID, 'io.appium.android.apis:id/edit').send_keys("Hello")

sleep(1) # For demo purpose
driver.quit()

# =================================================================================
# Real Type 1 - Key Event
appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Views').click()
list_view = driver.find_element(by=AppiumBy.ID, value='android:id/list')
driver.execute_script('mobile: swipeGesture', {
    'elementId': list_view,
    'direction': 'up',
    'percent': 1.0,
})
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'TextFields').click()
driver.find_element(AppiumBy.ID, 'io.appium.android.apis:id/edit').click()
driver.press_keycode(36) # H
# or
# driver.keyevent(36)
driver.press_keycode(33) # E
driver.press_keycode(40) # L
driver.press_keycode(40) # L
driver.press_keycode(43) # O
sleep(0.2) # For demo purpose
driver.press_keycode(67) # Backspace
sleep(0.2) # For demo purpose
driver.long_press_keycode(67) # Hold Backspace

sleep(1) # For demo purpose
driver.quit()

# =================================================================================
# Device Keys
appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Views').click()
driver.press_keycode(187) # App_Switch
# or
# driver.keyevent(187)
sleep(0.2)
driver.press_keycode(4) # Back
sleep(0.2)
driver.press_keycode(3) # Home

sleep(1) # For demo purpose
driver.quit()

# =================================================================================
# Control keyboard
appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Views').click()
list_view = driver.find_element(by=AppiumBy.ID, value='android:id/list')
driver.execute_script('mobile: swipeGesture', {
    'elementId': list_view,
    'direction': 'up',
    'percent': 1.0,
})
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'TextFields').click()
driver.find_element(AppiumBy.ID, 'io.appium.android.apis:id/edit').click()

check = driver.is_keyboard_shown()
print(check)

driver.hide_keyboard()

check = driver.is_keyboard_shown()
print(check)

sleep(1) # For demo purpose
driver.quit()

# =================================================================================
# Real Type 2 - execute 'mobile: type'
appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Views').click()
list_view = driver.find_element(by=AppiumBy.ID, value='android:id/list')
driver.execute_script('mobile: swipeGesture', {
    'elementId': list_view,
    'direction': 'up',
    'percent': 1.0,
})
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'TextFields').click()
# driver.find_element(AppiumBy.ID, 'io.appium.android.apis:id/edit').click() # Focus on element
driver.execute_script('mobile: type', {'text': 'Hello World'})
sleep(0.2) # For demo purpose

sleep(1) # For demo purpose
driver.quit()

# =================================================================================
#  Input Method Editor (IME) Generation
# # https://appium.readthedocs.io/en/latest/en/writing-running-appium/android/android-ime/
appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Views').click()
list_view = driver.find_element(by=AppiumBy.ID, value='android:id/list')
driver.execute_script('mobile: swipeGesture', {
    'elementId': list_view,
    'direction': 'up',
    'percent': 1.0,
})
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'TextFields').click()
driver.execute_script('mobile: type', {'text': 'Hello'})
sleep(0.2) # For demo purpose
driver.execute_script('mobile: performEditorAction', {'action': 'next'}) # IME Action
sleep(0.2) # For demo purpose
driver.execute_script('mobile: type', {'text': 'World'})
sleep(0.2) # For demo purpose

sleep(1) # For demo purpose
driver.quit()

# =================================================================================
#  Search
appium_options = UiAutomator2Options().load_capabilities(desired_caps.amazon)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.implicitly_wait(5)
driver.find_element(AppiumBy.ID, 'com.amazon.mShop.android.shopping:id/skip_sign_in_button').click()
driver.find_element(AppiumBy.ID, 'com.amazon.mShop.android.shopping:id/chrome_search_hint_view').click()
search_field = driver.find_element(AppiumBy.ID, 'com.amazon.mShop.android.shopping:id/rs_search_src_text')

search_field.send_keys('iPhone')

# Using IME
driver.execute_script('mobile: performEditorAction', {'action': 'search'})

sleep(1) # For demo purpose
driver.quit()



