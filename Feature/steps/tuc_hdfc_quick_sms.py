import new_quick_sms_input
from behave import *
from selenium.webdriver.common.by import By
import time


@then(u'send sms through qucick sms')
def step_impl(context):
    context.driver.find_element(By.ID, "newSms").click()
    new_quick_sms_input.quick_sms(context)

    # time.sleep(1)
    # context.driver.close()
