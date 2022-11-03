from behave import *
from selenium.webdriver.common.by import By
import time

@then(u'Enter amount "{amt}"')
def step_impl(context,amt):
    context.driver.find_element(By.ID, "amount").send_keys(amt)

@then(u'click on the add button')
def step_impl(context):
    context.driver.find_element(By.ID, "add").click()

    # time.sleep(1)
    # context.driver.close()



