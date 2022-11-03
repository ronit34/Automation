from behave import *
from selenium.webdriver.common.by import By
import time

import CommonUtility as CU
new_dynamic_smsObj = CU.new_dynamic_sms()

new_dynamic_sms_checkboxObj = CU.new_dynamic_sms_checkbox()

@then(u'click on Dynamic sms')
def step_impl(context):
    button = context.driver.find_element(By.ID, "dynamic_sms_page_link")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'check Dynamic sms elements are present')
def step_impl(context):
    for x in new_dynamic_smsObj.new_dynamic_sms_list:
        try:
            status = context.driver.find_element(By.ID, x).is_displayed()
            print(f"{x} --> is {status} ")
        except NameError:
            print(NameError)

@then(u'check Dynamic sms check boxes are present')
def step_impl(context):
    for x in new_dynamic_sms_checkboxObj.new_dynamic_sms_checkbox_list:
        try:
            status = context.driver.find_element(By.NAME, x).is_displayed()
            print(f"{x} --> is {status} ")
        except NameError:
            print(NameError)

    # time.sleep(1)
    # context.driver.close()
