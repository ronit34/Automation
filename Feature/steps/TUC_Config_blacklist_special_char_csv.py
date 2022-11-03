from behave import *
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select


@then(u'Click on Add Blacklist Category')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "add_blacklist")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Insert category name and category description')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.ID, "blacklist-name").send_keys("a")
    context.driver.find_element(By.ID, "blacklist_desc").send_keys("abcd")


@then(u'Click on add button in blacklist category')
def step_impl(context):
    time.sleep(2)
    print("******************************************************************")
    button = context.driver.find_element(By.ID, "create_blacklist")
    context.driver.execute_script("arguments[0].click();", button)
    # context.driver.find_element(By.ID, 'create_blacklist').click()
    print("******************************************************************")


@then(u'Click on blacklist Number')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "blacklist_num_tab")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Click on Upload Blacklist_number')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "update_blacklist")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Choose csv file for blacklist')
def step_impl(context):
    time.sleep(2)
    a = context.driver.switch_to.frame("up_onex_file")
    context.driver.find_element(By.ID, "file1").send_keys("/home/ronit/Desktop/official/Contabo/File format/NameWithSpecialCharacter/campaign@@10.csv")


@then(u'Select Category in blacklist')
def step_impl(context):
    time.sleep(2)
    entity = context.driver.find_element(By.ID, "black_category")
    select = Select(entity)
    select.select_by_visible_text("ab[1323]")


@then(u'Add records to category')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "upload_all")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Click on Ok button in blacklist')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "ok_modal")
    context.driver.execute_script("arguments[0].click();", button)