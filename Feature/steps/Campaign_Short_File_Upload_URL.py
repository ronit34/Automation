import re
from behave import *
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

@then(u'choose numbers file')
def step_impl(context):
    time.sleep(3)
    a = context.driver.switch_to.frame("up_onex_file")
    context.driver.find_element_by_id("file1").send_keys(
        "/home/onexadmin/Downloads/fileFormats/csv_files/10.csv")

@then(u'select a sender id')
def step_impl(context):
    # context.driver.switch()
    time.sleep(1)
    context.driver.switch_to.default_content()
    time.sleep(2)
    button = context.driver.find_element(By.ID, "sender_id")
    context.driver.execute_script("arguments[0].click();", button)
    select = Select(button)
    select.select_by_value("123456")
