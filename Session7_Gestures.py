from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from time import sleep

# Deprecated in warning status
from appium.webdriver.common.touch_action import TouchAction

# Deprecated in warning status
from appium.webdriver.common.multi_action import MultiAction

# W3C compatible: create more gestures
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.mouse_button import MouseButton

# W3C compatible: available as driver methods
from appium.webdriver.extensions.action_helpers import ActionHelpers

from helper import desired_caps

# =================================================================================
## Different ways to make gestures in appium:
# 1. "touch_action/multi_action" libraries (deprecated)
# 2. W3C Actions (action_builder library)
# 3. "action_helper" library (some already created w3c actions)
# 4. Mobile gestures
#   - (https://github.com/appium/appium-uiautomator2-driver/tree/master?tab=readme-ov-file#mobile-gesture-commands)
#   - (https://github.com/appium/appium-uiautomator2-driver/blob/master/docs/android-mobile-gestures.md)
# 5. Android UiScrollable Class (https://developer.android.com/reference/androidx/test/uiautomator/UiScrollable)
# 6. Appium Gesture Plugin (https://github.com/AppiumTestDistribution/appium-gestures-plugin)
# =================================================================================
## Difference between gestures:
# Tap: Use fingers
# Click: Use mouse
# Press: Use input device / Hold fingers on screen
# Scroll: From element to another element
# Swipe: From a point to another point (With duration - Release hand after it is done)
# Flick: From a point to another point (No control and duration - Release hand before it is done)
# =================================================================================
appium_server = "http://127.0.0.1:4723"
# >>> All `sleep`s are for demo purpose
# =================================================================================
# 0. Get element rect (bounds) - Location (Coordination - X,Y) | Size (Height, Width)
appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.implicitly_wait(5) 
el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Animation')
print(el.rect)
print(el.location)
print(el.location_in_view)
driver.quit()

# =================================================================================
# 0. Get window rect/size (bounds) - Location (Coordination - X,Y) | Size (Height, Width)
appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.implicitly_wait(5)
window_rect = driver.get_window_rect()
window_size = driver.get_window_size()
print(window_rect)
print(window_size)
driver.quit()

# =================================================================================
# 1. Tap (Single) - Actions API - W3C
appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Views').click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Controls').click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='1. Light Theme').click()
driver.tap([(0, 596)])
sleep(2)  # For demo purpose
driver.quit()

# =================================================================================
# 2. Tap (Multi-finger) - Actions API - W3C
appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Views').click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Controls').click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='1. Light Theme').click()
# driver.tap([(0, 840), (0, 1008), (0, 1344), (0, 1456), (0, 1615)]) # 100ms
driver.tap([(0, 840), (0, 1008), (0, 1344), (0, 1456), (0, 1615)], 1000) # 1000ms
sleep(2)  # For demo purpose
driver.quit()
# =================================================================================
# 3. Tap (Single) - TouchAction
appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Views').click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Controls').click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='1. Light Theme').click()
action = TouchAction(driver)
action.tap(x=0, y=596).perform()
sleep(2)  # For demo purpose
driver.quit()

# =================================================================================
# 4. Tap (Multi-finger) - TouchAction
appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Views').click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Controls').click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='1. Light Theme').click()
action1 = TouchAction(driver)
action2 = TouchAction(driver)
action3 = TouchAction(driver)

# Perform separately: 
# action1.tap(x=0, y=596).perform()
# action2.tap(x=0, y=840).perform()
# action3.tap(x=0, y=1008).perform()

# Or perform together:
action1.tap(x=0, y=596)
action2.tap(x=0, y=840)
action3.tap(x=0, y=1008)
multi_action = MultiAction(driver)
multi_action.add(action1, action2, action3)
multi_action.perform()
sleep(2)  # For demo purpose
driver.quit()

# =================================================================================
# 5.Double Tap - TouchAction
appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Text').click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='LogTextBox').click()
action = TouchAction(driver)
el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Add')
action.tap(element=el, count=2).perform()
text_el = driver.find_element(by=AppiumBy.ID, value='io.appium.android.apis:id/text')
print(text_el.get_attribute('text'))
sleep(2)  # For demo purpose
driver.quit()

