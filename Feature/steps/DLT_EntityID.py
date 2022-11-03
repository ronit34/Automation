from behave import *
from selenium.webdriver.common.by import By
import time

import CommonUtility as CU
DLT_entityIDObj = CU.DLT_entityID()

@then(u'Click on Add Entity button')
def step_impl(context):
    context.driver.find_element(By.ID, "create_entityid").click()

@then(u'Check DLT Entity element is present')
def step_impl(context):
    for x in DLT_entityIDObj.DLT_entityID_inputbox_list:
        try:
            status = context.driver.find_element(By.ID, x).is_displayed()
            print(f"{x} --> is {status} ")
        except NameError:
            print(NameError)

@then(u'Insert data into entity fields')
def step_impl(context):
    for element_id in DLT_entityIDObj.DLT_entityID_inputbox_list.keys():
        context.driver.find_element(By.ID, element_id).send_keys(
            DLT_entityIDObj.DLT_entityID_inputbox_list[element_id])
        print(f"{element_id}")

@then(u'click on add button to add entity')
def step_impl(context):
    context.driver.find_element(By.ID, "add_entityid").click()

@then(u'Check entity id is created or not')
def entity(context):
    time.sleep(1)
    entity = context.driver.find_element(By.XPATH, "//*[@id='entityid_table']/tbody/tr[2]/td[1]").text
    if (entity == "123"):
        assert True, f"{entity} found"
    else:
        assert False, f"{entity} not found"

    # time.sleep(2)
    # context.driver.close()

