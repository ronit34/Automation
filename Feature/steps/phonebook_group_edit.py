from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
import time

import TUC_CommonUtility as CU

phonebook_group_editobj = CU.phonebook_group_edit()

@then(u'check edit button is present')
def check_edit_button(context):
    time.sleep(1)
    context.driver.find_element_by_css_selector(
        "[title*='Edit']").is_displayed()

@then(u'check edit icon mouse hover text - group')
def check_edit_button(context):
    time.sleep(2)
    action = ActionChains(context.driver);
    parent_level_menu = context.driver.find_element_by_xpath("//*[@id='tab_content']/table/tbody/tr[2]/td[4]/a[1]")
    action.move_to_element(parent_level_menu).perform()

    hover_title = context.driver.find_element_by_xpath("//*[@id='tab_content']/table/tbody/tr[2]/td[4]/a[1]").get_attribute('title')
    if hover_title == "Edit":
        print(f"{hover_title} --> is present")
        print(f"{hover_title} --> is present")
    else:
        assert False, f"{hover_title}--->is not present"

@then(u'click on edit button')
def click_edit_button(context):
    time.sleep(1)
    button = context.driver.find_element_by_css_selector("[title*='Edit']")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check elements are present in Edit Group')
def check_edit_group(context):
    time.sleep(3)
    for x in phonebook_group_editobj.phonebook_group_edit_inputbox_list:
        try:
            status = context.driver.find_element(By.XPATH, x).is_displayed()
            print(f"{x} --> is {status} ")
        except NameError:
            print(NameError)

@then(u'Enter the details into edit group')
def insert_edit_group(context):
    time.sleep(1)
    for element_id in phonebook_group_editobj.phonebook_group_edit_inputbox_list.keys():
        context.driver.find_element(By.XPATH, element_id).clear()
        context.driver.find_element(By.XPATH, element_id).send_keys(
            phonebook_group_editobj.phonebook_group_edit_inputbox_list[element_id])
        print(f"{element_id}")

@then(u'click on update button')
def click_update_button(context):
    time.sleep(1)
    button = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[1]/div[2]/div/div/div/div/div/div[3]/input[2]")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check if group name is updated or not')
def check_group_name(context):
    time.sleep(2)
    # text = context.driver.find_element_by_xpath(
    #                "//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[2]").text
    text = context.driver.find_element_by_xpath(
        "//*[@id='tab_content']/table/tbody/tr[2]/td[1]").text

    if text == "abcd [500]":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if description is updated or not')
def check_description(context):
    # text = context.driver.find_element_by_xpath(
    #           "//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[4]").text
    text = context.driver.find_element_by_xpath(
        "//*[@id='tab_content']/table/tbody/tr[2]/td[3]").text

    if text == "wxyz":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

    # time.sleep(1)
    # context.driver.close()
