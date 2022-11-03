from behave import *
from selenium.webdriver.common.by import By
import time
import CommonUtility as CU

creditaddObj = CU.credit_add()
creditaddlabelObj = CU.credit_add_label()

@then(u'click on update credit')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "update_credit")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check the credit add element should be present')
def step_impl(context):
    for x in creditaddObj.credit_add_inputbox_list:
        try:
            status = context.driver.find_element(By.ID, x).is_displayed()
            print(f"{x} --> is {status} ")
        except NameError:
            print(NameError)
    context.driver.implicitly_wait(1000)

    # time.sleep(1)
    # context.driver.close()





