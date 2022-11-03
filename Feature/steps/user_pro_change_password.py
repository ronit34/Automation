from behave import *
import time
from selenium.webdriver.common.by import By

import CommonUtility as CU
profile_change_passwordObj = CU.profile_change_password()


@then(u'click on change password')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='profiledropdown']/li[3]/a").click()


@then(u'check all elment is present in change password')
def step_impl(context):
    for x in profile_change_passwordObj.profile_change_password_list:
        try:
            status = context.driver.find_element(By.ID, x).is_displayed()
            print(f"{x} --> is {status} ")
        except NameError:
            print(NameError)

    # time.sleep(1)
    # context.driver.close()
