from behave import *
from selenium.webdriver.common.by import By
import time

import CommonUtility as CU
ApprovalsObj = CU.Approvals()

@then(u'check approvals is present')
def approvals_present(context):
    context.driver.find_element(By.ID, "menu_approvals").is_displayed()

@then(u'Click On Approvals')
def click_approvals(context):
    button = context.driver.find_element(By.ID, "menu_approvals")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'Check all tabs are there')
def check_all_tabs(context):
    for x in ApprovalsObj.Approvals_label_list:
        try:
            status = context.driver.find_element(By.ID, x).is_displayed()
            print(f"{x} --> is {status} ")
        except NameError:
            print(NameError)

@then(u'check all labels of tabs are there')
def check_all_labels(context):
    for x in ApprovalsObj.Approvals_label_list:
        context.driver.implicitly_wait(20)
        if context.driver.find_element(By.ID, x).text == ApprovalsObj.Approvals_label_list[x]:
            print(f"{ApprovalsObj.Approvals_label_list[x]}--> found")
        else:
            print(f"{ApprovalsObj.Approvals_label_list[x]}--> Not found")

    # time.sleep(1)
    # context.driver.close()
