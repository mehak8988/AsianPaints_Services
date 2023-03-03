import time

from selenium.webdriver.common.by import By



class ServicesPageClass:


    def __init__(self, driver):

        self.ThankYou = "thankYouTitle"
        self.driver = driver
        self.serviceslink = "//a[@data-target='#SERVICES']"


        self.usernameTextBoxElement = "//input[@name='ENQUIRE_NAME']"
        self.useremailTextBoxElement = "//input[@name='ENQUIRE_EMAIL']"
        self.usermobileTextBoxElement = "//input[@name='ENQUIRE_MOBILE']"
        self.userpincodeTextBoxElement = " //input[@name='ENQUIRE_PINCODE']"
        self.EnquireNowButtonElement = "//button[@class='ctaText enquireForm--step-1-submit track_form_submit']"
        self.FrameElement = "//*[@id='__st_fancy_popup']/iframe"
        self.NotNowElement = "//input[@value='Not Now']"
        self.ArrowElement = "(//button[@class='slick-prev slick-arrow'])[2]"

     #Method

    def click_services_link(self):
        servicesLink = self.driver.find_element(By.XPATH, self.serviceslink)
        servicesLink.click()

    def click_KnowMore_Button(self):
        button = self.driver.find_element_by_xpath("(//*[text()='KNOW MORE'])[1]")
        self.driver.execute_script("arguments[0].click();", button)

    def click_Expand_Button(self):
        button = self.driver.find_element_by_xpath("(//*[text()='Click to Expand'])[4]")
        self.driver.execute_script("arguments[0].click();", button)

    def enter_username_textbox(self, uname):
        usernameTextBox = self.driver.find_element(By.XPATH, self.usernameTextBoxElement)
        usernameTextBox.send_keys(uname)

    def enter_useremail_textbox(self, uemail):
        useremailTextBox = self.driver.find_element(By.XPATH, self.useremailTextBoxElement)
        useremailTextBox.send_keys(uemail)

    def enter_usermobile_textbox(self, umobile):
        usermobileTextBox = self.driver.find_element(By.XPATH, self.usermobileTextBoxElement)
        usermobileTextBox.send_keys(umobile)

    def enter_userpincode_textbox(self, upincode):
        userpincodeTextBox = self.driver.find_element(By.XPATH, self.userpincodeTextBoxElement)
        userpincodeTextBox.send_keys(upincode)

    def click_EnquireNow_Button(self):
        EnquireNowButton = self.driver.find_element(By.XPATH, self.EnquireNowButtonElement)
        EnquireNowButton.click()


    def click_Allow_Button(self):
        Frame = self.driver.find_element(By.XPATH, self.FrameElement)
        self.driver.switch_to.frame(Frame)
        clickAllowButton = self.driver.find_element(By.XPATH, self.NotNowElement)
        clickAllowButton.click()
        time.sleep(50)
        self.driver.switch_to.default_content()


    def ThankYouText(self):
        ThankYouText = self.driver.find_element(By.CLASS_NAME, self.ThankYou).text
        return ThankYouText

    def arrowbutton(self):
        arrowvalue = self.driver.find_element(By.XPATH, self.ArrowElement)
        return arrowvalue