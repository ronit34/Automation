from selenium.webdriver.support.select import Select
from behave import *
from selenium.webdriver.common.by import By
import time

@then(u'Enter Data to create new Entity')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element_by_id("entity_id").send_keys(789)
    time.sleep(1)
    context.driver.find_element_by_id("entity_name").send_keys("Test")


@then(u'Enter New Sender Id "123456"')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element_by_id("sender_name").send_keys(123456)

@then(u'Select new Entity Name')
def step_impl(context):
    entity = context.driver.find_element(By.ID, "sender_entity_id")
    select = Select(entity)
    select.select_by_visible_text("Test(789)")

@then(u'Click on Add button to add sender id')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "add_sender_id")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'Check for Error Message')
def step_impl(context):
    time.sleep(1)
    txt = context.driver.find_element_by_xpath(
        "//*[@id='myModal']/div/div/div[2]/div[2]/span/span").text
    if txt == "Sender Id Already Exists.":
        print(f"{txt} --> Cannot Allocate a SenderID to Multiple EntityID")
        print(f"{txt} --> Cannot Allocate a SenderID to Multiple EntityID")
    else:
        assert False, f"{txt} ---> SenderID allocated to Multiple EntityID"

    # time.sleep(1)
    # context.driver.close()


