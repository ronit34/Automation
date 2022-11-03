from behave import *
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select


@then(u'click on report_search button')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "pills-search-tab")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Enter Sender_id')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_id("sender_id").send_keys(123456)


@then(u'Click on search_button')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "search")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Check appearing message')
def step_impl(context):
    text = context.driver.find_element_by_id("search_label").text
    if text == "Please enter Sender ID with Mobile":
        time.sleep(2)
        button = context.driver.find_element(By.ID, "reset")
        context.driver.execute_script("arguments[0].click();", button)
    else:
        assert False, f" {text} ----> Not Found"


@then(u'Click on reset_button')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "reset")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Enter mobile and sender_id')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_id("number").send_keys(8605493727)
    time.sleep(2)
    context.driver.find_element_by_id("sender_id").send_keys(123456)


@then(u'Enter UUID')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='search-table']/tbody/tr[2]/td[2]").text
    time.sleep(2)
    context.driver.find_element_by_id("uuid").send_keys(text)


@then(u'Change Source type')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_id("number").send_keys(8605493727)
    time.sleep(2)
    context.driver.find_element_by_id("sender_id").send_keys(123456)
    time.sleep(2)

    time.sleep(2)
    entity = context.driver.find_element(By.ID, "source_type")
    select = Select(entity)
    select.select_by_visible_text("WEB")

@then(u'Click on reset_butt')
def step_impl(context):
    time.sleep(4)
    button = context.driver.find_element(By.ID, "reset")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'Select different tuc')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.ID, "tuc-report").send_keys("ICICI")
    # entity = context.driver.find_element(By.ID, "tuc-report")
    # select = Select(entity)
    # select.select_by_visible_text("ICICI")


@then(u'Set limit to 5')
def step_impl(context):
    time.sleep(2)
    entity = context.driver.find_element(By.ID, "page record_limit")
    select = Select(entity)
    select.select_by_visible_text("5")
