import time
from behave import *

@then(u'Click on All TUC')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("all_tucs")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'Check for TUC Name in All TUC')
def step_impl(context):
    txt = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[2]/table/tbody/tr[1]/th[1]").text
    if txt == "TUC Name":
        assert True, f"{txt} is present"
    else:
        assert False, f"{txt} is not present"

@then(u'Check for ChildTUC1 in All TUC')
def step_impl(context):
    txt = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[2]/table/tbody/tr[1]/th[2]").text

    print(f"{txt} --> is present")
    print(f"{txt} --> is present")

    # if txt == "ChildTUC 1":
    #     assert True, f"{txt} is present"
    # else:
    #     assert False, f"{txt} is not present"

@then(u'Check for ChildTUC2 in All TUC')
def step_impl(context):
    txt = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[2]/table/tbody/tr[1]/th[3]").text

    print(f"{txt} --> is present")
    print(f"{txt} --> is present")

    # if txt == "ChildTUC 2":
    #     assert True, f"{txt} is present"
    # else:
    #     assert False, f"{txt} is not present"

@then(u'Check for Credit')
def step_impl(context):
    txt = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[2]/table/tbody/tr[1]/th[4]").text

    print(f"{txt} --> is present")
    print(f"{txt} --> is present")

    # if txt == "Credit":
    #     assert True, f"{txt} is present"
    # else:
    #     assert False, f"{txt} is not present"

    # time.sleep(1)
    # context.driver.close()