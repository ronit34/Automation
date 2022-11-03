from behave import *
from selenium.webdriver.common.by import By
import time

# @then(u'click on url')
# def step_impl(context):
#     context.driver.find_element(By.ID, "url_tab").click()


@then(u'check text of url')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[2]/table/tbody/tr/th[2]").text

    if text == "URL":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check text of url status')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[2]/table/tbody/tr/th[3]").text

    if text == "Status":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check text of url action')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[2]/table/tbody/tr/th[4]").text

    if text == "Action":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

#
# @then(u'click on Add short url')
# def step_impl(context):
#     context.driver.find_element(By.ID, "create_url").click()
#     text = context.driver.find_element_by_xpath(
#         "//*[@id='create_url']").text
#
#     if text == "+ Add Short URL":
#         assert True, f"{text} is present"
#     else:
#         assert False, f"{text} is not present"


@then(u'check text of Add Short URL')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='myModal']/div/div/div[1]/p[1]").text

    if text == "Add Short URL":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check text of url label')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='myModal']/div/div/div[2]/div/label").text

    if text == "URL *":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check text of cancel url')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_id("cancel_modal").get_attribute("value")

    if text == "Cancel":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check text of add url')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_id("add_url").get_attribute("value")

    if text == "Add":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check text inside place holder')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_id("url_name").text

    if text == "":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

    # time.sleep(1)
    # context.driver.close()