# =================================================================================
# 6. Double Tap - Actions API - W3C
appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Text').click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='LogTextBox').click()
el_coords = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Add').location
driver.tap([(el_coords['x'], el_coords['y'])])
driver.tap([(el_coords['x'], el_coords['y'])])
text_el = driver.find_element(by=AppiumBy.ID, value='io.appium.android.apis:id/text')
print(text_el.get_attribute('text'))
sleep(2)  # For demo purpose
driver.quit()

# =================================================================================
# 7. Double Tap - Mobile Gesture Commands - W3C
appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Text').click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='LogTextBox').click()
el_coords = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Add').location
driver.execute_script('mobile: doubleClickGesture', {'x': el_coords['x'], 'y': el_coords['y']})
sleep(2)  # For demo purpose
driver.quit()

# =================================================================================
# 8. Press and Hold - TouchAction
appium_options = UiAutomator2Options().load_capabilities(desired_caps.contacts)
driver = webdriver.Remote(appium_server, options=appium_options)
contacts = driver.find_elements(by=AppiumBy.ID, value="com.android.contacts:id/cliv_name_textview")
actions = TouchAction(driver)

# actions.long_press(el=contacts[0]).perform()
# or:
actions.press(el=contacts[0]).wait(ms=1000).release().perform()
sleep(2)  # For demo purpose
driver.quit()

# =================================================================================
# 9. Press and Hold - Actions API - W3C
appium_options = UiAutomator2Options().load_capabilities(desired_caps.contacts)
driver = webdriver.Remote(appium_server, options=appium_options)
contacts = driver.find_elements(by=AppiumBy.ID, value="com.android.contacts:id/cliv_name_textview")
chains = ActionChains(driver)
chains.w3c_actions.pointer_action.click_and_hold(contacts[0])
chains.perform()
sleep(2)  # For demo purpose
driver.quit()

# =================================================================================
# 10. Press and Hold - Mobile Gesture Commands - W3C
appium_options = UiAutomator2Options().load_capabilities(desired_caps.contacts)
driver = webdriver.Remote(appium_server, options=appium_options)
contacts = driver.find_elements(by=AppiumBy.ID, value="com.android.contacts:id/cliv_name_textview")
element_coord = contacts[0].location
driver.execute_script('mobile: longClickGesture', {'x': element_coord['x'], 'y': element_coord['y'], 'duration': 1000})
sleep(2)  # For demo purpose
driver.quit()

# =================================================================================
# 11. Scroll Down/Up - TouchAction
appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Views').click()
actions = TouchAction(driver)

# Scroll Down
up_el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Buttons')
down_el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Grid')
actions.press(el=down_el).move_to(x=up_el.location['x'], y=up_el.location['y']).release().perform()

# Scroll Up
grid_el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Grid')
picker_el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Picker')
actions.press(el=grid_el).move_to(el=picker_el).release().perform()
sleep(2)  # For demo purpose
driver.quit()

# =================================================================================
# 12. Scroll Down - TouchAction - with calculations
appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Views').click()
actions = TouchAction(driver)
up_el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Buttons')
down_el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Grid')
up_el_coord = up_el.location
down_el_coord = down_el.location
window_size = driver.get_window_size()
down_el_x = window_size['width'] / 2 + down_el_coord['x']
up_el_x = window_size['width'] / 2 + up_el_coord['x']
actions.press(x=down_el_x, y=down_el_coord['y']).move_to(x=up_el_x, y=up_el_coord['y']).release().perform()
sleep(2)  # For demo purpose
driver.quit()

# =================================================================================
# 13. Scroll Down/Up - Actions API - W3C
appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Views').click()
buttons_el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Buttons')
grid_el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Grid')
# Scroll Down
driver.scroll(origin_el=grid_el, destination_el=buttons_el)
sleep(1)  # For demo purpose
# Scroll Up
grid_el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Grid')
picker_el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Picker')
driver.scroll(grid_el, picker_el)
sleep(2)  # For demo purpose
driver.quit()

