import time
from behave import *
from selenium.webdriver.common.by import By


@then(u'Enter sender id')
def step_impl(context):
    context.driver.find_element(By.ID, "search-id").send_keys("123456")

