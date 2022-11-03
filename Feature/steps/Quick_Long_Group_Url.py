import re
from behave import *
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import pyperclip

@then(u'select sender id for group')
def step_impl(context):
    time.sleep(1)
    sender = context.driver.find_element(By.ID, "sender_id")
    select = Select(sender)
    select.select_by_value("123456")



@then(u'select test group')
def step_impl(context):
    time.sleep(1)
    sender = context.driver.find_element(By.ID, "groupDropdown")
    select = Select(sender)
    select.select_by_visible_text("test (22)")


