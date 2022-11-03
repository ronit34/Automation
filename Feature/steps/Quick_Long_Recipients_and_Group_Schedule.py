from behave import *
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

import CommonUtility as CU

new_quick_sms_input1Obj = CU.new_quick_sms_input1()

@then(u'select new group1')
def step_impl(context):
    time.sleep(1)
    select = Select(context.driver.find_element(By.ID, "groupDropdown"))
    select.select_by_visible_text('test (22)')