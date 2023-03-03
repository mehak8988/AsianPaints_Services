import time
from features.utility.UtilityClass import UtilityClass

def before_scenario(context, driver):
    UtilityClass.launch_browser(context)
    context.driver.implicitly_wait(1)


    UtilityClass.launch_browser_notification(context)
    context.driver.implicitly_wait(1)

    UtilityClass.browser_maximise(context)
    context.driver.implicitly_wait(1)

    UtilityClass.launch_app(context)
    context.driver.implicitly_wait(1)






def after_scenario(context, driver):
    time.sleep(1)
    UtilityClass.close_browser(context)