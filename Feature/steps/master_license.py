from behave import *
from selenium.webdriver.common.by import By
import time
import CommonUtility as CU

master_licenseobj = CU.master_license()

@then(u'Check the Master License is present')
def step_impl(context):

    context.driver.find_element(By.ID, "menu_master_license").is_displayed()


@then(u'click on master license')
def step_impl(context):
    button = context.driver.find_element(By.ID, "menu_master_license")
    context.driver.execute_script("arguments[0].click();", button)
    # context.driver.find_element(By.ID, "menu_master_license").click()

@then(u'check all elements is present in master license page')
def step_impl(context):
    for x in master_licenseobj.master_license_inputbox_list:
        try:
            status = context.driver.find_element(By.ID, x).is_displayed()
            print(f"{x} --> is {status} ")
        except NameError:
            print(NameError)

    # time.sleep(1)
    # context.driver.close()
