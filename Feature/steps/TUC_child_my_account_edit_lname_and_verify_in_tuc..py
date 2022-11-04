import time
from behave import *
from selenium.webdriver.common.by import By


@then(u'Edit Last Name')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.ID, "profile-lname").clear()
    context.driver.find_element(By.ID, "profile-lname").send_keys("patel")


@then(u'Verify Last Name')
def step_impl(context):
    time.sleep(2)
    txt = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[3]").text
    if txt == "patel":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
