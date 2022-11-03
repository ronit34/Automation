import time

from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then(u'click on the DLT button')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_xpath("//*[@id='menu_manage']/p")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'click on Bulk Upload tab')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_xpath("//*[@id='bulktemplate_tab']")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check if Entity ID is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='bulk-entity-title']").text

    if text == "Entity ID *":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Operator is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='bulk-operator-title']").text

    if text == "Operator*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Reset button text is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='bulk-cancel']").get_attribute('value')

    if text == "Reset":
        assert True, "Test Passed"
    else:
        assert False, "Test Failed"

@then(u'check if Save Templates text is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='bulk-save']").get_attribute('value')

    if text == "Save Templates":
        assert True, "Test Passed"
    else:
        assert False, "Test Failed"

    # time.sleep(1)
    # context.driver.close()