import time
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

@then(u'Select TUC as ICICI')
def step_impl(context):
    tuc = context.driver.find_element(By.ID, "select_tuc")
    select = Select(tuc)
    select.select_by_value("2000")

@then(u'Click on update for transaction of tuc')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, "update_credits").click()

@then(u'check credit alloted successuflly')
def step_impl(context):
    time.sleep(3)
    credit = context.driver.find_element(By.XPATH, "//*[@id='campaign-table']/tbody/tr[2]/td[3]").text
    if (credit == "25,000"):
        assert True, f"{credit} found"
    else:
        assert False, f"{credit} not found"

    # time.sleep(1)
    # context.driver.close()
