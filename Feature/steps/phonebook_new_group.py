from behave import *
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

@then(u'enter group data')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, "group-name").send_keys("test")
    time.sleep(1)
    context.driver.find_element(By.ID, "group-desc").send_keys("Testing")
    time.sleep(1)
    schedule = context.driver.find_element(By.ID, "add")
    context.driver.execute_script("arguments[0].click();", schedule)

@then(u'choose the contacts file to upload')
def step_impl(context):
    time.sleep(2)
    a = context.driver.switch_to.frame("up_onex_file")
    context.driver.find_element_by_id("file1").send_keys(
        "/home/onexadmin/Downloads/fileFormats/csv_files/100.csv")
    time.sleep(3)
    context.driver.switch_to.default_content()

@then(u'select the group')
def step_impl(context):
    time.sleep(1)
    select = Select(context.driver.find_element_by_xpath("//*[@id='select-group-bulk']"))
    select.select_by_visible_text('test(501)')


