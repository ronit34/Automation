import label as label
from behave import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

import CommonUtility as CU
new_quick_smsObj = CU.new_quick_sms()

new_quick_sms_Promo_inputbj = CU.new_quick_sms_Promo_input()


# @then(u'insert data for promo quick')
# def step_impl(context):
#     for element_id in new_quick_sms_Promo_inputbj.new_quick_sms_Promo_input1_list.keys():
#         context.driver.find_element(By.ID, element_id).send_keys(
#             new_quick_sms_Promo_inputbj.new_quick_sms_Promo_input1_list[element_id])
#         print(f"{element_id}")



@then(u'select Promo template for unicode')
def step_impl(context):
    # click on Insert Template template_name
    time.sleep(1)
    button = context.driver.find_element(By.ID, "insert_template")
    context.driver.execute_script("arguments[0].click();", button)

    # Select Template Type
    button = context.driver.find_element(By.ID, "template_type_id")
    context.driver.execute_script("arguments[0].click();", button)
    select = Select(button)
    select.select_by_value("promo")

    # select template as English short
    time.sleep(1)
    button = context.driver.find_element(By.ID, "template_name")
    context.driver.execute_script("arguments[0].click();", button)
    select = Select(button)
    select.select_by_visible_text("Promo Hindi")

    time.sleep(2)
    button = context.driver.find_element(By.ID, "insert_template_to_msg")
    context.driver.execute_script("arguments[0].click();", button)
