from behave import *
from selenium.webdriver.common.by import By
import time
import CommonUtility as CU
SMPP_SMPPSObj = CU.SMPP_SMPPS()

@then(u'click on add SMPPS button')
def step_impl(context):
    button = context.driver.find_element(By.ID, "create_smpps")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'check all elements are present in SMPPS')
def step_impl(context):
    for x in SMPP_SMPPSObj.SMPP_SMPPS_inputbox_list:
        try:
            status = context.driver.find_element(By.ID, x).is_displayed()
            print(f"{x} --> is {status} ")
        except NameError:
            print(NameError)


@then(u'insert data into SMPPS field')
def step_impl(context):
    for element_id in SMPP_SMPPSObj.SMPP_SMPPS_inputbox_list.keys():
        context.driver.find_element(By.ID, element_id).send_keys(
            SMPP_SMPPSObj.SMPP_SMPPS_inputbox_list[element_id])
        print(f"{element_id}")

@then(u'click on create button to create SMPPS')
def step_impl(context):
    button = context.driver.find_element(By.ID, "save_smpps")
    context.driver.execute_script("arguments[0].click();", button)

    # time.sleep(1)
    # context.driver.close()
