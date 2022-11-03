from selenium.webdriver.support.select import Select
from behave import *
from selenium.webdriver.common.by import By
import time


@then(u'click on campaign summary tab in report')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "pills-campaign-summary-tab")
    context.driver.execute_script("arguments[0].click();", button)

