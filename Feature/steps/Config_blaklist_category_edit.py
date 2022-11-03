from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

import TUC_CommonUtility as CU
Config_blacklist_catObj = CU.Config_blacklist_cat()

@then(u'insert black list data')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element_by_id("blacklist-name").send_keys("Test")
    time.sleep(1)
    context.driver.find_element_by_id("blacklist_desc").send_keys("It's a test category")

@then(u'check edit icon mouse hover text - blacklist_category')
def step_impl(context):
    time.sleep(2)
    action = ActionChains(context.driver);
    parent_level_menu = context.driver.find_element_by_xpath("//*[@id='edit']")
    action.move_to_element(parent_level_menu).perform()

    hover_title = context.driver.find_element_by_xpath("//*[@id='edit']").get_attribute('title')
    if hover_title == "Edit":
        print(f"{hover_title} --> is present")
        print(f"{hover_title} --> is present")
    else:
        assert False, f"{hover_title}--->is not present"


@then(u'Click on Edit of the created blacklist category')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.XPATH, "//*[@id='edit']/img")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Enter new category name to update')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element_by_xpath("//*[@id='blacklist_name']").clear()
    time.sleep(1)
    context.driver.find_element_by_xpath("//*[@id='blacklist_name']").send_keys("Fresh")

@then(u'Enter new description to update')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element_by_xpath("//*[@id='blacklist_desc']").clear()
    time.sleep(1)
    context.driver.find_element_by_xpath("//*[@id='blacklist_desc']").send_keys("Fresh Category")

@then(u'Click on update button to update data')
def step_impl(context):
    button = context.driver.find_element(By.ID, "update_blacklist")
    context.driver.execute_script("arguments[0].click();", button)

    # time.sleep(1)
    # context.driver.close()