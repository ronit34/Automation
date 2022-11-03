import time
from behave import *
from selenium.webdriver.common.by import By


@then(u'Click on Master Credits')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.XPATH, "//*[@id='menu_master_balance']/p")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Click on Master Update Credits')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "update_balance")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Verify Sub-heading and Placeholder Update Credit')
def step_impl(context):
    time.sleep(2)
    txt = context.driver.find_element(By.ID, "balance_subtitle").text
    if txt == "Update Credits by entering amount below":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"

    credit = context.driver.find_element(By.ID, "amount").get_attribute('placeholder')
    print(credit)
    if credit == "Enter Credits":
        assert True, f"{credit}"
    else:
        assert False, f"{credit}"
