from behave import *
from selenium.webdriver.common.by import By
import time

@then(u'Click on Type tab')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element_by_id("option_type").click()


@then(u'check text of Add Type')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='myModal']/div/div/div[1]/p[1]").text

    if text == "Add Type":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text of Type in Atom')
def step_impl(context):

    text = context.driver.find_element_by_xpath("//*[@id='myModal']/div/div/div[2]/div[1]/label").text

    # if text == "Type in Atom":
    if text == "Type in Atom*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text of Type Name')
def step_impl(context):

    text = context.driver.find_element_by_xpath("//*[@id='myModal']/div/div/div[2]/div[2]/label").text

    # if text == "Type Name":
    if text == "Type Name*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check text of add Type Description')
def step_impl(context):

    text = context.driver.find_element_by_xpath("//*[@id='myModal']/div/div/div[2]/div[3]/label").text

    # if text == "Description":
    if text == "Description*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text of Type Add')
def step_impl(context):

    text = context.driver.find_element_by_id("add_option").get_attribute("value")

    if text == "Add":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text Cancel of add Type')
def step_impl(context):

    text = context.driver.find_element_by_id("cancel_modal").get_attribute("value")
    if text == "Cancel":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

    # time.sleep(1)
    # context.driver.close()
