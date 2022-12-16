import time
from behave import *
from selenium.webdriver.common.by import By


@then(u'Click on Add tenant in SA')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "create_tenant")
    context.driver.execute_script("arguments[0].click()", button)


@then(u'Insert details in add tenant in SA for same name')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, "name").send_keys("Onexmedia")
    context.driver.find_element(By.ID, "description").send_keys("Test")
    context.driver.find_element(By.ID, "childtuc").clear()
    time.sleep(1)
    context.driver.find_element(By.ID, "childtuc").send_keys("1")
    context.driver.find_element(By.ID, "smpps").clear()
    time.sleep(1)
    context.driver.find_element(By.ID, "smpps").send_keys("1")
    context.driver.find_element(By.ID, "smsapi").clear()
    time.sleep(1)
    context.driver.find_element(By.ID, "smsapi").send_keys("1")


@then(u'Click on create in add tenant in SA')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "save_tenant")
    context.driver.execute_script("arguments[0].click()", button)


@then(u'Verify tenant create or not in SA')
def step_impl(context):
    txt = "Onexmedia(12)"
    if txt in context.driver.page_source:
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
