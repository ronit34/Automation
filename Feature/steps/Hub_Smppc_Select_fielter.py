from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

import Tenant_CommomUtility as CU

hub_smppc_dropdown_fillobj = CU.hub_smppc_dropdown_fill()
hub_smppc_dropdown_fill0obj = CU.hub_smppc_dropdown_fill0()

@then(u'Select data')
def step_impl(context):
    time.sleep(1)
    for element_id in hub_smppc_dropdown_fillobj.hub_smppc_dropdown_fill_list.keys():
        context.driver.find_element(By.ID, element_id).send_keys(
            hub_smppc_dropdown_fillobj.hub_smppc_dropdown_fill_list[element_id])
        print(f"{element_id}")

    button = context.driver.find_element(By.ID, "apply_filter")
    context.driver.execute_script("arguments[0].click();", button)
    time.sleep(2)
    context.driver.refresh()

@then(u'select another data')
def step_impl(context):
    time.sleep(2)
    for element_id in hub_smppc_dropdown_fill0obj.hub_smppc_dropdown_fill_list0.keys():
        context.driver.find_element(By.ID, element_id).send_keys(
            hub_smppc_dropdown_fill0obj.hub_smppc_dropdown_fill_list0[element_id])
        print(f"{element_id}")

    button = context.driver.find_element(By.ID, "apply_filter")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[3]/table/tbody/tr[2]/td[1]").text

    if text == ("Total = 0"):
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

    # time.sleep(1)
    # context.driver.close()
