from behave import *
import time
from selenium.webdriver.common.by import By

import CommonUtility as CU
profile_alertObj = CU.profile_alert()

@then(u'click on alert')
def click_aleert(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID,"user-alerts")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check all elment is present in alert')
def cehck_element_present(context):
    for x in profile_alertObj.profile_alert_list:
        try:
            # status = context.driver.find_element(By.NAME, x).is_displayed()
            status = context.driver.find_element(By.XPATH, x).is_displayed()
            print(f"{x} --> is {status} ")
        except NameError:
            print(NameError)

    # time.sleep(1)
    # context.driver.close()