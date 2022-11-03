from behave import *
from selenium.webdriver.common.by import By
import time

import CommonUtility as CU
phonebookObj = CU.phonebook()

@then(u'check phonebook is present')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.driver.find_element(By.ID, "menu_phonebook").is_displayed()

@then(u'click on phonebook')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "menu_phonebook")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check phonebook element is present')
def step_impl(context):
    for x in phonebookObj.phonebook_label_list:
        try:
            status = context.driver.find_element(By.ID, x).is_displayed()
            print(f"{x} --> is {status} ")
        except NameError:
            print(NameError)

@then(u'check phonebook label is present')
def step_impl(context):
    for x in phonebookObj.phonebook_label_list:
        context.driver.implicitly_wait(20)
        if context.driver.find_element(By.ID, x).text == phonebookObj.phonebook_label_list[x]:
            print(f"{phonebookObj.phonebook_label_list[x]}--> found")
        else:
            print(f"{phonebookObj.phonebook_label_list[x]}--> Not found")

    # time.sleep(1)
    # context.driver.close()
