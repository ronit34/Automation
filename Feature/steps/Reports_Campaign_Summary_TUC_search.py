from behave import *
from selenium.webdriver.common.by import By
import time

@then(u'Enter Specific TUC to see data')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.ID, "tuc-report").send_keys("IC")
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//*[@id='ui-id-2']").click()

@then(u'Verify that TUC Name is same as applied filter')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, "//*[@id='campaign-summary-table']/tbody/tr[2]/td[2]").text
    if text == "ICICI":
        assert True, "TUC Name is same as applied Filter"
    else:
        assert False, "TUC Name is different from applied Filter"

@then(u'Verify that TUC ID is same as applied filter')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, "//*[@id='campaign-summary-table']/tbody/tr[2]/td[1]").text
    if text == "2000":
        assert True, "TUC Name is same as applied Filter"
    else:
        assert False, "TUC Name is different from applied Filter"

