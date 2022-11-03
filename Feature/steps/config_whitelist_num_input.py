from behave import *
from selenium.webdriver.common.by import By
import time

import TUC_CommonUtility as CU
Config_White_List_Number_inputObj = CU.Config_White_List_Number_input()

Config_White_List_Number_dropdown_inputObj = CU.Config_White_List_Number_dropdown_input()

@then(u'insert data on the given page of white list number')
def step_impl(context):
    for element_id in Config_White_List_Number_inputObj.Config_White_List_Number_input_list.keys():
        context.driver.find_element(By.ID, element_id).send_keys(
            Config_White_List_Number_inputObj.Config_White_List_Number_input_list[element_id])
        print(f"{element_id}")

    for element_id in Config_White_List_Number_dropdown_inputObj.Config_White_List_Number_dropdown_input_list.keys():
        context.driver.find_element(By.ID, element_id).send_keys(
            Config_White_List_Number_dropdown_inputObj.Config_White_List_Number_dropdown_input_list[element_id])
        print(f"{element_id}")


@then(u'click on add button of the given page of white list number')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID,"add")
    context.driver.execute_script("arguments[0].click();", button)

    # time.sleep(1)
    # context.driver.close()