# =================================================================================
# 14. Scroll Right/Left - Actions API - W3C
appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Views').click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Gallery').click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='1. Photos').click()
# Scroll Right
image_views = driver.find_elements(AppiumBy.CLASS_NAME, value='android.widget.ImageView')
driver.scroll(image_views[2], image_views[0], duration=400)
# Scroll Left
image_views = driver.find_elements(AppiumBy.CLASS_NAME, value='android.widget.ImageView')
driver.scroll(image_views[0], image_views[2])
sleep(2)  # For demo purpose
driver.quit()

# =================================================================================
# 15. Scroll Down/Up - Mobile Gesture Commands - W3C
appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Views').click()
print(driver.get_window_size())
# Scroll Down - with Element
list_view = driver.find_element(by=AppiumBy.ID, value='android:id/list')
driver.execute_script('mobile: scrollGesture', {
    'elementId': list_view,
    'direction': 'down',
    'percent': 2,
})
# Scroll Up - with Element
list_view = driver.find_element(by=AppiumBy.ID, value='android:id/list')
driver.execute_script('mobile: scrollGesture', {
    'elementId': list_view,
    'direction': 'up',
    'percent': 0.5,
    'speed': 1000
})
sleep(2)  # For demo purpose
driver.quit()

# =================================================================================
# 16. Scroll Right/Left - Mobile Gesture Commands - W3C
appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Views').click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Gallery').click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='1. Photos').click()
# Scroll Right - with Bounds
driver.execute_script('mobile: scrollGesture', {
    'left': 500, 'top': 500, 'width': 500, 'height': 0,
    'direction': 'right',
    'percent': 1.0
})
sleep(1)  # For demo purpose
# Scroll Left - with Bounds
driver.execute_script('mobile: scrollGesture', {
    'left': 500, 'top': 500, 'width': 500, 'height': 0,
    'direction': 'left',
    'percent': 1.0
})
sleep(2)  # For demo purpose
driver.quit()

# =================================================================================
# 17. Scroll Element Into View (Search for element) - UiScrollable Class
appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Views').click()
driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Picker").instance(0))')
sleep(2)  # For demo purpose
driver.quit()

# =================================================================================
# 18. Scroll Element Into View (Search for element) - Mobile Gesture Commands - W3C
appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Views').click()
driver.execute_script('mobile: scroll', {'strategy': 'accessibility id', 'selector': 'Picker'})
sleep(2)  # For demo purpose
driver.quit()

# =================================================================================
# 19. Scroll to End/Beginning - UiScrollable Class
appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Views').click()
driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiScrollable(new UiSelector().scrollable(true)).setAsVerticalList().scrollToEnd(5)')
sleep(1)  # For demo purpose
driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiScrollable(new UiSelector().scrollable(true)).setAsVerticalList().scrollToBeginning(5)')
sleep(2)  # For demo purpose
driver.quit()

# =================================================================================
# 20. Swipe Up/Down - Actions API - W3C
appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Views').click()
buttons_el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Buttons')
grid_el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Grid')
# Swipe Up
driver.swipe(start_x=grid_el.location['x'], start_y=grid_el.location['y'], end_x=buttons_el.location['x'], end_y=buttons_el.location['y'])
# Swipe Down
grid_el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Grid')
picker_el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Picker')
driver.swipe(start_x=grid_el.location['x'], start_y=grid_el.location['y'], end_x=picker_el.location['x'], end_y=picker_el.location['y'])
sleep(2)  # For demo purpose
driver.quit()

