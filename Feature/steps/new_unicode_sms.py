import time
from behave import *
from selenium.webdriver.common.by import By
import CommonUtility as CU
new_unicode_smsObj = CU.new_unicode_sms()

new_unicode_sms_checkboxObj = CU.new_unicode_sms_checkbox()

@then(u'click on Unicode sms')
def click_unicode(context):
    button = context.driver.find_element(By.ID, "unicode_sms_page_link")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check Unicode sms elements are present')
def check_element(context):
    for x in new_unicode_smsObj.new_unicode_sms_list:
        try:
            status = context.driver.find_element(By.ID, x).is_displayed()
            print(f"{x} --> is {status} ")
        except NameError:
            print(NameError)

@then(u'check Unicode sms check boxes are present')
def checkbox(context):
    for x in new_unicode_sms_checkboxObj.new_unicode_sms_checkbox_list:
        try:
            status = context.driver.find_element(By.NAME, x).is_displayed()
            print(f"{x} --> is {status} ")
        except NameError:
            print(NameError)

    # time.sleep(1)
    # context.driver.close()
