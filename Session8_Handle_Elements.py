from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from time import sleep
from helper import desired_caps

appium_server = "http://127.0.0.1:4723"


# =================================================================================
# 1. TextBox 2. Checkbox 3. Radio 4. Switches
appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Views').click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Controls').click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='1. Light Theme').click()
# TextBox
driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText").send_keys("Appium")
sleep(1)
driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText").clear()
# Checkbox
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Checkbox 1').click()
# Radio
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'RadioButton 1').click()
# Switches > Views > Switches

driver.quit()

# =================================================================================
# 5. Drop Down
appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Views').click()
list_view = driver.find_element(by=AppiumBy.ID, value='android:id/list')
driver.execute_script('mobile: swipeGesture', {
    'elementId': list_view,
    'direction': 'up',
    'percent': 1.0,
})
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Spinner').click()
driver.find_element(AppiumBy.ID, 'io.appium.android.apis:id/spinner1').click()
driver.find_element(AppiumBy.XPATH, '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="green"]').click()
# Use XPath
el1_xpath = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="io.appium.android.apis:id/spinner1"]//*[@resource-id="android:id/text1"]')
# Use CSS
el1_css = driver.find_element(AppiumBy.CSS_SELECTOR, '[resource-id="io.appium.android.apis:id/spinner1"]>[resource-id="android:id/text1"]')
# Query on parent
el1 = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="io.appium.android.apis:id/spinner1"]').find_element(AppiumBy.XPATH, '//*[@resource-id="android:id/text1"]')
print(el1_xpath)
print(el1_css)
print(el1)
assert el1.get_attribute('text') == 'green'
sleep(3)
driver.quit()

# =================================================================================
# 6. Drop Down - Scrollable Options list
appium_options = UiAutomator2Options().load_capabilities(desired_caps.contacts)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.implicitly_wait(5)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Create new contact").click()
driver.find_element(AppiumBy.ID, 'com.android.contacts:id/left_button').click()
driver.hide_keyboard()
driver.find_element(AppiumBy.XPATH, '//android.widget.Spinner[@content-desc="Phone"]').click()
list_view = driver.find_element(AppiumBy.CLASS_NAME, 'android.widget.ListView')
driver.execute_script('mobile: swipeGesture', {
    'elementId': list_view,
    'direction': 'up',
    'percent': 1.0,
})
driver.find_element(AppiumBy.XPATH, '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Telex"]').click()

sleep(3)
driver.quit()

# =================================================================================
# 7. Wheeler (Picker)
appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Views').click()
list_view = driver.find_element(AppiumBy.CLASS_NAME, 'android.widget.ListView')
driver.execute_script('mobile: scrollGesture', {
    'elementId': list_view,
    'direction': 'down',
    'percent': 1.0,
})
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Picker').click()
picker_el = driver.find_element(AppiumBy.ID, 'android:id/numberpicker_input')
up_el = driver.find_element(AppiumBy.XPATH,'//*[@resource-id="android:id/numberpicker_input"]/preceding-sibling::*[@class="android.widget.Button"]')
while picker_el.text != 'kupima':
    # Method 1 - W3C Mobile Gestures Commands
    # driver.execute_script('mobile: scrollGesture', {
    #     'elementId': picker_el,
    #     'direction': 'down',
    #     'percent': 1.0,
    #     'speed': 1000
    # })

    # Method 2 - W3C Action Helpers
    driver.scroll(picker_el, up_el)

    picker_el = driver.find_element(AppiumBy.ID, 'android:id/numberpicker_input')

text_el = driver.find_element(AppiumBy.ID, 'io.appium.android.apis:id/textView1').get_attribute('text')
assert text_el == "Value: kupima"

sleep(2)
driver.quit()

# =================================================================================
# 8. Date/Time Picker - Spinner
appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.implicitly_wait(10)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Views').click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Date Widgets').click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, '1. Dialog').click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'change the time (spinner)').click()
pickers = driver.find_elements(AppiumBy.ID, 'android:id/numberpicker_input')

# Not working
# pickers[0].send_keys('7')
# pickers[1].send_keys('30')
# pickers[2].send_keys('PM')

pickers[0].click()
driver.execute_script('mobile: type', {'text': '7'})
pickers[1].click()
driver.execute_script('mobile: type', {'text': '30'})
pickers[2].click()
driver.execute_script('mobile: type', {'text': 'PM'})

driver.quit()

# =================================================================================
# 9. Date/Time Picker - Calendar
from datetime import datetime

def get_selected_date(_driver):
    selected_date_desc = _driver.find_element(AppiumBy.CSS_SELECTOR,'[resource-id="android:id/month_view"] > .android.view.View:checked').get_attribute('content-desc')
    return datetime.strptime(selected_date_desc, "%d %B %Y")

def get_all_dates_of_current_month(_driver):
    date_objects = []
    date_elements = _driver.find_element(AppiumBy.ID, 'android:id/month_view').find_elements(AppiumBy.CLASS_NAME, 'android.view.View')
    for day in date_elements:
        date_string = day.get_attribute('content-desc')
        if date_string == 'null':
            continue
        date_objects.append(datetime.strptime(date_string, "%d %B %Y"))
    return date_objects

def change_month_view(_driver, direction):
    """
    Change Current Month View
    :param _driver: driver instance
    :param direction: "previous" or "next"
    """
    if direction not in ['previous', 'next']:
        raise ValueError("Invalid direction. Should be either 'previous' or 'next'.")
    element_id = 'android:id/prev' if direction == "previous" else 'android:id/next'
    _driver.find_element(AppiumBy.ID, element_id).click()

