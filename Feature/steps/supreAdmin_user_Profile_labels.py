from behave import *
from selenium.webdriver.common.by import By
import time

@then(u'click on super admin after which drop down menu will appear')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("dropdown-caret")
    context.driver.execute_script("arguments[0].click();", button)
