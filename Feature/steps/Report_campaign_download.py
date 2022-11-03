from selenium.webdriver.support.select import Select
from behave import *
from selenium.webdriver.common.by import By
import time

@then(u'click on campaign tab in report')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "pills-campaign-tab")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'click on Search Button in campaign')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "search")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'select Download file type in campaign')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "download_csv")
    context.driver.execute_script("arguments[0].click();", button)


