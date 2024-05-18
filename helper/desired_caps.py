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
        "automationName": "UiAutomator2",
        # "systemPort": "8201"
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

wdio = {
    "appium:appPackage": "com.wdiodemoapp",
    "appium:appActivity": ".MainActivity",
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
}

uidesign = {
    "appium:appPackage": "uidesigns.withsourcecode",
    "appium:appActivity": ".activities.MainActivity",
    "platformName": "Android",
    "appium:automationName": "UiAutomator2"
}

amazon = {
    "appium:appPackage": "com.amazon.mShop.android.shopping",
    "appium:appActivity": "com.amazon.mShop.splashscreen.StartupActivity",
    "platformName": "Android",
    "appium:automationName": "UiAutomator2"
}

swaglab = {
    "appium:appPackage": "com.swaglabsmobileapp",
    "appium:appActivity": ".SplashActivity",
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    # "appium:systemPort": "8201"
}

clockify = {
    "appium:appPackage": "me.clockify.android",
    "appium:appActivity": ".presenter.screens.main.MainActivity",
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
}

chrome_app = {
    "appium:appPackage": "com.android.chrome",
    "appium:appActivity": "com.google.android.apps.chrome.Main",
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "noReset": True
}