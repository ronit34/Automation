from behave import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

import CommonUtility as CU

new_quick_sms_input1Obj = CU.new_quick_sms_group()


@then(u'insert long data into quick sms without recipients')
def step_impl(context):
    for element_id in new_quick_sms_input1Obj.new_quick_sms_group_list.keys():
        context.driver.find_element(By.ID, element_id).send_keys(
            new_quick_sms_input1Obj.new_quick_sms_group_list[element_id])
        print(f"{element_id}")

    time.sleep(1)
    button = context.driver.find_element(By.ID, "insert_template")
    context.driver.execute_script("arguments[0].click();", button)

    # Select Template Type
    button = context.driver.find_element(By.ID, "template_type_id")
    context.driver.execute_script("arguments[0].click();", button)
    select = Select(button)
    select.select_by_value("serv_imp")

    # select template as English short
    time.sleep(1)
    button = context.driver.find_element(By.ID, "template_name")
    context.driver.execute_script("arguments[0].click();", button)
    select = Select(button)
    select.select_by_visible_text("English Long")

    time.sleep(2)
    button = context.driver.find_element(By.ID, "insert_template_to_msg")
    context.driver.execute_script("arguments[0].click();", button)