def set_target_date(_driver, target):
    """
    :param _driver: Driver Instance
    :param target: target date in format "%d %B %Y". e.g.: "07 March 2024"
    """
    all_dates = get_all_dates_of_current_month(_driver)
    target_date_obj = datetime.strptime(target, "%d %B %Y")

    if target_date_obj in all_dates:
        target_date_str = target_date_obj.strftime("%d %B %Y")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, target_date_str).click()
        return

    while target_date_obj not in all_dates:
        if target_date_obj > all_dates[-1]:
            change_month_view(_driver, 'next')
        elif target_date_obj < all_dates[0]:
            change_month_view(_driver, 'previous')
        all_dates = get_all_dates_of_current_month(_driver)

    set_target_date(_driver, target)

appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.implicitly_wait(10)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Views').click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Date Widgets').click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, '1. Dialog').click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'change the date').click()

# set_target_date(driver, "10 January 2025")
set_target_date(driver, "20 July 2023")

sleep(5)
driver.quit()

# =================================================================================
# 10. Slider - Rating Bar
appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.implicitly_wait(10)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Views').click()
list_view = driver.find_element(AppiumBy.CLASS_NAME, 'android.widget.ListView')
driver.execute_script('mobile: scrollGesture', {
    'elementId': list_view,
    'direction': 'down',
    'percent': 1.0,
})
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Rating Bar').click()
rating_element = driver.find_element(AppiumBy.ID, 'io.appium.android.apis:id/ratingbar2')
driver.execute_script('mobile: scrollGesture', {
    'elementId': rating_element,
    'direction': 'left',
    'percent': 3.5/5,
})

rating_text = driver.find_element(AppiumBy.ID, 'io.appium.android.apis:id/rating').text
assert rating_text == "Rating: 4.0/5"

sleep(3)
driver.quit()

# =================================================================================
# 11. Slider - Seek Bar
appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.implicitly_wait(10)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Views').click()
list_view = driver.find_element(AppiumBy.CLASS_NAME, 'android.widget.ListView')
driver.execute_script('mobile: swipeGesture', {
    'elementId': list_view,
    'direction': 'up',
    'percent': 1.0,
})
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Seek Bar').click()
bar_element = driver.find_element(AppiumBy.ID, 'io.appium.android.apis:id/seek')
driver.execute_script('mobile: scrollGesture', {
    'elementId': bar_element,
    'direction': 'left',
    'percent': 0.4,
})

bar_value = driver.find_element(AppiumBy.ID, 'io.appium.android.apis:id/progress').text
print(bar_value)

sleep(3)
driver.quit()

# =================================================================================
# 12. Popups
appium_options = UiAutomator2Options().load_capabilities(desired_caps.contacts)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.implicitly_wait(5)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Create new contact").click()
driver.find_element(AppiumBy.ID, 'com.android.contacts:id/left_button').click()
driver.hide_keyboard()
coords = driver.find_element(AppiumBy.XPATH, '//*[@text="Create new contact"]').location

driver.find_element(AppiumBy.XPATH, '//android.widget.Spinner[@content-desc="Phone"]').click()
sleep(1)
driver.tap([(coords['x'], coords['y'])])  # Close popup
driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="Email"]').send_keys("test@gmail.com")

# sleep(3)
driver.quit()

# =================================================================================
# 13. Alerts
from selenium.webdriver.common.alert import Alert
appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.implicitly_wait(5)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'App').click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Alert Dialogs').click()
driver.find_element(AppiumBy.ID, 'io.appium.android.apis:id/two_buttons').click()

# Get text
alert_text = Alert(driver).text
alert_text_alt = driver.switch_to.alert.text
print(alert_text)
print(alert_text_alt)
# Accept
driver.switch_to.alert.accept()

sleep(1)
driver.find_element(AppiumBy.ID, 'io.appium.android.apis:id/two_buttons').click()


# Dismiss
driver.switch_to.alert.dismiss()

driver.find_element(AppiumBy.ID, 'io.appium.android.apis:id/text_entry_button').click()
# Set text
# driver.switch_to.alert.send_keys('Something') # Works if there is only one input field

driver.find_element(AppiumBy.ID, 'io.appium.android.apis:id/username_edit').send_keys('AutomationCamp')
driver.find_element(AppiumBy.ID, 'io.appium.android.apis:id/password_edit').send_keys('123456')

sleep(2)
driver.quit()

# =================================================================================
# 14. Toast Message (Snackbar)

appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.implicitly_wait(3)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Views').click()
list_view = driver.find_element(AppiumBy.CLASS_NAME, 'android.widget.ListView')
driver.execute_script('mobile: swipeGesture', {
    'elementId': list_view,
    'direction': 'up',
    'percent': 1.0,
})
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Switches').click()
driver.find_element(AppiumBy.ID, 'io.appium.android.apis:id/monitored_switch').click()

# toast_message = driver.find_element(AppiumBy.CLASS_NAME, 'android.widget.Toast') # Not working - Toast message doesn't belong to current package
toast_message = driver.find_element(AppiumBy.XPATH, '//android.widget.Toast') # Working - XPath searches in the entire XML source
assert toast_message.text == 'Monitored switch is on'
sleep(2)
driver.quit()

# =================================================================================
# 15. Get app source (XML Hierarchy)

appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Views').click()
list_view = driver.find_element(AppiumBy.CLASS_NAME, 'android.widget.ListView')
driver.execute_script('mobile: swipeGesture', {
    'elementId': list_view,
    'direction': 'up',
    'percent': 1.0,
})
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Switches').click()
driver.find_element(AppiumBy.ID, 'io.appium.android.apis:id/monitored_switch').click()
page_source = driver.page_source
print(page_source)
assert 'android.widget.Toast' in page_source
assert 'Monitored switch is on' in page_source

sleep(2)
driver.quit()
