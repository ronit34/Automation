import time
from behave import *
from selenium.webdriver.common.by import By

import CommonUtility as CU
phonebook_contactObj = CU.phonebook_contact()

@then(u'click on contact')
def step_impl(context):
    # button = context.driver.find_element(By.ID, "phonebook_contact")
    button = context.driver.find_element(By.ID, "contacts")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check contact elements are present')
def step_impl(context):
    for x in phonebook_contactObj.phonebook_contact_label_list:
        try:
            status = context.driver.find_element(By.ID, x).is_displayed()
            print(f"{x} --> is {status} ")
        except NameError:
            print(NameError)

@then(u'check contact labels are present')
def step_impl(context):
    for x in phonebook_contactObj.phonebook_contact_label_list:
        context.driver.implicitly_wait(20)
        if context.driver.find_element(By.ID, x).text == phonebook_contactObj.phonebook_contact_label_list[x]:
            print(f"{phonebook_contactObj.phonebook_contact_label_list[x]}--> found")
        else:
            print(f"{phonebook_contactObj.phonebook_contact_label_list[x]}--> Not found")

    # time.sleep(1)
    # context.driver.close()