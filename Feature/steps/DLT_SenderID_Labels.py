from behave import *
from selenium.webdriver.common.by import By
import time

# @then(u'click on the DLT button')
# def step_impl(context):
#     time.sleep(1)
#     button = context.driver.find_element_by_xpath("//*[@id='menu_manage']/p")
#     context.driver.execute_script("arguments[0].click();", button)

@then(u'click on sender ids tab')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("senderid_tab")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check if Sender ID text is present or not in dlt sender id tab')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='senderid_table']/tbody/tr/th[1]").text

    if text == "Sender ID":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Entity ID text is present or not in dlt sender id tab')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='senderid_table']/tbody/tr/th[2]").text

    if text == "Entity ID":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Approved By text is present or not in dlt sender id tab')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='senderid_table']/tbody/tr[1]/th[3]").text

    if text == "Approved By":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Approved On text is present or not in dlt sender id tab')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='senderid_table']/tbody/tr[1]/th[4]").text

    if text == "Approved On":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Status text is present or not in dlt sender id tab')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='senderid_table']/tbody/tr[1]/th[5]").text

    if text == "Status":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Default text is present or not in dlt sender id tab')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='senderid_table']/tbody/tr[1]/th[6]").text

    if text == "Default":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Action text is present or not in dlt sender id tab')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='senderid_table']/tbody/tr[1]/th[7]").text

    if text == "Action":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'click on add sender id button in dlt sender id tab')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("create_senderid")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check if Add Sender ID text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='myModal']/div/div/div[1]/p[1]").text

    if text == "Add Sender ID":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Sender ID text inside add sender id  is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='myModal']/div/div/div[2]/div[1]/label").text

    if text == "Sender ID*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Select Entity Name text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='myModal']/div/div/div[2]/div[3]/label").text

    if text == "Select Entity Name*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

    # time.sleep(1)
    # context.driver.close()