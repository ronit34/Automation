from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

import Tenant_CommomUtility as CU
hubgatewayobj = CU.hub_gateway()

hubgatewaydropdownobj = CU.hub_gateway_dropdown()

@then(u'Click on hub')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "menu_hub")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'click on add gateway')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.driver.find_element(By.ID, "create_gateway").click()

@then(u'check element present')
def step_impl(context):

    for element_id in hubgatewayobj.hub_gateway_inputbox_list.keys():
        try:
            status = context.driver.find_element(By.ID, element_id).is_displayed()
            print(f"{element_id} --> is {status} ")
            # print(*element_id, sep=" is present\n")
        except NameError:
            print(NameError)

    for element_id in hubgatewaydropdownobj.hub_gateway_dropdown_inputbox_list.keys():
        try:
            status = context.driver.find_element(By.ID, element_id).is_displayed()
            print(f"{element_id} --> is {status} ")

        except NameError:
            print(NameError)

@then(u'insert the element')
def step_impl(context):

    for element_id in hubgatewayobj.hub_gateway_inputbox_list.keys():
        context.driver.find_element(By.ID, element_id).send_keys(hubgatewayobj.hub_gateway_inputbox_list[element_id])
        print(f"{element_id}")

    for element_id in hubgatewaydropdownobj.hub_gateway_dropdown_inputbox_list.keys():
        try:
            context.driver.implicitly_wait(20)
            element_obj = context.driver.find_element(By.ID, element_id)
            context.driver.implicitly_wait(20)
            select = Select(element_obj)
            context.driver.implicitly_wait(20)
            select.select_by_visible_text(hubgatewaydropdownobj.hub_gateway_dropdown_inputbox_list[element_id])
        except NameError:
            print(NameError)

@then(u'click on the create')
def step_impl(context):
    context.driver.find_element(By.ID, "save_gateway").click()

    # time.sleep(1)
    # context.driver.close()



