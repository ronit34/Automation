from selenium.webdriver.support.select import Select
from behave import *
from selenium.webdriver.common.by import By
import time

@then(u'click on scheduled campaigns tab in report')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "pills-campaign-tab")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'click on Search Button in scheduled campaigns')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("search")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'Check for campaign name appearing')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, "//*[@id='campaign-summary-table']/tbody/tr[2]/td[3]").text

    if text == "RCF":
        assert True, "Campaign Name is --> RCF"
    else:
        assert False, "Campaign Name is different than RCF"

@then(u'Select Campaign Name filter from dropdown')
def step_impl(context):
    time.sleep(2)
    entity = context.driver.find_element(By.ID, "camp-report")
    select = Select(entity)
    select.select_by_visible_text("default(2000)")
