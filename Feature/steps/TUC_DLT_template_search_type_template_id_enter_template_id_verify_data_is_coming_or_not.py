import time
from behave import *
from selenium.webdriver.common.by import By


@then(u'Enter template id in template')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.ID, "search-id").send_keys("12345")
