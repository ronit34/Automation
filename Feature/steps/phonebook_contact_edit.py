from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

import TUC_CommonUtility as CU

phonebook_contact_editobj = CU.phonebook_contact_edit()

@then(u'check Contacts text is present')
def check_contacts(context):
    time.sleep(1)
    # text = context.driver.find_element_by_id("phonebook_contact").text
    text = context.driver.find_element_by_id("contacts").text
    if text == "Contacts":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'click on contacts tab')
def click_contacts(context):
    time.sleep(1)
    # button = context.driver.find_element_by_id("phonebook_contact")
    button = context.driver.find_element_by_id("contacts")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'select phonebook group')
def step_impl(context):
    time.sleep(2)
    grp = context.driver.find_element(By.ID, "group-select")
    select = Select(grp)
    select.select_by_visible_text("abcd(500)")

@then(u'search')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("search")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check edit button  in contacts tab is present')
def check_edit_button(context):
    time.sleep(1)
    context.driver.find_element_by_css_selector(
        "[title*='Edit']").is_displayed()


@then(u'check edit icon mouse hover text - phonebook')
def check_edit_button(context):
    time.sleep(2)
    action = ActionChains(context.driver);
    # parent_level_menu = context.driver.find_element_by_xpath("//*[@id='contacts-table']/tbody/tr[2]/td[4]/a[1]")
    parent_level_menu = context.driver.find_element_by_xpath("//*[@id='contacts-table']/tbody/tr[2]/td[5]/a[1]/img")
    action.move_to_element(parent_level_menu).perform()

    # hover_title = context.driver.find_element_by_xpath("//*[@id='contacts-table']/tbody/tr[2]/td[4]/a[1]").get_attribute('title')
    hover_title = context.driver.find_element_by_xpath("//*[@id='contacts-table']/tbody/tr[2]/td[5]/a[1]").get_attribute('title')
    if hover_title == "Edit":
        print(f"{hover_title} --> is present")
        print(f"{hover_title} --> is present")
    else:
        assert False, f"{hover_title}--->is not present"

@then(u'click on edit button on contacts tab')
def click_edit_button(context):
    time.sleep(1)
    button = context.driver.find_element_by_css_selector("[title*='Edit']")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check elements are present in Edit Group of contacts tab')
def check_edit_group_ele(context):
    time.sleep(3)
    for x in phonebook_contact_editobj.phonebook_contact_edit_inputbox_list:
        try:
            status = context.driver.find_element(By.XPATH, x).is_displayed()
            print(f"{x} --> is {status} ")
        except NameError:
            print(NameError)

@then(u'Enter the details into edit group of contacts tab')
def enter_details(context):
    time.sleep(1)
    for element_id in phonebook_contact_editobj.phonebook_contact_edit_inputbox_list.keys():
        context.driver.find_element(By.XPATH, element_id).clear()
        context.driver.find_element(By.XPATH, element_id).send_keys(
            phonebook_contact_editobj.phonebook_contact_edit_inputbox_list[element_id])
        print(f"{element_id}")

@then(u'click on update button of contacts tab')
def click_update_button(context):
    time.sleep(1)
    button = context.driver.find_element_by_xpath(
        "//*[@id='addcontact']/div/div/div[3]/input[2]")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check name is updated or not')
def check_name(context):
    time.sleep(1)
    # text = context.driver.find_element_by_xpath("//*[@id='contact-table']/tbody/tr[2]/td[2]").text
    text = context.driver.find_element_by_xpath("//*[@id='contacts-table']/tbody/tr[2]/td[2]").text
    if text == "william":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

    # time.sleep(1)
    # context.driver.close()
