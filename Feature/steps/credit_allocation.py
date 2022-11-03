from behave import *
from selenium.webdriver.common.by import By
import time
import CommonUtility as CU

creditallocationObj = CU.credit_allocation()
credit_allocation_labelObj = CU.credit_allocation_label()

@then(u'click on credit allocation')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.driver.find_element(By.ID, "menu_credit_allocation").click()

@then(u'check the credit allocation element should be present')
def step_impl(context):
    for x in creditallocationObj.credit_allocation_inputbox_list:
        try:
            status = context.driver.find_element(By.ID, x).is_displayed()
            print(f"{x} --> is {status} ")
        except NameError:
            print(NameError)

@then(u'discover credit allocation related label')
def step_impl(context):
    for x in credit_allocation_labelObj.credit_allocation_label_inputbox_list:
        context.driver.implicitly_wait(20)
        if context.driver.find_element(By.ID, x).text == credit_allocation_labelObj.credit_allocation_label_inputbox_list[x]:
            print(f"{credit_allocation_labelObj.credit_allocation_label_inputbox_list[x]}--> found")
        else:
            print(f"{credit_allocation_labelObj.credit_allocation_label_inputbox_list[x]}--> Not found")

    # time.sleep(2)
    # context.driver.close()
    
