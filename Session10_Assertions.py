from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from time import sleep
from helper import desired_caps
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

appium_server = "http://127.0.0.1:4723"

# =================================================================================
# 6. Get Attribute of Elements
# Supported attributes: [checkable, checked, {class,className}, clickable,
# {content-desc,contentDescription}, enabled, focusable, focused, {long-clickable,longClickable},
# package, password, {resource-id,resourceId}, scrollable, selection-start, selection-end, selected,
# {text,name}, hint, extras, bounds, displayed, contentSize]

appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Views').click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Controls').click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='1. Light Theme').click()
element = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Checkbox 1')
print(element.get_attribute('resource-id'))
print(element.get_attribute('class'))
print(element.get_attribute('content-desc'))
print(element.get_attribute('text'))
print(element.get_attribute('checked'))

driver.quit()

# =================================================================================
# 7. Assertions

appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Views').click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Controls').click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='1. Light Theme').click()
text_input = driver.find_element(by=AppiumBy.ID, value='io.appium.android.apis:id/edit')
checkbox1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Checkbox 1')
checkbox2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Checkbox 2')
radiobutton1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='RadioButton 1')
radiobutton2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='RadioButton 2')
toggle1 = driver.find_element(by=AppiumBy.ID, value='io.appium.android.apis:id/toggle1')
toggle2 = driver.find_element(by=AppiumBy.ID, value='io.appium.android.apis:id/toggle2')
save1 = driver.find_element(by=AppiumBy.ID, value='io.appium.android.apis:id/button')
save2 = driver.find_element(by=AppiumBy.ID, value='io.appium.android.apis:id/button_disabled')

text_input.send_keys("Hello")
assert text_input.get_attribute("text") == "Hello"

checkbox1.click()
radiobutton2.click()
toggle1.click()

assert checkbox1.get_attribute('checked') == 'true'
assert checkbox2.get_attribute('checked') == 'false'
assert radiobutton2.get_attribute('checked') == 'true'
assert toggle1.get_attribute('checked') == 'true'
# assert toggle2.get_attribute('checked') == 'true', "Toggle 2 is OFF" # Raise AssertionError
assert save1.is_enabled()
assert save2.is_enabled() == False

driver.find_element(AppiumBy.ID, 'io.appium.android.apis:id/spinner1').click()
element_earth = driver.find_element(AppiumBy.XPATH, '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Earth"]')
assert element_earth.is_displayed()

driver.quit()

# =================================================================================
# 8. While loop
appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'App').click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Loader').click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Throttle').click()
driver.find_element(AppiumBy.XPATH, '//*[@text="POPULATE"]').click()
sleep(1) # For demo purpose

# text = driver.find_element(AppiumBy.XPATH, '//(*[@resource-id="android:id/text1"])[1]').text
# while text != 'Data A':
#     sleep(0.2)
#     print(f"Current text is '{text}'")
#     text = driver.find_element(AppiumBy.XPATH, '//(*[@resource-id="android:id/text1"])[1]').text
# print(text)

def verify_element_text(locator: tuple, text: str, timeout: int = 5, element_find_timeout: int =5):
    """
    Waits for thr specified element to have  the given text within a timeout period
    :param locator: (tuple): Strategy and Locator pair of the element. (e.g. (AppiumBy.ID, 'elementID'))
    :param text: (str): The expected text of the element.
    :param timeout: (int) The maximum time to wait for the text in seconds. Default is 5
    :param element_find_timeout: (int) The maximum time to wait for the visibility of the element in seconds. Default is 5:
    :raise TimeoutError
    :return None
    """
    wait = WebDriverWait(driver, element_find_timeout)
    wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, '//(*[@resource-id="android:id/text1"])[1]')))

    counter = timeout * 5
    while counter > 0:
        try:
            element = driver.find_element(*locator)
            print(f"Current text is '{element.text}'")
            # For assertion keyword
            assert element.text == text
            return
            # For checking keyword
            # if element.text == text:
            #     return
        except AssertionError:
            sleep(0.2)
            counter -= 1
    raise TimeoutError(f'Element text was not {text} after {timeout} seconds ')

verify_element_text(locator=(AppiumBy.XPATH, '//(*[@resource-id="android:id/text1"])[1]'), text='Data A', timeout=10)
# verify_element_text(locator=(AppiumBy.XPATH, '//(*[@resource-id="android:id/text1"])[1]'), text='Hello', timeout=6)  # Raise TimeoutError

driver.quit()
# =================================================================================
# 9. Exceptions
from selenium.common.exceptions import *
from appium.common.exceptions import *

appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
views_element = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Views')
views_element.click()
list_view = driver.find_element(by=AppiumBy.ID, value='android:id/list')
driver.execute_script('mobile: swipeGesture', {
    'elementId': list_view,
    'direction': 'up',
    'percent': 1.0,
})
sleep(1)
try:
    # driver.find_element(AppiumBy.ID, 'dddd') #NoSuchElementException
    views_element.click() # StaleElementReferenceException
except NoSuchElementException:
    print("Element is not in DOM")

except StaleElementReferenceException:
    print("Stale Element Error raised")
finally:
    print("After handling exception")

driver.quit()




