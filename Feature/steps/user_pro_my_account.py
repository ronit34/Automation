from behave import *
import time
from selenium.webdriver.common.by import By

import CommonUtility as CU
profile_my_accountObj = CU.profile_my_account()

@then(u'click on my account')
def click_my_account(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "user-account")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'check all elments are present in my account')
def step_impl(context):
    for x in profile_my_accountObj.profile_my_account_list:
        try:
            status = context.driver.find_element(By.ID, x).is_displayed()
            print(f"{x} --> is {status} ")
        except NameError:
            print(NameError)

@then(u'verify the info present in field as per profile')
def step_impl(context):
    for x in profile_my_accountObj.profile_my_account_list:
        context.driver.implicitly_wait(20)
        if context.driver.find_element(By.ID, x).text == \
                profile_my_accountObj.profile_my_account_list[x]:
            print(f"{profile_my_accountObj.profile_my_account_list[x]}--> found")
        else:
            print(f"{profile_my_accountObj.profile_my_account_list[x]}--> Not found")

@then(u'click on save changes')
def step_impl(context):
    button = context.driver.find_element(By.ID, "save-changes")
    context.driver.execute_script("arguments[0].click();", button)

    # time.sleep(1)
    # context.driver.close()

