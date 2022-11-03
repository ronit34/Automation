from behave import *
from selenium.webdriver.common.by import By
import time
import CommonUtility as CU

campaignaddObj = CU.campaign_add()

@then(u'click on add campaign')
def step_impl(context):
    context.driver.find_element(By.ID, "create_campaign").click()

@then(u'check add campaign element is present')
def step_impl(context):
    for x in campaignaddObj.campaign_add_inputbox_list:
        try:
            status = context.driver.find_element(By.ID, x).is_displayed()
            print(f"{x} --> is {status} ")
        except NameError:
            print(NameError)

    # time.sleep(1)
    # context.driver.close()

