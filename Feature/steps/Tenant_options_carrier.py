from behave import *
import time
from selenium.webdriver.common.by import By

import Tenant_CommomUtility as CU
options_carrierObj = CU.options_carrier()

@then(u'Click on Carrier tab')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, "option_carrier").click()

@then(u'Click on Add Carrier')
def click_add(context):
    time.sleep(1)
    context.driver.find_element(By.ID, "add_carrier").click()

@then(u'Check elements are present in Carrier')
def check_element(context):
    for x in options_carrierObj.options_carrier_list:
        try:
            status = context.driver.find_element(By.ID, x).is_displayed()
            print(f"{x} --> is {status} ")
        except NameError:
            print(NameError)

@then(u'enter data into Carrier')
def enter_data(context):
    for element_id in options_carrierObj.options_carrier_list.keys():
        context.driver.find_element(By.ID, element_id).send_keys(options_carrierObj.options_carrier_list[element_id])
        print(f"{element_id}")

@then(u'Verify Carrier is added or not')
def check_carrier_add(context):
    carrier = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[1]").text
    if carrier == "AIRTEL":
        assert True, f"Carrier {carrier} Is Added Succesfully"
    else:
        assert False, f"Carrier {carrier} Unable To Add"

    # time.sleep(1)
    # context.driver.close()

