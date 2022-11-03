from behave import *
import time

from selenium.webdriver import ActionChains


@then(u'check edit icon mouse hover text - Spam_Category')
def check_edit_button(context):
    time.sleep(2)
    action = ActionChains(context.driver);
    parent_level_menu = context.driver.find_element_by_xpath("//*[@id='tab_content']/table/tbody/tr[2]/td[2]/a[1]")
    action.move_to_element(parent_level_menu).perform()

    hover_title = context.driver.find_element_by_xpath("//*[@id='tab_content']/table/tbody/tr[2]/td[2]/a[1]").get_attribute('title')
    if hover_title == "Edit":
        print(f"{hover_title} --> is present")
        print(f"{hover_title} --> is present")
    else:
        assert False, f"{hover_title}--->is not present"

@then(u'click on edit icon against category name')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_xpath("//*[@id='tab_content']/table/tbody/tr[2]/td[2]/a[1]/img")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'edit category name')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_id("spam-cat-name").clear()
    time.sleep(2)
    context.driver.find_element_by_id("spam-cat-name").send_keys("promotes abuse")


@then(u'click Update Btn')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("add")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check updated category name')
def step_impl(context):
    time.sleep(3)
    text = context.driver.find_element_by_xpath("//*[@id='tab_content']/table/tbody/tr[2]/td[1]").text
    if text == "promotes abuse [4008]":
        assert True, "Text Passed"
    else:
        assert False, f" {text} ----> Not Found , category not updated"

    # time.sleep(2)
    # context.driver.close()


