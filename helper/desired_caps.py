chrome = {
    "platformName": "Android",
    "browserName": "Chrome",
    "appium:options": {
        "automationName": "UiAutomator2",
        # "chromedriverExecutable": "C:/chromedriver.exe"
    }
}

apidemos = {
    "platformName": "Android",
    "appium:options": {
        "appPackage": "io.appium.android.apis",
        "appActivity": ".ApiDemos",
        ":automationName": "UiAutomator2"
    }
}

contacts = {
    "appium:appPackage": "com.android.contacts",
    "appium:appActivity": ".activities.PeopleActivity",
    "platformName": "Android",
    "appium:automationName": "UiAutomator2"
}

maps = {
    "appium:appPackage": "com.google.android.apps.maps",
    "appium:appActivity": "com.google.android.maps.MapsActivity",
    "platformName": "Android",
    "appium:automationName": "UiAutomator2"
}
