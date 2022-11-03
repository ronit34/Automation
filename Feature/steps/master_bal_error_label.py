import time

from behave import *
from selenium.webdriver.common.by import By

# import CommonUtility as CU
# practiseObj = CU.practise()

import CommonUtility as CU
master_bal_error_labelObj = CU.master_bal_error_label()

@then(u'click on master')
def step_impl(context):
    context.driver.find_element(By.ID, "menu_master_balance").click()

@then(u'click on the Update')
def step_impl(context):
    context.driver.find_element(By.ID, "update_balance").click()

@then(u'click on add but')
def step_impl(context):
    context.driver.find_element(By.ID, "add").click()

@then(u'check error lab')
def step_impl(context):
    for y in master_bal_error_labelObj.master_bal_error_label_list:
        try:
            status = context.driver.find_element(By.XPATH, y).is_displayed()
            print(f"{y} --> is {status} ")
        except NameError:
            print(NameError)

    for x in master_bal_error_labelObj.master_bal_error_label_list:
        context.driver.implicitly_wait(20)
        if context.driver.find_element(By.XPATH, x).text == master_bal_error_labelObj.master_bal_error_label_list[x]:
            print(f"{master_bal_error_labelObj.master_bal_error_label_list[x]}--> found")
        else:
            print(f"{master_bal_error_labelObj.master_bal_error_label_list[x]}--> Not found")

    # time.sleep(1)
    # context.driver.close()
