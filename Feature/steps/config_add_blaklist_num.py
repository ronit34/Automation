from behave import *
from selenium.webdriver.common.by import By
import time

import TUC_CommonUtility as CU
Config_ADD_Black_List_NumberObj = CU.Config_ADD_Black_List_Number()

Config_ADD_Black_List_Number_dropdownObj = CU.Config_ADD_Black_List_Number_dropdown()

@then(u'click on Black List Number')
def step_impl(context):
    button = context.driver.find_element(By.ID, "blacklist_num_tab")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check add black list number elements is present')
def step_impl(context):
    for x in Config_ADD_Black_List_NumberObj.Config_ADD_Black_List_Number_list:
        try:
            status = context.driver.find_element(By.ID, x).is_displayed()
            print(f"{x} --> is {status} ")
        except NameError:
            print(NameError)

    for element_id in Config_ADD_Black_List_Number_dropdownObj.Config_ADD_Black_List_Number_dropdown_list.keys():
        try:
            status = context.driver.find_element(By.ID, element_id).is_displayed()
            print(f"{element_id} --> is {status} ")

        except NameError:
            print(NameError)

@then(u'Check add blak list label is present')
def step_impl(context):
    for x in Config_ADD_Black_List_NumberObj.Config_ADD_Black_List_Number_list:
        context.driver.implicitly_wait(20)
        if context.driver.find_element(By.ID, x).text == Config_ADD_Black_List_NumberObj.Config_ADD_Black_List_Number_list[x]:
            print(f"{Config_ADD_Black_List_NumberObj.Config_ADD_Black_List_Number_list[x]}--> found")
        else:
            print(f"{Config_ADD_Black_List_NumberObj.Config_ADD_Black_List_Number_list[x]}--> Not found")

    # time.sleep(1)
    # context.driver.close()