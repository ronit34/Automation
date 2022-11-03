from behave import *
from selenium.webdriver.common.by import By
import time

@then(u'Click on URL of tenant')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, "menu_url_tnt").click()

@then(u'Check text of  url tenant')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[2]/table/tbody/tr/th[2]").text

    if text == "URL":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'Check text of  status tenant')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[2]/table/tbody/tr/th[3]").text

    if text == "Status":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'Check text of  action tenant')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[2]/table/tbody/tr/th[4]").text

    if text == "Action":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'click on add short URl button to add URL')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, "create_url").click()

@then(u'enter url of tenant')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element_by_id("url_name").send_keys("google.com")

@then(u'click on ad')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element_by_id("add_url").click()

@then(u'enter new url of tenant')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element_by_id("url_name").send_keys("facebook.com")

@then(u'Check entered URL is created or not')
def step_impl(context):
    time.sleep(1)
    entity = context.driver.find_element(By.XPATH,
                "//*[@id='pills-campaign']/div[2]/table/tbody/tr[3]/td[2]").text
    if (entity == "google.com"):
        assert True, f"{entity} found"
    else:
        assert False, f"{entity} not found"

    # time.sleep(1)
    # context.driver.close()

