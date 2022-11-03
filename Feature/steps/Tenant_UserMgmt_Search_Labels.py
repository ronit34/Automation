from behave import *
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

@then(u'Click on Search btn in UserMgmt')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("search")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'Select TUCID in UserMgmt')
def step_impl(context):
    time.sleep(1)
    entity = context.driver.find_element(By.ID, "select_type")
    select = Select(entity)
    select.select_by_visible_text("Tuc ID")

@then(u'Enter TUCID')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_id("enter_type").send_keys("2000")

@then(u'Click Search')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("search_type")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'Check for TUC Hierarchy')
def step_impl(context):
    txt = context.driver.find_element_by_id("tuc_search_header").text

    if txt == "TUC Hierarchy(2000)":
        assert True, f"{txt} is present"
    else:
        assert False, f"{txt} is not present"

@then(u'Check for Name in UserMgmt')
def step_impl(context):
    txt = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[2]/div/table/tbody/tr[1]/th[1]").text

    if txt == "Name":
        assert True, f"{txt} is present"
    else:
        assert False, f"{txt} is not present"

@then(u'Check for Credits')
def step_impl(context):
    txt = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[2]/div/table/tbody/tr[1]/th[2]").text
    if txt == "Credits":
        assert True, f"{txt} is present"
    else:
        assert False, f"{txt} is not present"

@then(u'Check for Bill Type')
def step_impl(context):
    txt = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[2]/div/table/tbody/tr[1]/th[3]").text
    if txt == "Bill Type":
        assert True, f"{txt} is present"
    else:
        assert False, f"{txt} is not present"

@then(u'Check for DLT Charge')
def step_impl(context):
    txt = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[2]/div/table/tbody/tr[1]/th[4]").text
    if txt == "DLT Charge":
        assert True, f"{txt} is present"
    else:
        assert False, f"{txt} is not present"

@then(u'Check for SMS Charge')
def step_impl(context):
    txt = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[2]/div/table/tbody/tr[1]/th[5]").text
    if txt == "SMS Charge":
        assert True, f"{txt} is present"
    else:
        assert False, f"{txt} is not present"

    # time.sleep(1)
    # context.driver.close()