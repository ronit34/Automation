import time

from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

@then(u'Select TUC as HDFC')
def step_impl(context):
    tuc = context.driver.find_element(By.ID, "select_tuc")
    select = Select(tuc)
    select.select_by_value("2001")

@then(u'Select Add-Credit for HDFC')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//*[@id='add_credit_div']/label").click()

@then(u'check updated credit is showing or not')
def step_impl(context):
    time.sleep(3)
    credit = context.driver.find_element(By.XPATH, "//*[@id='campaign-table']/tbody/tr[2]/td[3]").text
    if (credit == "2,000"):
        assert True, f"{credit} found"
    else:
        assert False, f"{credit} not found"

    # time.sleep(1)
    # context.driver.close()



