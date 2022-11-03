from behave import *
from selenium.webdriver.common.by import By
import time
import CommonUtility as CU
new_smsObj = CU.new_sms()

@then(u'check new sms is present')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.driver.find_element(By.ID, "newSms").is_displayed()

@then(u'click on new sms')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "newSms")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check ALL new sms elements are present')
def step_impl(context):
    for x in new_smsObj.new_sms_label_list:
        try:
            status = context.driver.find_element(By.ID, x).is_displayed()
            print(f"{x} --> is {status} ")
        except NameError:
            print(NameError)

    # time.sleep(1)
    # context.driver.close()
