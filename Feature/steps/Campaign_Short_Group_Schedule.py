from behave import *
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

@then(u'select test group for dynamic')
def step_impl(context):
    time.sleep(1)
    sender = context.driver.find_element(By.ID, "groupDropdownCamp")
    select = Select(sender)
    select.select_by_visible_text("test (22)")