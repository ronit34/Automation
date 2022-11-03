from behave import *
import time
from selenium.webdriver.common.by import By

import CommonUtility as CU
profile_alertObj = CU.profile_alert()

@then(u'click on all checkbox present in alret')
def step_impl(context):
    for x in profile_alertObj.list_edit:
        try:
            time.sleep(2)
            status = context.driver.find_element(By.NAME, x)
            context.driver.execute_script("arguments[0].click();", status)
            print(f"{x} --> is {status} ")
        except NameError:
            print(NameError)

    # time.sleep(1)
    # context.driver.close()