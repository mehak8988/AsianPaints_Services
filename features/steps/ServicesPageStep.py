import time

import self
from hamcrest import *
from behave import *
from selenium.webdriver.common.by import By

from features.pages.ServicesPageClass import ServicesPageClass




@given("Chrome is opened and Asian Paints app is opened")
def step_impl(context):
    context.driver.implicitly_wait(5)

    expectedTitle = "Trusted Wall Painting, Home Painting & Waterproofing in India - Asian Paints"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)

    assert_that(expectedTitle, equal_to(actualTitle))

'''@when("user clicks on Allow Button")
def step_impl(context):
    context.driver.implicitly_wait(5)
    Allowvalue= ServicesPageClass(context.driver)
    Allowvalue.click_Allow_Button()'''





@when(u'customer is able to click on services link')
def step_impl(context):
    context.driver.implicitly_wait(5)
    ServicesPage = ServicesPageClass(context.driver)
    ServicesPage.click_services_link()



@then(u'It shows services page')
def step_impl(context):
    context.driver.implicitly_wait(4)
    expectedTitle = "Services Designed for your Home Paint Solutions - Asian Paints"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))


@when(u'customer is able to click on Know More Button')
def step_impl(context):
    context.driver.implicitly_wait(4)
    ServicePage= ServicesPageClass(context.driver)
    ServicePage.click_KnowMore_Button()


@then(u'It shows the page Safe Painting Services:Home Painting Services For Interior & Exterior House Painting - Asian Paints')
def step_impl(context):
    context.driver.implicitly_wait(1)
    expectedTitle = "Safe Painting Services: Home Painting Services For Interior & Exterior House Painting - Asian Paints"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))



@when(u'customer is able to click on Expand Button')
def step_impl(context):
    context.driver.implicitly_wait(1)
    ServicePage = ServicesPageClass(context.driver)
    ServicePage.click_Expand_Button()


'''@then(u'It show content')
def step_impl(context):
   context.driver.implicitly_wait(2)
   Text = ServicesPageClass(context.driver)
   actualText = Text.searchtext()
   print("The Text is  ",actualText)'''

@then(u'It show content')
def step_impl(context):
    context.driver.implicitly_wait(5)
    services = ServicesPageClass(context.driver)
    if(services.arrowbutton()):
        print("working")
    else:
        print("Not working")





@when(u'customer enters {uname} and {uemail} and {umobile} and {upincode}')
def step_impl(context, uname, uemail, umobile, upincode):
    context.driver.implicitly_wait(2)

    ServicesPage = ServicesPageClass(context.driver)

    ServicesPage.enter_username_textbox(uname)
    time.sleep(1)

    ServicesPage.enter_useremail_textbox(uemail)
    time.sleep(1)

    ServicesPage.enter_usermobile_textbox(umobile)
    time.sleep(1)

    ServicesPage.enter_userpincode_textbox(upincode)
    time.sleep(1)




@when(u'customer clicks on Enquire Now Button')
def step_impl(context):
    context.driver.implicitly_wait(2)
    ServicePage = ServicesPageClass(context.driver)
    ServicePage.click_EnquireNow_Button()


@then(u'it shows Thank you image')
def step_impl(context):

    #It will check if ecpectedText ==actualText and print the actualText

    time.sleep(2)
    ServicesPage = ServicesPageClass(context.driver)
    expectedText = " Thank you!"
    actualText = ServicesPage.ThankYouText()

    print(actualText)
    assert_that(expectedText, actualText, "Text is not same")




@then(u'It is on the same page')
def step_impl(context):
    expectedTitle = "Services Designed for your Home Paint Solutions - Asian Paints"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))


@when("user clicks on Not Now button")
def step_impl(context):
    time.sleep(6)
    Allowvalue = ServicesPageClass(context.driver)
    Allowvalue.click_Allow_Button()