# =================================================================================
# 21. Swipe Up/Down - Mobile Gesture Commands - W3C
appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Views').click()
# Swipe Up - With Element
list_view = driver.find_element(by=AppiumBy.ID, value='android:id/list')
driver.execute_script('mobile: swipeGesture', {
    'elementId': list_view,
    'direction': 'up',
    'percent': 0.3,
    'speed': 5000
})
# Swipe Down - With Element
list_view = driver.find_element(by=AppiumBy.ID, value='android:id/list')
driver.execute_script('mobile: swipeGesture', {
    'elementId': list_view,
    'direction': 'down',
    'percent': 0.3,
    'speed': 3000
})
sleep(2)  # For demo purpose
driver.quit()

# =================================================================================
# 22. Swipe Left/Right - Actions API - W3C
appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Views').click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Gallery').click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='1. Photos').click()

# Swipe Left
image_views = driver.find_elements(AppiumBy.CLASS_NAME, value='android.widget.ImageView')
driver.swipe(image_views[2].location['x'], image_views[2].location['y'], image_views[0].location['x'], image_views[0].location['y'])

# Swipe Right
image_views = driver.find_elements(AppiumBy.CLASS_NAME, value='android.widget.ImageView')
driver.swipe(image_views[0].location['x'], image_views[0].location['y'], image_views[2].location['x'], image_views[2].location['y'])
sleep(2)  # For demo purpose
driver.quit()

# =================================================================================
# 23. Swipe Left/Right - Mobile Gesture Commands - W3C
appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Views').click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Gallery').click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='1. Photos').click()
# Swipe Left
galley = driver.find_element(by=AppiumBy.ID, value='io.appium.android.apis:id/gallery')
driver.execute_script('mobile: swipeGesture', {
    'elementId': galley,
    'direction': 'left',
    'percent': 0.3,
    'speed': 5000
})
# Swipe Right
galley = driver.find_element(by=AppiumBy.ID, value='io.appium.android.apis:id/gallery')
driver.execute_script('mobile: swipeGesture', {
    'elementId': galley,
    'direction': 'right',
    'percent': 0.3,
    'speed': 3000
})
sleep(2)  # For demo purpose
driver.quit()

# =================================================================================
# 24. Flick Up/Down (Fling/Flip) - Actions API - W3C
appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Views').click()
buttons_el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Buttons')
grid_el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Grid')
# Flick Up
driver.flick(start_x=grid_el.location['x'], start_y=grid_el.location['y'], end_x=buttons_el.location['x'], end_y=buttons_el.location['y'])
# Flick Down
grid_el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Grid')
picker_el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Picker')
driver.flick(start_x=250, start_y=900, end_x=250, end_y=2300)
sleep(2)  # For demo purpose
driver.quit()

# =================================================================================
# 25. Flick Up|Down (Fling/Flip) - Mobile Gesture Commands - W3C
appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Views').click()
# Flick Up
list_view = driver.find_element(by=AppiumBy.ID, value='android:id/list')
list_view_rect = list_view.rect
driver.execute_script('mobile: flingGesture', {
    'elementId': list_view,
    'direction': 'down',
    'percent': 1,
})
sleep(1)  # For demo purpose
# Flick Down
sleep(1)  # For demo purpose
driver.execute_script('mobile: flingGesture', {
    'left': list_view_rect['x'],
    'top': list_view_rect['y'],
    'direction': 'up',
    'width': list_view_rect['width'],
    'height': list_view_rect['height'],
    'percent': 2,
})
sleep(2)  # For demo purpose
driver.quit()

# =================================================================================
# 26. Flick (Fling/Flip) - UiScrollable

# =================================================================================
# 27. Drag and Drop - TouchAction
appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Views').click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Drag and Drop').click()
el1 = driver.find_element(by=AppiumBy.ID, value='io.appium.android.apis:id/drag_dot_1')
el2 = driver.find_element(by=AppiumBy.ID, value='io.appium.android.apis:id/drag_dot_2')
el3 = driver.find_element(by=AppiumBy.ID, value='io.appium.android.apis:id/drag_dot_3')
actions = TouchAction(driver)
actions.long_press(el1).move_to(el2).release().perform()
result = driver.find_element(by=AppiumBy.ID, value='io.appium.android.apis:id/drag_result_text').get_attribute('text')
print(result)
sleep(2)  # For demo purpose
driver.quit()

