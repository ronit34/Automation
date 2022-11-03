from behave import *
from selenium.webdriver.common.by import By
import time
@then(u'select from date "{From}"')
def step_impl(context,From):
    context.driver.find_element(By.ID, "date1").send_keys(From)

@then(u'select to date "{To}"')
def step_impl(context,To):
    context.driver.find_element(By.ID, "date2").send_keys(To)

@then(u'click on search button')
def step_impl(context):
    context.driver.find_element(By.ID, "search_alloc").click()

    # time.sleep(1)
    # context.driver.close()