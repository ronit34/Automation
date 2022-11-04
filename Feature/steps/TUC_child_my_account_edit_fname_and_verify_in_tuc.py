import time
from behave import *
from selenium.webdriver.common.by import By


@then(u'Click on Profile')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.XPATH, "//*[@id='profile']/div/p[1]")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Edit First Name')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.ID, "profile-fname").clear()
    context.driver.find_element(By.ID, "profile-fname").send_keys("ronit")


@then(u'Click Ok on Pop-Up')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "ok_modal")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Click on Log Out')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "log-out")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Click on User Management')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.XPATH, "//*[@id='menu_users']/p")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Verify First Name')
def step_impl(context):
    time.sleep(2)
    txt = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[2]").text
    if txt == "ronit":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
