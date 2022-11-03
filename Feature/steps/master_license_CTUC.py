from behave import *
from selenium.webdriver.common.by import By
import time
import CommonUtility as CU
master_license_CTUCobj = CU.master_license_CTUC()

@then(u'click on CTUC Update button')
def step_impl(context):
    context.driver.find_element(By.ID, "update_childtuc_license").click()

@then(u'Check CTUC elements are present')
def step_impl(context):
    context.driver.find_element_by_id("value").clear()

    for x in master_license_CTUCobj.master_license_CTUC_inputbox_list:
        try:
            status = context.driver.find_element(By.ID, x).is_displayed()
            print(f"{x} --> is {status} ")
        except NameError:
            print(NameError)

@then(u'enter value to update CTUC "{val}"')
def step_impl(context,val):
    context.driver.find_element(By.ID, "value").send_keys(val)

@then(u'click on add button')
def step_impl(context):
    context.driver.find_element(By.ID, "add").click()

    # time.sleep(1)
    # context.driver.close()
