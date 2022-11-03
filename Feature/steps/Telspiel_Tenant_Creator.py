import time
from behave import *
from selenium.webdriver.common.by import By

import Tenant_CommomUtility as CU
telspieltenantcreatorObj = CU.tenant_telspiel_creator()

@then(u'check all element present in super admin')
def step_impl(context):
    for element_id in telspieltenantcreatorObj.tenant_telspiel_creator_inputbox_list.keys():
        try:
            status = context.driver.find_element(By.ID, element_id).is_displayed()
            print(f"{element_id} --> is {status}")
        except NameError:
            print(NameError)

@then(u'insert details in the text box')
def step_impl(context):
    for element_id in telspieltenantcreatorObj.tenant_telspiel_creator_inputbox_list.keys():
        context.driver.find_element(By.ID, element_id).send_keys(
            telspieltenantcreatorObj.tenant_telspiel_creator_inputbox_list[element_id])
        print(f"{element_id}")


@then(u'check Tenant is created successfully or not')
def step_impl(context):
    time.sleep(1)
    tenant = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[2]/table/tbody/tr[3]/td[1]").text
    if (tenant == "Telspiel(11)"):
        assert True, f"{tenant} found"
    else:
        assert False, f"{tenant} not found"

    # time.sleep(1)
    # context.driver.close()