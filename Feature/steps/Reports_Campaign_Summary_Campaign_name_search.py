from selenium.webdriver.support.select import Select
from behave import *
from selenium.webdriver.common.by import By
import time

@then(u'Select Campaign Name from dropdown')
def step_impl(context):
    time.sleep(2)
    entity = context.driver.find_element(By.ID, "camp-report")
    select = Select(entity)
    select.select_by_visible_text("default(2000)")

@then(u'Verify that Campaign Name is same as applied filter')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, "//*[@id='campaign-summary-table']/tbody/tr[2]/td[3]").text
    if text == "default":
        assert True, "Campaign Name is same as applied Filter"
    else:
        assert False, "Campaign Name is different from applied Filter"

