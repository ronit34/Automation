from behave import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

import CommonUtility as CU
new_quick_smsObj = CU.new_quick_sms()

new_quick_sms_inputObj = CU.new_quick_sms_input()

@then(u'click on quick sms')
def step_impl(context):
    button = context.driver.find_element(By.ID, "quick_sms_page_link")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check all elements are present in quick sms')
def step_impl(context):
    for x in new_quick_smsObj.new_quick_sms_list:
        try:
            status = context.driver.find_element(By.ID, x).is_displayed()
            print(f"{x} --> is {status} ")
        except NameError:
            print(NameError)

@then(u'check some labels are presents')
def step_impl(context):
    for x in new_quick_smsObj.new_quick_sms_list:
        context.driver.implicitly_wait(20)
        if context.driver.find_element(By.ID, x).text == new_quick_smsObj.new_quick_sms_list[x]:
            print(f"{new_quick_smsObj.new_quick_sms_list[x]}--> found")
        else:
            print(f"{new_quick_smsObj.new_quick_sms_list[x]}--> Not found")

@then(u'insert data into quick sms')
def step_impl(context):
    for element_id in new_quick_sms_inputObj.new_quick_sms_input_list.keys():
        context.driver.find_element(By.ID, element_id).send_keys(
            new_quick_sms_inputObj.new_quick_sms_input_list[element_id])
        print(f"{element_id}")

    # click on Insert Template template_name
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
    select.select_by_visible_text("English Short")

    time.sleep(2)
    button = context.driver.find_element(By.ID, "insert_template_to_msg")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'click on send button')
def step_impl(context):
    # click on send button
    time.sleep(1)
    button = context.driver.find_element(By.ID, "send")
    context.driver.execute_script("arguments[0].click();", button)
    # click on multipart SMS
    time.sleep(2)
    try:
        if (context.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[4]/div[1]/div/div/div/div[1]/div[1]/div/div/div/div[2]/p").text== "Message too long, Select Multipart !!!"):
            time.sleep(1)
            button = context.driver.find_element(By.ID, "ok_modal")
            context.driver.execute_script("arguments[0].click();", button)
            time.sleep(1)
            button = context.driver.find_element(By.NAME, "multipart_check")
            context.driver.execute_script("arguments[0].click();", button)
            time.sleep(1)
            button = context.driver.find_element(By.ID, "send")
            context.driver.execute_script("arguments[0].click();", button)
        else:
            print(f"Message is short no required for multipart")
            print(f"Message is short no required for multipart")
    except NoSuchElementException:
        print(f"Message is short no required for multipart")

@then(u'check pop up window is coming')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.ID, "confirm_send_sms").is_displayed()

    # time.sleep(1)
    # context.driver.close()
