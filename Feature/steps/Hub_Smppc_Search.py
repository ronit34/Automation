from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

import Tenant_CommomUtility as CU

hub_smppc_dropdown_fill1obj = CU.hub_smppc_dropdown_fill1()
hub_smppc_dropdown_fill2obj = CU.hub_smppc_dropdown_fill2()

@then(u'search by name')
def step_impl(context):
    time.sleep(1)
    for element_id in hub_smppc_dropdown_fill1obj.hub_smppc_dropdown_fill_list1.keys():
        context.driver.find_element(By.ID, element_id).send_keys(
            hub_smppc_dropdown_fill1obj.hub_smppc_dropdown_fill_list1[element_id])
        print(f"{element_id}")

    button = context.driver.find_element(By.ID, "search_host")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[3]/table/tbody/tr[2]/td[1]").text
    # if (text == "SKV_MTXT_P3/_/_/otp/_(1001)"):
    if text == "SKV_MTXT_P3/N.A./N.A./otp/N.A.(1001)":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"
    time.sleep(2)
    context.driver.refresh()

@then(u'search by systemid')
def step_impl(context):
        for element_id in hub_smppc_dropdown_fill2obj.hub_smppc_dropdown_fill_list2.keys():
            context.driver.find_element(By.ID, element_id).send_keys(
                hub_smppc_dropdown_fill2obj.hub_smppc_dropdown_fill_list2[element_id])
            print(f"{element_id}")

        button = context.driver.find_element(By.ID, "search_host")
        context.driver.execute_script("arguments[0].click();", button)
        time.sleep(1)
        text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[3]/table/tbody/tr[2]/td[1]").text
        # if text == "SKV_MTXT_P3/_/_/otp/_(1001)":
        if text == "SKV_MTXT_P3/N.A./N.A./otp/N.A.(1001)":
            assert True, f"{text} is present"
        else:
            assert False, f"{text} is not present"

        # time.sleep(1)
        # context.driver.close()