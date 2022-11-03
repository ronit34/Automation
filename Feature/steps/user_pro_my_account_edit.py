from behave import *
import time
from selenium.webdriver.common.by import By

import CommonUtility as CU
profile_my_accountObj = CU.profile_my_account()

@then(u'Edit the my account details')
def step_impl(context):
    for element_id in profile_my_accountObj.profile_my_account_list.keys():
        time.sleep(1)
        context.driver.find_element(By.ID, element_id).send_keys(profile_my_accountObj.profile_my_account_list[element_id])
    time.sleep(3)

    button = context.driver.find_element(By.ID, "save-changes")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'click on save changes for saving details')
def step_impl(context):

    time.sleep(1)



