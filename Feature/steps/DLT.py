from behave import *
from selenium.webdriver.common.by import By
import time
import CommonUtility as CU
DLTObj = CU.DLT()

@then(u'check DLT is present')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.driver.find_element(By.ID, "menu_manage").is_displayed()

@then(u'click on DLT')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.XPATH, "//*[@id='menu_manage']/p")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check DLT element is present')
def step_impl(context):
    for x in DLTObj.DLT_inputbox_list:
        try:
            status = context.driver.find_element(By.ID, x).is_displayed()
            print(f"{x} --> is {status} ")
        except NameError:
            print(NameError)

@then(u'check DLT label is present')
def step_impl(context):
        for x in DLTObj.DLT_inputbox_list:
            context.driver.implicitly_wait(20)
            if context.driver.find_element(By.ID, x).text == DLTObj.DLT_inputbox_list[x]:
                print(f"{DLTObj.DLT_inputbox_list[x]}--> found")
            else:
                print(f"{DLTObj.DLT_inputbox_list[x]}--> Not found")

        # time.sleep(1)
        # context.driver.close()



