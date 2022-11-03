from behave import *
from selenium.webdriver.common.by import By
import time

import TUC_CommonUtility as CU
Config_blacklist_catObj = CU.Config_blacklist_cat()

# @then(u'click on Black List Category')
# def click_blc(context):
#     # context.driver.implicitly_wait(20)
#     button = context.driver.find_element(By.ID, "menu_blacklist_category")
#     context.driver.execute_script("arguments[0].click();", button)
#     context.driver.find_element(By.ID, "menu_blacklist_category").click()


@then(u'check new blacklist button is present')
def check_nblb(context):
    context.driver.implicitly_wait(20)
    button=context.driver.find_element(By.ID, "add_blacklist").is_displayed()
    if button:
        assert True, f"{button} found"
    else:
        assert False, f"{button} not found"

@then(u'click on new blacklist button')
def click_nblb(context):
    context.driver.find_element(By.ID, "add_blacklist").click()

@then(u'check all elements of blak list catefgory is present')
def check_all_element(context):
    for x in Config_blacklist_catObj.Config_blacklist_cat_list:
        try:
            status = context.driver.find_element(By.XPATH, x).is_displayed()
            print(f"{x} --> is {status} ")
        except NameError:
            print(NameError)

@then(u'insert blak list catefgory data')
def insert_data(context):
    for element_id in Config_blacklist_catObj.Config_blacklist_cat_list.keys():
        context.driver.find_element(By.XPATH, element_id).send_keys(
            Config_blacklist_catObj.Config_blacklist_cat_list[element_id])
        print(f"{element_id}")

@then(u'click on add button of the given page')
def click_add(context):
    button = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[1]/div[2]/div/div/div/div[3]/input[2]")
    context.driver.execute_script("arguments[0].click();", button)

    # time.sleep(1)
    # context.driver.close()

