import time
from behave import *
from selenium.webdriver.common.by import By


@then(u'Click on Update credits and click cross and cancel button')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "update_balance")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(2)
    button1 = context.driver.find_element(By.ID, "cancel")
    context.driver.execute_script("arguments[0].click();", button1)

    time.sleep(2)
    button2 = context.driver.find_element(By.ID, "update_balance")
    context.driver.execute_script("arguments[0].click();", button2)

    time.sleep(2)
    button3 = context.driver.find_element(By.ID, "cancel")
    context.driver.execute_script("arguments[0].click();", button3)