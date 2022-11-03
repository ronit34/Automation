import time

from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# @then(u'click on the DLT button')
# def step_impl(context):
#     time.sleep(1)
#     button = context.driver.find_element_by_xpath("//*[@id='menu_manage']/p")
#     context.driver.execute_script("arguments[0].click();", button)

@then(u'check if DLT text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[1]/p[1]").text

    if text == "DLT":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Entity ID text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='entityid_table']/tbody/tr[1]/th[1]").text

    if text == "Entity ID":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if EntityName text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='entityid_table']/tbody/tr[1]/th[2]").text

    if text == "EntityName":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Action text is present or not in dlt entity id')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='entityid_table']/tbody/tr[1]/th[3]").text

    if text == "Action":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'click on add entity id button')
def step_impl(context):
    button = context.driver.find_element_by_id("create_entityid")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check if Add Entity ID text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='myModal']/div/div/div[1]/p[1]").text

    if text == "Add Entity ID":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Entity ID text inside add entity id button is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='myModal']/div/div/div[2]/div[1]/label").text

    if text == "Entity ID*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Entity Name text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='myModal']/div/div/div[2]/div[2]/label").text

    if text == "Entity Name*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

    # time.sleep(1)
    # context.driver.close()