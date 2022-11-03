import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@then(u'insert detail')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, "name").send_keys("Ronit")
    context.driver.find_element(By.ID, "description").send_keys("abcd")
    context.driver.find_element(By.ID, "childtuc").send_keys("abcd")
    context.driver.find_element(By.ID, "smpps").send_keys("abcd")
    context.driver.find_element(By.ID, "smsapi").send_keys("abcd")


@then(u'Check Licenses labels are error or not')
def step_impl(context):
    time.sleep(1)
    txt = context.driver.find_element(By.ID, "childtucpanel1").text
    print(txt)
    if txt == "Child TUC* (9499) Number Required":
        assert True, "Character not supported"
    else:
        assert False, "Character not supported"
