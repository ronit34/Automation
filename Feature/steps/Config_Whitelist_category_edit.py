from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

@then(u'insert whitelist data')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element_by_id("whitelist_name").send_keys("BOB Cust")
    time.sleep(1)
    context.driver.find_element_by_xpath("//*[@id='whitelist_desc']").send_keys("It's a test Bank category")


@then(u'check edit icon mouse hover text - whitelist')
def check_edit_button(context):
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

@then(u'Click on Edit of the created whitelist category')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.XPATH, "//*[@id='edit']/img")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Enter new whitelist category name to update')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element_by_xpath("//*[@id='whitelist_name']").clear()
    time.sleep(1)
    context.driver.find_element_by_xpath("//*[@id='whitelist_name']").send_keys("SBI Cust")

@then(u'Enter new category description to update')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element_by_xpath("//*[@id='whitelist_desc']").clear()
    time.sleep(1)
    context.driver.find_element_by_xpath("//*[@id='whitelist_desc']").send_keys("Fresh Whitelist Category")

@then(u'Click on update button to update whitelist data')
def step_impl(context):
    button = context.driver.find_element(By.ID, "update_whitelist")
    context.driver.execute_script("arguments[0].click();", button)

    # time.sleep(1)
    # context.driver.close()