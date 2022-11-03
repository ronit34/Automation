import time
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

@then(u'Click on Delete All button')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "delete-phonebook-number")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'Click on Delete button of the pop up')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "delete")
    context.driver.execute_script("arguments[0].click();", button)

    # time.sleep(1)
    # context.driver.close()