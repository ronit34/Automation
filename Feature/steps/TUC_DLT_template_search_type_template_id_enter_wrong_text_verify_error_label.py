import time
from behave import *
from selenium.webdriver.common.by import By


@then(u'Enter wrong text')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.ID, "search-id").send_keys("qwerty")

