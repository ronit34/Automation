import time
from behave import *
from selenium.webdriver.common.by import By


@then(u'Edit Company')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.ID, "profile-company").clear()
    context.driver.find_element(By.ID, "profile-company").send_keys("ONEXTEL")


@then(u'Verify Company')
def step_impl(context):
    time.sleep(2)
    txt = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[6]").text
    if txt == "ONEXTEL":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"