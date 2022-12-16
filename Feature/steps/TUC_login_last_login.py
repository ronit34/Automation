import time
from behave import *
from selenium.webdriver.common.by import By


@then(u'Stored last login time data')
def step_impl(context):
    time.sleep(2)
    context.txt = context.driver.find_element(By.XPATH, "//*[@id='menu-sidebar']/div[2]/div[1]/p[2]").text
    print(context.txt)


@then(u'Verify last login time history')
def step_impl(context):
    time.sleep(2)
    txt = context.driver.find_element(By.XPATH, "//*[@id='campaign-table']/tbody/tr[3]/td[2]").text
    print(txt)
    if txt == context.txt:
        assert True
    else:
        assert False
