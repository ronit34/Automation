from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

import CommonUtility as CU

option_type_editobj = CU.Option_Type_edit()

@then(u'check edit button of first Type is present')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[4]/a[1]/img").is_displayed()

@then(u'check edit icon mouse hover text - type')
def check_edit_button(context):
    time.sleep(2)
    action = ActionChains(context.driver);
    parent_level_menu = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[4]/a[1]")
    action.move_to_element(parent_level_menu).perform()

    hover_title = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[4]/a[1]").get_attribute('title')
    if hover_title == "Edit":
        print(f"{hover_title} --> is present")
        print(f"{hover_title} --> is present")
    else:
        assert False, f"{hover_title}--->is not present"


@then(u'click on edit button of first Type is present')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[4]/a[1]/img")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check elements are present in Edit Type')
def step_impl(context):
    time.sleep(3)
    for x in option_type_editobj.Option_Type_edit_inputbox_list:
        try:
            status = context.driver.find_element(By.ID, x).is_displayed()
            print(f"{x} --> is {status} ")
        except NameError:
            print(NameError)


@then(u'Enter the details into edit Type')
def step_impl(context):
    time.sleep(1)
    atom = context.driver.find_element(By.ID, "type_atom")
    select = Select(atom)
    select.select_by_visible_text("simroute")

    for element_id in option_type_editobj.Option_Type_edit_inputbox_list.keys():
        time.sleep(1)
        context.driver.find_element(By.ID, element_id).clear()
        context.driver.find_element(By.ID, element_id).send_keys(
            option_type_editobj.Option_Type_edit_inputbox_list[element_id])
        print(f"{element_id}")

@then(u'click on update button of edit Type')
def step_impl(context):
    time.sleep(5)
    button = context.driver.find_element_by_id("update_option")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'verify the updated Type created or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[1]").text

    # if text == "PROMO":
    if text == "SIM Route":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

    # time.sleep(2)
    # context.driver.close()