import time
from behave import *
from selenium.webdriver.common.by import By


@then(u'Edit Phone Number')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.ID, "profile-phone").clear()
    context.driver.find_element(By.ID, "profile-phone").send_keys("1111122222")


@then(u'Verify Phone Number')
def step_impl(context):
    time.sleep(2)
    txt = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[5]").text
    if txt == "1111122222":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"

