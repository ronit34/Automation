from behave import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

import CommonUtility as CU
new_unicode_sms_inputObj = CU.new_unicode_sms_input()

@then(u'insert data into Unicode sms')
def step_impl(context):
    for element_id in new_unicode_sms_inputObj.new_unicode_sms_input_list.keys():
        context.driver.find_element(By.ID, element_id).send_keys(
            new_unicode_sms_inputObj.new_unicode_sms_input_list[element_id])
        print(f"{element_id}")

    # click on Insert Template template_name
    time.sleep(2)
    button = context.driver.find_element(By.ID, "insert_template")
    context.driver.execute_script("arguments[0].click();", button)

    # Select Template Type
    time.sleep(2)
    button = context.driver.find_element(By.ID, "template_type_id")
    context.driver.execute_script("arguments[0].click();", button)
    select = Select(button)
    select.select_by_value("serv_imp")

    # select template as English short
    time.sleep(2)
    button = context.driver.find_element(By.ID, "template_name")
    context.driver.execute_script("arguments[0].click();", button)
    select = Select(button)
    select.select_by_visible_text("Hindi Short")

    time.sleep(2)
    button = context.driver.find_element(By.ID, "insert_template_to_msg")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'click on send now button')
def step_impl(context):
    # click on multipart SMS

    time.sleep(3)
    unicode = context.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[4]/div[1]/div/div/div/div[1]/div[1]/div/div/div/div[2]/p").text
    if unicode == "Message Contains Unicode Characters, Please select Allow Unicode to Send this Message!!!":
        time.sleep(1)
        button = context.driver.find_element(By.ID, "ok_modal")
        context.driver.execute_script("arguments[0].click();", button)
        time.sleep(1)
        button = context.driver.find_element(By.NAME, "unicode_check")
        context.driver.execute_script("arguments[0].click();", button)
        time.sleep(1)
        button = context.driver.find_element(By.ID, "send")
        context.driver.execute_script("arguments[0].click();", button)
    else:
        assert False, f"{unicode}"

    time.sleep(3)
    try:
        if (context.driver.find_element(By.XPATH,
                                            "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[4]/div[1]/div/div/div/div[1]/div[1]/div/div/div/div[2]/p").text == "Message too long, Select Multipart !!!"):
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

    time.sleep(3)
    button = context.driver.find_element(By.ID, "confirm_send_sms")
    context.driver.execute_script("arguments[0].click();", button)

    # time.sleep(1)
    # context.driver.close()

