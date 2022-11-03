import time
import CommonUtility as CU

masterbalanceObj = CU.master_balance()
from behave import *
from selenium.webdriver.common.by import By



@when(u'check master balance is present')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.driver.find_element(By.ID, "menu_master_balance").is_displayed()

@then(u'click on master balance')
def step_impl(context):
    context.driver.find_element(By.ID, "menu_master_balance").click()


@then(u'check the element should be present')
def step_impl(context):
    for x in masterbalanceObj.master_balance_inputbox_list:
        try:
            status = context.driver.find_element(By.ID, x).is_displayed()
            print(f"{x} --> is {status} ")
        except NameError:
            print(NameError)


@then(u'discover all related label')
def step_impl(context):
    for x in masterbalanceObj.master_balance_inputbox_list:
        context.driver.implicitly_wait(20)
        if context.driver.find_element(By.ID, x).text == masterbalanceObj.master_balance_inputbox_list[x]:
            print(f"{masterbalanceObj.master_balance_inputbox_list[x]}--> found")
        else:
            print(f"{masterbalanceObj.master_balance_inputbox_list[x]}--> Not found")

    # time.sleep(1)
    # context.driver.close()

