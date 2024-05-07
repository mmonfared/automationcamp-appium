from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from helper import desired_caps

appium_server = "http://127.0.0.1:4723"

# =================================================================================
# Types of applications:
# 1. Native
# 2. WebView/PWA
# 3. Hybrid (Native+WebView)

# =================================================================================
# 1 - Open Mobile Browser Directly > Session 5
# =================================================================================
# 2 - Contexts + Handle Hybrid App (Webview or Internal Browser)
appium_options = UiAutomator2Options().load_capabilities(desired_caps.swaglab)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.implicitly_wait(8)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'test-Username').send_keys("standard_user")
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'test-Password').send_keys("secret_sauce")
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'test-LOGIN').click()

driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'test-Menu').click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'test-WEBVIEW').click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'test-enter a https url here...').send_keys("https://www.monfared.io")
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'test-GO TO SITE').click()

# Chrome driver should be passed
# `appium server --allow-insecure chromedriver_autodownload`

# All contexts
# The first item in the list is always NATIVE
# The last item in the list is WEBVIEW
contexts = driver.contexts # ['NATIVE_APP', 'WEBVIEW_com.swaglabsmobileapp']

# Get current context
current_context = driver.current_context # or driver.context

# Switch to WEBVIEW context
driver.switch_to.context(contexts[-1])

# Action on WEBVIEW element
driver.find_element(AppiumBy.CSS_SELECTOR, ".readme").click()

# Switch back to NATIVE context
driver.switch_to.context(contexts[0])

# Action on NATIVE element
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'test-Menu').click()

driver.quit()

# =================================================================================
# 3 - NoSuchContextException
from appium.common.exceptions import NoSuchContextException
try:
    driver.switch_to.context('Wrong Context')
except NoSuchContextException:
    print("The context name is wrong")

# =================================================================================
# 4 - Switch to Chrome Browser (External) and Back to NATIVE app

appium_options = UiAutomator2Options().load_capabilities(desired_caps.contacts)
driver = webdriver.Remote(appium_server, options=appium_options)
wait = WebDriverWait(driver, 10)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Open navigation drawer').click()
driver.find_element(AppiumBy.ID, 'com.android.contacts:id/nav_settings').click()
driver.find_element(AppiumBy.XPATH, '//*[@text="About Contacts"]').click()
driver.find_element(AppiumBy.XPATH, '//*[@text="Terms of service"]').click()

# Wait for Google terms page to be loaded
sleep(5)

# Switch to chrome WEBVIEW
driver.switch_to.context('WEBVIEW_chrome')

# Switch to current tab (last)
handles = driver.window_handles
driver.switch_to.window(handles[0])

# Perform action on WEBVIEW element
driver.find_element(AppiumBy.XPATH, '//*[@aria-label="Main menu"]').click()
wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//*[@href="terms/information-requests"]')))

# Bring NATIVE app to front
driver.press_keycode(187)
sleep(0.5)
driver.press_keycode(187)

# Switch back to NATIVE app
driver.switch_to.context('NATIVE_APP')

# Verify NATIVE app is open
wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//*[@text="Privacy policy"]')))

driver.quit()

# =================================================================================
# 5 - Internal Browser but in NATIVE context
appium_options = UiAutomator2Options().load_capabilities(desired_caps.maps)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 5)
driver.find_element(by=AppiumBy.XPATH, value="//*[@text='SKIP']").click()
driver.find_element(AppiumBy.ID, 'com.google.android.apps.maps:id/og_apd_ring_view').click()
driver.find_element(AppiumBy.ID, 'com.google.android.apps.maps:id/og_privacy_policy_button').click()
sleep(5)
print(driver.contexts)
# driver.switch_to.context(driver.contexts[-1])
wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//*[contains(@text,'When you use our services')]")))

driver.quit()