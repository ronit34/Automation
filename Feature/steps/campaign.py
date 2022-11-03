from behave import *
from selenium.webdriver.common.by import By
import time
import CommonUtility as CU

campaignObj = CU.campaign()


@then(u'Check Campaign is present')
def campaign_present(context):
    context.driver.implicitly_wait(20)
    context.driver.find_element(By.ID, "menu_campaigns").is_displayed()

@then(u'click on Campaign')
def campaign_click(context):
    context.driver.find_element(By.ID, "menu_campaigns").click()

@then(u'check campaign element is present')
def step_impl(context):
    for x in campaignObj.campaign_inputbox_list:
        try:
            status = context.driver.find_element(By.ID, x).is_displayed()
            print(f"{x} --> is {status} ")
        except NameError:
            print(NameError)


@then(u'check campaign label is present')
def step_impl(context):
    for x in campaignObj.campaign_inputbox_list:
        context.driver.implicitly_wait(20)
        if context.driver.find_element(By.ID, x).text == campaignObj.campaign_inputbox_list[x]:
            print(f"{campaignObj.campaign_inputbox_list[x]}--> found")
        else:
            print(f"{campaignObj.campaign_inputbox_list[x]}--> Not found")

    # time.sleep(1)
    # context.driver.close()

