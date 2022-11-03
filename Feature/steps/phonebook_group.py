import time

from behave import *
from selenium.webdriver.common.by import By

import CommonUtility as CU
phonebook_groupObj = CU.phonebook_group()

@then(u'click on Add group')
def step_impl(context):
    # button = context.driver.find_element(By.ID, "create_group")
    button = context.driver.find_element(By.ID, "add-group")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check add group element is present in phonebook')
def step_impl(context):
    for x in phonebook_groupObj.phonebook_group_inputbox_list:
        try:
            status = context.driver.find_element(By.ID, x).is_displayed()
            print(f"{x} --> is {status} ")
        except NameError:
            print(NameError)


@then(u'insert add group element in phonebook')
def step_impl(context):

    for element_id in phonebook_groupObj.phonebook_group_inputbox_list.keys():
        context.driver.find_element(By.ID, element_id).send_keys(
            phonebook_groupObj.phonebook_group_inputbox_list[element_id])
        print(f"{element_id}")

    context.driver.find_element(By.ID, "add").click()

    # time.sleep(1)
    # context.driver.close()

