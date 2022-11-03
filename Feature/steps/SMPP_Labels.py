from behave import *
from selenium.webdriver.common.by import By
import time
import CommonUtility as CU
SMPPObj = CU.SMPP()

@then(u'check SMPP is present')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.driver.find_element(By.ID, "menu_smpps_view").is_displayed()

@then(u'click on SMPP')
def step_impl(context):
    button = context.driver.find_element(By.ID, "menu_smpps_view")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check element is present on SMPP page')
def step_impl(context):
    for x in SMPPObj.smpp_label_list:
        try:
            status = context.driver.find_element(By.ID, x).is_displayed()
            print(f"{x} --> is {status} ")
        except NameError:
            print(NameError)

@then(u'check labels are present on SMPP page')
def step_impl(context):
    for x in SMPPObj.smpp_label_list:
        context.driver.implicitly_wait(20)
        if context.driver.find_element(By.ID, x).text == SMPPObj.smpp_label_list[x]:
            print(f"{SMPPObj.smpp_label_list[x]}--> found")
        else:
            print(f"{SMPPObj.smpp_label_list[x]}--> Not found")

    # time.sleep(1)
    # context.driver.close()