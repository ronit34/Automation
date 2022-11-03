from behave import *
from selenium.webdriver.common.by import By
import time

@then(u'click on credits tab')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element_by_xpath("//*[@id='menu_credit_allocation']/p").click()

@then(u'check if text credit is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[4]/div[1]/p[1]").text

    if text == "Credits":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if text Select Tenant/TUC is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[1]/div[1]/div[1]/label").text

    if text == "Select Tenant/TUC":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if text PID/User is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='campaign-table']/tbody/tr/th[1]").text

    # if text == "PID/User":
    if text == "Tenant ID":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if text Name/Company is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='campaign-table']/tbody/tr/th[2]").text

    # if text == "Name/Company":
    if text == "Tenant Name":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

# @then(u'check if text Amount is present or not')
# def step_impl(context):
#     time.sleep(1)
#     text = context.driver.find_element_by_xpath("//*[@id='campaign-table']/tbody/tr/th[3]").text
#
#     if text == "Amount":
#         assert True, f"{text} is present"
#     else:
#         assert False, f"{text} is not present"

@then(u'check if text Credits is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='campaign-table']/tbody/tr/th[3]").text

    if text == "Credits":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if text Allocated by is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='campaign-table']/tbody/tr/th[4]").text

    if text == "Allocated by":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if text Tr Date/Time is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='campaign-table']/tbody/tr/th[5]").text

    if text == "Tr Date/Time":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if text Transaction/Type is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='campaign-table']/tbody/tr/th[6]").text

    if text == "Transaction/Type":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if text Remark is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='campaign-table']/tbody/tr/th[7]").text

    if text == "Remark":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

# @then(u'click on all allocation')
# def step_impl(context):
#     time.sleep(1)
#     context.driver.find_element_by_xpath("//*[@id='pills-all-alloc']").click()

@then(u'check if text From is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[1]/div/div[1]/label").text

    if text == "From":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if text To is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[1]/div/div[2]/label").text

    if text == "To":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

    # time.sleep(1)
    # context.driver.close()