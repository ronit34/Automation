from selenium.webdriver.support.select import Select
from behave import *
from selenium.webdriver.common.by import By
import time

@then(u'Select Campaign Name from campaign dropdown')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.ID, "camp-report").click()
    entity = context.driver.find_element(By.ID, "camp-report")
    select = Select(entity)
    select.select_by_visible_text("default(2000)")