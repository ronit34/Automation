from behave import *
from selenium.webdriver.common.by import By
import time

@then(u'click on the SMS API Update button')
def step_impl(context):
    context.driver.find_element(By.ID, "update_smsapi_license").click()

@then(u'click on add button of SMS API')
def step_impl(context):
    context.driver.find_element(By.ID, "add").click()

    # time.sleep(1)
    # context.driver.close()

