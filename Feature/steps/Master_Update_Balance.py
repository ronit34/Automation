import CommonUtility as CU
from behave import *
from selenium.webdriver.common.by import By
import time

masterupdatebalanceObj = CU.Master_Update_Balance()
masterupdatebalancelabelObj = CU.Master_Update_Balance_label()

@when(u'click on the Master balance')
def click_Master_balance(context):
    context.driver.implicitly_wait(20)
    context.driver.find_element(By.ID, "menu_master_balance").click()

@then(u'click on the Update Balance')
def click_update(context):
    context.driver.find_element(By.ID, "update_balance").click()

@then(u'check the elements should be present')
def step_impl(context):
    for x in masterupdatebalanceObj.Master_Update_Balance_inputbox_list:
        try:
            status = context.driver.find_element(By.XPATH, x).is_displayed()
            print(f"{x} --> is {status} ")
        except NameError:
            print(NameError)


@then(u'discover the all related label')
def step_impl(context):
    for x in masterupdatebalancelabelObj.Master_Update_Balance_label_inputbox_list:
        context.driver.implicitly_wait(20)
        if context.driver.find_element(By.XPATH, x).text == \
                masterupdatebalancelabelObj.Master_Update_Balance_label_inputbox_list[x]:
            print(f"{masterupdatebalancelabelObj.Master_Update_Balance_label_inputbox_list[x]}--> found")
        else:
            print(f"{masterupdatebalancelabelObj.Master_Update_Balance_label_inputbox_list[x]}--> Not found")

    # time.sleep(1)
    # context.driver.close()