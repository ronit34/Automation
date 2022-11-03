from behave import *
from selenium.webdriver.common.by import By
import time

@then(u'check text of Add Carrier')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='myModal']/div/div/div[1]/p[1]").text

    if text == "Add Carrier":
        print(f"{text} is present")
        print(f"{text} is present")
        # print(f"{text} is present")
        # assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check text of CarrierName')
def step_impl(context):
    text = context.driver.find_element_by_xpath("//*[@id='myModal']/div/div/div[2]/div[1]/label").text

    if text == "Carrier Name*":
        print(f"{text} is present")
        print(f"{text} is present")
        # assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check text of Carrier add Description')
def step_impl(context):

    text = context.driver.find_element_by_xpath(
        "//*[@id='myModal']/div/div/div[2]/div[2]/label").text

    if text == "Description*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check text of Carrier Add')
def step_impl(context):
    text = context.driver.find_element_by_id("add_option").get_attribute("value")

    if text == "Add":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check on Cancel of add Carrier')
def step_impl(context):
    text = context.driver.find_element_by_id("cancel_modal").get_attribute("value")

    if text == "Cancel":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

    # time.sleep(1)
    # context.driver.close()


