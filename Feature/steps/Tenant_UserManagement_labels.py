import time
from behave import *
from selenium.webdriver.common.by import By


@then(u'Check for search in userMgmt')
def step_impl(context):
    time.sleep(1)
    txt = context.driver.find_element_by_id("user_search").get_attribute("value")
    if txt == "Search":
        assert True, f"{txt} is present"
    else:
        assert False, f"{txt} is not present"

@then(u'Check for reset in userMgmt')
def step_impl(context):
    txt = context.driver.find_element_by_id("user_reset").get_attribute("value")
    if txt == "Reset":
        assert True, f"{txt} is present"
    else:
        assert False, f"{txt} is not present"

@then(u'Check for Download in userMgmt')
def step_impl(context):
    txt = context.driver.find_element_by_id("dropdownMenuLink").text
    if txt == "Download":
        assert True, f"{txt} is present"
    else:
        assert False, f"{txt} is not present"

@then(u'Check for TUC Name in userMgmt')
def step_impl(context):
    txt = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[2]/table/tbody/tr[1]/th[1]").text
    if txt == "TUC Name":
        assert True, f"{txt} is present"
    else:
        assert False, f"{txt} is not present"

@then(u'Check for Available Credits in userMgmt')
def step_impl(context):
    txt = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[2]/table/tbody/tr[1]/th[2]").text
    if txt == "Available Credits":
        assert True, f"{txt} is present"
    else:
        assert False, f"{txt} is not present"

@then(u'Check for Validity in userMgmt')
def step_impl(context):
    txt = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[2]/table/tbody/tr[1]/th[3]").text
    if txt == "Validity":
        assert True, f"{txt} is present"
    else:
        assert False, f"{txt} is not present"

@then(u'Check for Status in userMgmt')
def step_impl(context):
    txt = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[2]/table/tbody/tr[1]/th[4]").text
    if txt == "Status":
        assert True, f"{txt} is present"
    else:
        assert False, f"{txt} is not present"

@then(u'Check for Creation Time in userMgmt')
def step_impl(context):
    txt = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[2]/table/tbody/tr[1]/th[5]").text
    if txt == "Creation time":
        assert True, f"{txt} is present"
    else:
        assert False, f"{txt} is not present"

@then(u'Check for Action in userMgmt')
def step_impl(context):
    txt = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[2]/table/tbody/tr[1]/th[6]").text
    if txt == "Action":
        assert True, f"{txt} is present"
    else:
        assert False, f"{txt} is not present"

    # time.sleep(1)
    # context.driver.close()