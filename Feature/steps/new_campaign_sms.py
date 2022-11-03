import time
from behave import *
from selenium.webdriver.common.by import By

import CommonUtility as CU
new_campaign_smsObj = CU.new_campaign_sms()

new_campaign_sms_checkboxObj = CU.new_campaign_sms_checkbox()

@then(u'click on campaign sms')
def campaign_sms(context):

    button = context.driver.find_element(By.ID, "campaign_sms_page_link")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check campaign sms elements are present')
def check_elements(context):
    for x in new_campaign_smsObj.new_campaign_sms_list:
        try:
            status = context.driver.find_element(By.ID, x).is_displayed()
            print(f"{x} --> is {status} ")
        except NameError:
            print(NameError)

@then(u'check campaign sms check boxes are present')
def check_by_name(context):
    for x in new_campaign_sms_checkboxObj.new_campaign_sms_checkbox_list:
        try:
            status = context.driver.find_element(By.NAME, x).is_displayed()
            print(f"{x} --> is {status} ")
        except NameError:
            print(NameError)

    # time.sleep(1)
    # context.driver.close()

