import time
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import CommonUtility as CU
select_groupObj = CU.select_group()

@then(u'click on select group and select contact')
def step_impl(context):
    time.sleep(1)
    # button = context.driver.find_element(By.ID, "select_group")
    button = context.driver.find_element(By.ID, "group-select")
    context.driver.execute_script("arguments[0].click();", button)

    select = Select(button)
    select.select_by_visible_text("abcd(500)")

    time.sleep(1)
    button = context.driver.find_element(By.ID, "search")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check contact is showing')
def step_impl(context):
    for x in select_groupObj.select_group_list:
        context.driver.implicitly_wait(20)
        if context.driver.find_element(By.XPATH, x).text == select_groupObj.select_group_list[x]:
            print(f"{select_groupObj.select_group_list[x]}--> found")
        else:
            print(f"{select_groupObj.select_group_list[x]}--> Not found")

    # time.sleep(1)
    # context.driver.close()