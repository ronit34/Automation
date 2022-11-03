from behave import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

import CommonUtility as CU

# new_quick_smsObj = CU.new_quick_sms()

new_quick_sms_input1Obj = CU.new_quick_sms_input1()


@then(u'insert long data into quick sms')
def step_impl(context):
    for element_id in new_quick_sms_input1Obj.new_quick_sms_input1_list.keys():
        context.driver.find_element(By.ID, element_id).send_keys(
            new_quick_sms_input1Obj.new_quick_sms_input1_list[element_id])
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


@then(u'click on SEND butn')
def step_impl(context):
    time.sleep(2)
    context.driver.execute_script("window.scrollTo(document.body.scrollHeight, 0)")

    time.sleep(2)
    button = context.driver.find_element(By.ID, "send")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'check allow multipart text for long sms')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='bd-example-modal-lg']/div/div/div[2]/p").text
    time.sleep(2)
    if text == "Message too long, Select Multipart !!!":
        button = context.driver.find_element(By.ID, "ok_modal")
        context.driver.execute_script("arguments[0].click();", button)
        time.sleep(2)
        button = context.driver.find_element(By.NAME, "multipart_check")
        context.driver.execute_script("arguments[0].click();", button)
        time.sleep(1)
        button = context.driver.find_element(By.ID, "send")
        context.driver.execute_script("arguments[0].click();", button)


@then(u'check change in credits after sms is sent "{verify}"')
def step_impl(context,verify):
    time.sleep(3)
    creds = context.driver.find_element_by_xpath("//*[@id='available_credits']").text
    credits = int(creds.replace(',', ''))

    time.sleep(2)
    button = context.driver.find_element(By.ID, "confirm_send_sms")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    button = context.driver.find_element(By.ID, "confirm_send_sms")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(2)
    creds_new = context.driver.find_element_by_xpath("//*[@id='available_credits']").text
    updated_creds = int(creds_new.replace(',', ''))
    verify_creds = int(verify)
    check = credits - updated_creds

    print(f"Credit before sending sms ---> {credits}")
    print(f"Credit after sending sms ---> {updated_creds}")
    print(f"Difference in Credits ---> {check}")

    if (check == verify_creds):
        print(f"{check} ---> Credit deduction is correct")
        print(f"{check} ---> Credit deduction is correct")
    else:
        assert False, print(f"{check} ---> Credit deduction is wrong")

    # time.sleep(1)
    # context.driver.close()
