from behave import *
import time
from selenium.webdriver.common.by import By

import CommonUtility as CU
profile_change_password_editObj = CU.profile_change_password_edit()

@then(u'Edit password')
def step_impl(context):
    for element_id in profile_change_password_editObj.profile_change_password_edit_list.keys():
        context.driver.find_element(By.ID, element_id).send_keys(profile_change_password_editObj.profile_change_password_edit_list[element_id])
        print(f"{element_id}")

@then(u'click on submit request button')
def step_impl(context):
    context.driver.find_element(By.ID, "change-num-email").click()

@then(u'click on log out button to verify change password')
def step_impl(context):
    button = context.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/a")
    context.driver.execute_script("arguments[0].click();", button)

    # time.sleep(1)
    # context.driver.close()