# =================================================================================
# 28. Drag and Drop - Actions API - W3C
appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Views').click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Drag and Drop').click()
el1 = driver.find_element(by=AppiumBy.ID, value='io.appium.android.apis:id/drag_dot_1')
el2 = driver.find_element(by=AppiumBy.ID, value='io.appium.android.apis:id/drag_dot_2')
el3 = driver.find_element(by=AppiumBy.ID, value='io.appium.android.apis:id/drag_dot_3')
actions = ActionChains(driver)
actions.w3c_actions.pointer_action.click_and_hold(el1)
actions.w3c_actions.pointer_action.pause(1)
actions.w3c_actions.pointer_action.move_to(el2)
actions.w3c_actions.pointer_action.release()
actions.perform()
# driver.drag_and_drop(el1, el2)
result = driver.find_element(by=AppiumBy.ID, value='io.appium.android.apis:id/drag_result_text').get_attribute('text')
print(result)
sleep(2)  # For demo purpose
driver.quit()

# =================================================================================
# 29. Drag and Drop - Mobile Gesture Commands - W3C
appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Views').click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Drag and Drop').click()
el1 = driver.find_element(by=AppiumBy.ID, value='io.appium.android.apis:id/drag_dot_1')
el2 = driver.find_element(by=AppiumBy.ID, value='io.appium.android.apis:id/drag_dot_2')
driver.execute_script('mobile: dragGesture', {
    'elementId': el1,
    'endX': el2.location['x'],
    'endY': el2.location['y']
})

result = driver.find_element(by=AppiumBy.ID, value='io.appium.android.apis:id/drag_result_text').get_attribute('text')
print(result)
sleep(2)  # For demo purpose
driver.quit()

# =================================================================================
# Drag and Drop - WebDriverIO Demo App - Actions API - W3C
appium_options = UiAutomator2Options().load_capabilities(desired_caps.wdio)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.implicitly_wait(5)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Drag').click()
draggable_el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'drag-c1')
droppable_el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'drop-c1')

driver.drag_and_drop(draggable_el, droppable_el)

sleep(2)  # For demo purpose
driver.quit()
# =================================================================================
# Drag and Drop - WebDriverIO Demo App - Mobile Gesture Commands - W3C
appium_options = UiAutomator2Options().load_capabilities(desired_caps.wdio)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.implicitly_wait(5)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Drag').click()
draggable_el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'drag-c1')
droppable_el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'drop-c1')

driver.execute_script('mobile: dragGesture', {
    'elementId': draggable_el,
    'endX': droppable_el.location['x'],
    'endY': droppable_el.location['y']
})

sleep(2)  # For demo purpose
driver.quit()

# =================================================================================
# 30. Pinch In/Out (Zoom In/Out) - Mobile Gesture Commands - W3C
appium_options = UiAutomator2Options().load_capabilities(desired_caps.maps)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.implicitly_wait(10)
driver.find_element(by=AppiumBy.XPATH, value="//*[@text='SKIP']").click()
sleep(5)  # For demo purpose
driver.execute_script('mobile: pinchOpenGesture', {
    'left': 200,
    'top': 800,
    'width': 1000,
    'height': 1000,
    'percent': 0.5,
})
sleep(3)  # For demo purpose
driver.execute_script('mobile: pinchCloseGesture', {
    'left': 200,
    'top': 800,
    'width': 1000,
    'height': 1000,
    'percent': 1,
})
sleep(2)  # For demo purpose
driver.quit()

# =================================================================================
# 31. Pinch In/Out (Zoom In/Out) - Actions API - W3C
appium_options = UiAutomator2Options().load_capabilities(desired_caps.maps)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.implicitly_wait(10)
driver.find_element(by=AppiumBy.XPATH, value="//*[@text='SKIP']").click()
sleep(5)  # For demo purpose
window_size = driver.get_window_size()
center_x = window_size['width']/2
center_y = window_size['height']/2
print(f'Center: {center_x}px, {center_y}px')

