import time

from behave import *

from datafiles import ExcelUtils
from features.pages.ServicesPageClass import ServicesPageClass
from features.utility.ConfigClass import ConfigClass




@when("user enters {name} and {email} and {mobile} and {pincode}")
def step_impl(context, name, email, mobile, pincode):

    ExcelUtils.get_row_count(ConfigClass.datafilespath, "Sheet1")

    name = ExcelUtils.read_data(ConfigClass.datafilespath, "Sheet1", 2, 1)
    email = ExcelUtils.read_data(ConfigClass.datafilespath, "Sheet1", 2, 2)
    mobile = ExcelUtils.read_data(ConfigClass.datafilespath, "Sheet1", 2, 3)
    pincode = ExcelUtils.read_data(ConfigClass.datafilespath, "Sheet1", 2, 4)

    ServicesPage = ServicesPageClass(context.driver)
    ServicesPage.enter_username_textbox(name)
    context.driver.implicitly_wait(1)

    ServicesPage.enter_useremail_textbox(email)
    context.driver.implicitly_wait(1)

    ServicesPage.enter_usermobile_textbox(mobile)
    context.driver.implicitly_wait(1)

    ServicesPage.enter_userpincode_textbox(pincode)
    context.driver.implicitly_wait(1)


@then("it shows valid search result page 2")
def step_impl(context):
    expectedTitle = "Services Designed for your Home Paint Solutions - Asian Paints"
    PageTitle = context.driver.title
    try:
      if (expectedTitle == PageTitle):
          assert True
          print("Test is passed")
          ExcelUtils.write_data(ConfigClass.datafilespath, "Sheet1", 2, 5, "Passed")
      else:
          print("Test is failed")
          ExcelUtils.write_data(ConfigClass.datafilespath, "Sheet1", 2, 5, "Failed")
          assert False
      time.sleep(1)
    finally:
        print("page title is" + PageTitle)
        time.sleep(1)


