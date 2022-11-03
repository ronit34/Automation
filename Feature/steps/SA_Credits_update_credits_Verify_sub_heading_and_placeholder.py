import time
from behave import *
from selenium.webdriver.common.by import By


@then(u'Click on Update Credits')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "update_credit")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Verify Sub-heading and Placeholder Update Credits')
def step_impl(context):
    time.sleep(2)
    txt = context.driver.find_element(By.XPATH, "//*[@id='myModal']/div/div/div[1]/p[2]").text
    if txt == "Add or deduct credits from the selected account":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"

    credit = context.driver.find_element(By.ID, "credits_amount").get_attribute('placeholder')
    if credit == "Enter Credits":
        assert True, f"{credit}"
    else:
        assert False, f"{credit}"

    remark = context.driver.find_element(By.ID, "credits_remark").get_attribute('placeholder')
    if remark == "Enter Remark":
        assert True, f"{remark}"
    else:
        assert False, f"{remark}"
