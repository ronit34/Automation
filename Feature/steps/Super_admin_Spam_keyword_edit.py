from behave import *
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select


@then(u'Select Category in keyword tab')
def step_impl(context):
    time.sleep(2)
    select = Select(context.driver.find_element_by_xpath('//*[@id="spam-cat-select"]'))
    select.select_by_visible_text('promotes abuse(4009)')


@then(u'Click   Search')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("search")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'check edit icon mouse hover text - keyword')
def check_edit_button(context):
    time.sleep(2)
    action = ActionChains(context.driver);
    parent_level_menu = context.driver.find_element_by_xpath("//*[@id='contacts-table']/tbody/tr[2]/td[2]/a[1]")
    action.move_to_element(parent_level_menu).perform()

    hover_title = context.driver.find_element_by_xpath("//*[@id='contacts-table']/tbody/tr[2]/td[2]/a[1]").get_attribute('title')
    if hover_title == "Edit":
        print(f"{hover_title} --> is present")
        print(f"{hover_title} --> is present")
    else:
        assert False, f"{hover_title}--->is not present"


@then(u'click on edit icon in keyword')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_xpath("//*[@id='contacts-table']/tbody/tr[2]/td[2]/a[1]")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'edit spam keyword')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_id("spam-cat-name").clear()
    time.sleep(2)
    context.driver.find_element_by_id("spam-cat-name").send_keys("bloodshed")


@then(u'check keyword updated or not')
def step_impl(context):
    text = context.driver.find_element_by_xpath(
        "//*[@id='contacts-table']/tbody/tr[2]/td[1]").text
    if text == "bloodshed":
        assert True, "Text Passed"
    else:
        assert False, f" {text} ----> Not Found"

    # time.sleep(2)
    # context.driver.close()
