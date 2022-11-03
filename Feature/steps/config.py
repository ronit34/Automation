from behave import *
from selenium.webdriver.common.by import By
import time

import TUC_CommonUtility as CU
ConfigObj = CU.Config()

@then(u'check Config is present')
def config_present(context):
    context.driver.implicitly_wait(20)
    context.driver.find_element(By.ID, "menu_config").is_displayed()

@then(u'click on Config')
def config_click(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "menu_config")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check Config element is present')
def config_element(context):
    for x in ConfigObj.Config_ID_Label_list:
        try:
            status = context.driver.find_element(By.ID, x).is_displayed()
            print(f"{x} --> is {status} ")
        except NameError:
            print(NameError)

@then(u'check Config label is present')
def config_label(context):
    for x in ConfigObj.Config_ID_Label_list:
        context.driver.implicitly_wait(20)
        if context.driver.find_element(By.ID, x).text == ConfigObj.Config_ID_Label_list[x]:
            print(f"{ConfigObj.Config_ID_Label_list[x]}--> found")
        else:
            print(f"{ConfigObj.Config_ID_Label_list[x]}--> Not found")

    # time.sleep(1)
    # context.driver.close()
