from behave import *
from selenium.webdriver.common.by import By
import time

import TUC_CommonUtility as CU
Config_WhiteList_catObj = CU.Config_WhiteList_cat()

@then(u'click on White List Category')
def step_impl(context):
    button = context.driver.find_element(By.ID, "whitelist_cat_tab")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'check new Whitelist button is present')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.driver.find_element(By.ID, "add_whitelist").is_displayed()


@then(u'click on new Whitelist button')
def step_impl(context):
    context.driver.find_element(By.ID, "add_whitelist").click()

@then(u'check all elements of White list category is present')
def step_impl(context):
    for x in Config_WhiteList_catObj.Config_WhiteList_cat_list:
        try:
            status = context.driver.find_element(By.XPATH, x).is_displayed()
            print(f"{x} --> is {status} ")
        except NameError:
            print(NameError)


@then(u'insert White list category data')
def step_impl(context):
    for element_id in Config_WhiteList_catObj.Config_WhiteList_cat_list.keys():
        context.driver.find_element(By.XPATH, element_id).send_keys(
            Config_WhiteList_catObj.Config_WhiteList_cat_list[element_id])
        print(f"{element_id}")


@then(u'click on add button of the given page of White list')
def step_impl(context):
    button = context.driver.find_element(By.ID, "create_whitelist")
    context.driver.execute_script("arguments[0].click();", button)

    # time.sleep(1)
    # context.driver.close()
