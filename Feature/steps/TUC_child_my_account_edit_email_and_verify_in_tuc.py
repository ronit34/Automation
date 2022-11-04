import time
from behave import *
from selenium.webdriver.common.by import By


@then(u'Edit Email')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.ID, "profile-email").clear()
    context.driver.find_element(By.ID, "profile-email").send_keys("ronit.patel@onextel.tech")


@then(u'Verify Email')
def step_impl(context):
    time.sleep(2)
    txt = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[4]").text
    if txt == "ronit.patel@onextel.tech":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
