from behave import *
from selenium.webdriver.common.by import By
import time
import CommonUtility as CU
SMPP_SMPPSObj = CU.SMPP_SMPPS_Promo()

@then(u'insert data into SMPPS field for promo')
def step_impl(context):
    for element_id in SMPP_SMPPSObj.SMPP_SMPPS_Promo_inputbox_list.keys():
        context.driver.find_element(By.ID, element_id).send_keys(
            SMPP_SMPPSObj.SMPP_SMPPS_Promo_inputbox_list[element_id])
        print(f"{element_id}")



@then(u'check DND_Filter is selected or not')
def step_impl(context):
    time.sleep(2)
    checkbox = context.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[2]/div/div/div[2]/div/div[1]/div[20]/div/div/div[1]/label/label/input").is_selected()
    if checkbox == True:
        assert True
    else:
        assert False, f"checkbox is not selected"

@then(u'click on create button in SMPPS')
def step_impl(context):
    button = context.driver.find_element(By.ID, "save_smpps")
    context.driver.execute_script("arguments[0].click();", button)

