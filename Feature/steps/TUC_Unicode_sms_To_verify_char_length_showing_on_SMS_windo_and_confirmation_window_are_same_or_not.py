from behave import *
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

import CommonUtility as CU
new_unicode_sms_inputObj = CU.new_unicode_sms_input()


@then(u'insert data into Unicode_sms')
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

    # check box of allow Unicode
    time.sleep(2)
    click = context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[5]/div[2]/label[1]/input")
    context.driver.execute_script("arguments[0].click();", click)


@then(u'Count characters for unicode')
def step_impl(context):
    time.sleep(2)
    text_2 = context.driver.find_element(By.ID, "limit_msg").text
    list_ = text_2.split(" ")
    time.sleep(2)
    txt = context.driver.find_element(By.XPATH, "//*[@id='msgText']").get_attribute("value")
    list_2 = list(txt)
    length_1 = len(list_2)
    var = "{" and "}"
    for i in list_2:
        if i in var:
            length_1 += 2
    count_length = length_1
    context.char = int(list_[0])

    if context.char == count_length:
        assert True, "Passed"
    else:
        assert False, "Failed"


@then(u'Verify char length showing on SMS windo and confirmation window are same or_not')
def step_impl(context):
    time.sleep(2)
    txt = context.driver.find_element(By.XPATH,
                                      "//*[@id='bd-example-modal-lg']/div/div/div[2]/div[2]/div[8]/div/p").text
    if context.char == int(txt):
        assert True, "Passed"
    else:
        assert False, "Failed"

