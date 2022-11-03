import time
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import CommonUtility as CU
phonebook_add_single_contactObj = CU.phonebook_add_single_contact()

phonebook_add_single_contact_inoutObj = CU.phonebook_add_single_contact_inout()

@then(u'click on add contact to create single contact')
def step_impl(context):
    # button = context.driver.find_element(By.ID, "create_contact")
    button = context.driver.find_element(By.ID, "add-contacts")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'check single contact is present')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='addcontact']/div/div/div[2]/div[1]/div/label[1]").is_displayed()


@then(u'click on single contact')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='addcontact']/div/div/div[2]/div[1]/div/label[1]").click()

@then(u'elements are present')
def step_impl(context):
    for x in phonebook_add_single_contactObj.phonebook_add_single_contact_list:
        try:
            status = context.driver.find_element(By.ID, x).is_displayed()
            print(f"{x} --> is {status} ")
        except NameError:
            print(NameError)


@then(u'insert data in single contact field')
def step_impl(context):
    for element_id in phonebook_add_single_contact_inoutObj.phonebook_add_single_contact_inout_list.keys():
        context.driver.find_element(By.ID, element_id).send_keys(
            phonebook_add_single_contact_inoutObj.phonebook_add_single_contact_inout_list[element_id])
        print(f"{element_id}")


    time.sleep(1)
    group = context.driver.find_element(By.ID, "select-group-single")
    select = Select(group)

    select.select_by_visible_text("abc(500)")

    # context.driver.find_element(By.ID, "add").click()


@then(u'click on the Add Button of single contact')
def step_impl(context):
    context.driver.find_element(By.ID, "add").click()
    
    # time.sleep(1)
    # context.driver.close()

