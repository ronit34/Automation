import time
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# @then(u'check if Filter label is present')
# def step_impl(context):
#     time.sleep(4)
#     context.driver.refresh()
#     time.sleep(4)
#     a = context.driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[2]/div/div[1]/label").is_displayed()
#     if a:
#         assert True, f"{a} is present"
#     else:
#         assert False, f"{a} is not present"

# @then(u'check whether Not able to load data! text is present')
# def step_impl(context):
#     time.sleep(1)
#     text = context.driver.find_element_by_id("dlr_content").text
#
#     if text == "Not able to load data!":
#         assert True, f"{text} is present"
#     else:
#         assert False, f"{text} is not present"

@then(u'Check text of Dashboard header')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[1]/p[1]").text

    if text == "Dashboard":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'Check text of Today in graph')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_id("summary_today").text

    if text == "Today":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'Check text of Week in graph')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_id("summary_week").text

    if text == "Week":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'Check text of Month in graph')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_id("summary_month").text

    if text == "Month":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check whether No Scheduled Record Found text is present in Scheduled SMS')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("collapsable_schedule")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='schedule_table']/span").text

    if text == "No Scheduled Record Found":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'Check text of Today')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[5]/div/div[1]/div/p").text

    if text == "Today":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'Check text of Week')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[5]/div/div[2]/div/p").text

    if text == "Week":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'Check text of Month')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[5]/div/div[3]/div/p").text

    if text == "Month":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'Check text of Quick Stats')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[6]/div[1]/div[1]/p").text

    if text == "Quick Stats":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'Check text of Schedule Campaigns')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[6]/div[1]/div[2]/a[2]/div/div/p").text

    if text == "Scheduled Campaigns":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'Check text of Inactive Accounts')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[6]/div[1]/div[2]/div/div/p").text

    if text == "Inactive Accounts":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'Close driver window')
def step_impl(context):
    time.sleep(1)
    context.driver.close()