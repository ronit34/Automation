from behave import *
from selenium.webdriver.common.by import By
import time
import CommonUtility as CU

all_allocationObj = CU.all_allocation()

@then(u'click on all allocation')
def step_impl(context):
    context.driver.find_element(By.ID, "pills-all-alloc").click()

@then(u'check all element of all allocation is present')
def step_impl(context):
    for x in all_allocationObj.all_allocation_inputbox_list:
        try:
            status = context.driver.find_element(By.ID, x).is_displayed()
            print(f"{x} --> is {status} ")
        except NameError:
            print(NameError)

    # time.sleep(2)
    # context.driver.close()