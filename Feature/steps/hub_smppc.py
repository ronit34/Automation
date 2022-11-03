from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

import Tenant_CommomUtility as CU

hubsmppcobj = CU.hub_smppc()

hubsmppcdropdownobj = CU.hub_smppc_dropdown()


@then(u'click on SMPPC')
def step_impl(context):
    context.driver.find_element(By.ID, "smppc_view").click()


@then(u'click on add smppc')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "create_smppc")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'check all the element is present')
def step_impl(context):

    for element_id in hubsmppcobj.hub_smppc_inputbox_list.keys():
        try:
            status = context.driver.find_element(By.ID, element_id).is_displayed()
            print(f"{element_id} --> is {status} ")
        except NameError:
            print(NameError)

    for element_id in hubsmppcdropdownobj.hub_smppc_inputbox_list.keys():
        try:
            status = context.driver.find_element(By.ID, element_id).is_displayed()
            print(f"{element_id} --> is {status} ")
        except NameError:
            print(NameError)


@then(u'insert all the details')
def step_impl(context):

    for element_id in hubsmppcobj.hub_smppc_inputbox_list.keys():
        context.driver.find_element(By.ID, element_id).send_keys(
            hubsmppcobj.hub_smppc_inputbox_list[element_id])
        print(f"{element_id}")

    for element_id in hubsmppcdropdownobj.hub_smppc_inputbox_list.keys():
        try:
            context.driver.implicitly_wait(20)
            element_obj = context.driver.find_element(By.ID, element_id)
            context.driver.implicitly_wait(20)
            select = Select(element_obj)
            context.driver.implicitly_wait(20)
            select.select_by_visible_text(hubsmppcdropdownobj.hub_smppc_inputbox_list[element_id])
        except NameError:
            print(NameError)


@then(u'click on the create button to save smppc details')
def step_impl(context):
    button = context.driver.find_element(By.ID, "save_smppc")
    context.driver.execute_script("arguments[0].click();", button)

    # time.sleep(1)
    # context.driver.close()