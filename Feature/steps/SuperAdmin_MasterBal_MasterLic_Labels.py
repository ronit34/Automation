from behave import *
from selenium.webdriver.common.by import By
import time

@then(u'click on master balance tab')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element_by_xpath("//*[@id='menu_master_balance']/p").click()

@then(u'check if text Master Balance is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='title']").text

    if text == "Master Balance":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

# @then(u'check if text Current Balance is present or not')
# def step_impl(context):
#     time.sleep(2)
#     text = context.driver.find_element_by_xpath("//*[@id='current_bal_label']").text
#
#     if text == "Current Balance":
#         assert True, f"{text} is present"
#     else:
#         assert False, f"{text} is not present"

@then(u'check if text Current Credits is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='current_bal_label']").text

    if text == "Current Credits":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'click on Super Admin History tab')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element_by_xpath("//*[@id='pills-all-alloc']").click()

@then(u'check if From text is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[1]/div/div[1]/label").text

    if text == "From":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if To text is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[1]/div/div[2]/label").text

    if text == "To":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'click on master licence tab')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element_by_xpath("//*[@id='menu_master_license']/p").click()

@then(u'check if Master License text is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[1]/p[1]").text

    if text == "Master Licenses":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if License text is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr[1]/th[1]").text

    if text == "License":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Total text is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr[1]/th[2]").text

    if text == "Total":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Used text is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr[1]/th[3]").text

    if text == "Used":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Available text is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr[1]/th[4]").text

    if text == "Available":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Action text in master license is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr[1]/th[5]").text

    if text == "Action":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

    # time.sleep(1)
    # context.driver.close()