actions = ActionChains(driver)
actions.w3c_actions.devices = []
finger1 = actions.w3c_actions.add_pointer_input('touch', 'finger1')
finger2 = actions.w3c_actions.add_pointer_input('touch', 'finger2')

# Zoom In
finger1.create_pointer_move(x=center_x-100, y=center_y)
finger1.create_pointer_down(button=MouseButton.LEFT)
finger1.create_pause(0.5)
finger1.create_pointer_move(x=center_x-500, y=center_y, duration=50)
finger1.create_pointer_up(button=MouseButton.LEFT)

finger2.create_pointer_move(x=center_x+100, y=center_y)
finger2.create_pointer_down(button=MouseButton.LEFT)
finger2.create_pause(0.5)
finger2.create_pointer_move(x=center_x+500, y=center_y, duration=50)
finger2.create_pointer_up(button=MouseButton.LEFT)

actions.perform()
sleep(3)  # For demo purpose

# Zoom Out
finger1.create_pointer_move(x=center_x-500, y=center_y)
finger1.create_pointer_down(button=MouseButton.LEFT)
finger1.create_pause(0.5)
finger1.create_pointer_move(x=center_x-100, y=center_y, duration=50)
finger1.create_pointer_up(button=MouseButton.LEFT)

finger2.create_pointer_move(x=center_x+500, y=center_y)
finger2.create_pointer_down(button=MouseButton.LEFT)
finger2.create_pause(0.5)
finger2.create_pointer_move(x=center_x+100, y=center_y, duration=50)
finger2.create_pointer_up(button=MouseButton.LEFT)

actions.perform()

sleep(2)  # For demo purpose
driver.quit()

# =================================================================================
## appium-gestures-plugin (https://github.com/AppiumTestDistribution/appium-gestures-plugin)
# Install using `appium plugin install --source=npm appium-gestures-plugin`
# Then run appium server  with this plugin: `appium --use-plugins=gestures`

# =================================================================================
# 32. Plugin - ScrollElementIntoView (Search)
appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Views').click()
list_view = driver.find_element(by=AppiumBy.ID, value='android:id/list')
driver.execute_script('gesture: scrollElementIntoView',
                      {'scrollableView': list_view.id, 'strategy': 'accessibility id', 'selector': 'Picker',
                       'percentage': 50, 'direction': 'up', 'maxCount': 3})
sleep(2)  # For demo purpose
driver.quit()

# =================================================================================
# 33. Plugin - Drag and Drop
appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Views').click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Drag and Drop').click()
el1 = driver.find_element(by=AppiumBy.ID, value='io.appium.android.apis:id/drag_dot_1')
el2 = driver.find_element(by=AppiumBy.ID, value='io.appium.android.apis:id/drag_dot_2')
driver.execute_script('gesture: dragAndDrop', {
    'sourceId': el1.id,
    'destinationId': el2.id,
})
result = driver.find_element(by=AppiumBy.ID, value='io.appium.android.apis:id/drag_result_text').get_attribute('text')
print(result)
sleep(2)  # For demo purpose
driver.quit()

# =================================================================================
# 34. Gestures in Mobile web browser
# Drag and Drop using W3C Actions

appium_options = UiAutomator2Options().load_capabilities(desired_caps.chrome)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.get("https://selenium08.blogspot.com/2020/01/drag-drop.html")
el1 = driver.find_element(AppiumBy.CSS_SELECTOR, '#draggable')
el2 = driver.find_element(AppiumBy.CSS_SELECTOR, '#droppable')
actions = ActionChains(driver)
actions.w3c_actions.pointer_action.click_and_hold(el1)
actions.w3c_actions.pointer_action.pause(1)
actions.w3c_actions.pointer_action.move_to(el2)
actions.w3c_actions.pointer_action.release()
actions.perform()
sleep(2)  # For demo purpose
driver.quit()
# =================================================================================

# Inspector Gesture Creator


