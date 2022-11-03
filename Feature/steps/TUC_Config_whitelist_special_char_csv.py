from behave import *
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select


@then(u'Click on Whitelist Category')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "whitelist_cat_tab")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Click on Add Whitelist Category')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "add_whitelist")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Insert category name and category description in whitelist')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.ID, "whitelist_name").send_keys("abc3")
    context.driver.find_element(By.ID, "whitelist_desc").send_keys("abcd")


@then(u'Click on add button in whitelist category')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "create_whitelist")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Click on whitelist Number')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "whitelist_num_tab")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Click on Upload Whitelist_number')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "update_whitelist")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Choose csv file for whitelist')
def step_impl(context):
    time.sleep(2)
    a = context.driver.switch_to.frame("up_onex_file")
    context.driver.find_element(By.ID, "file1").send_keys(
        "/home/ronit/Desktop/official/Contabo/File format/NameWithSpecialCharacter/campaign@@10.csv")


@then(u'Select Category in whitelist')
def step_impl(context):
    time.sleep(2)
    entity = context.driver.find_element(By.ID, "whitelist_category")
    select = Select(entity)
    select.select_by_visible_text("abc3[1328]")


@then(u'Click on Ok button in whitelist')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "ok_modal")
    context.driver.execute_script("arguments[0].click();", button)