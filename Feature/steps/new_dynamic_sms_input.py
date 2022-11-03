from behave import *
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

import CommonUtility as CU

new_dynamic_sms_inputObj = CU.new_dynamic_sms_input()


@then(u'insert data into Dynamic sms')
def insert_dynamic(context):
    time.sleep(3)
    a=context.driver.switch_to.frame("up_onex_file")
    context.driver.find_element(By.NAME, "file1").send_keys("/home/onexadmin/Downloads/fileFormats/dynamic_csv/10Nos1Vars10VarLength.csv")
    time.sleep(1)
    context.driver.switch_to.default_content()

    for element_id in new_dynamic_sms_inputObj.new_unicode_sms_input_list.keys():
        context.driver.find_element(By.ID, element_id).send_keys(
            new_dynamic_sms_inputObj.new_unicode_sms_input_list[element_id])


    # select Text column
    # button = context.driver.find_element(By.XPATH,
    #         "//*[@id='dashboard']/div[2]/div[1]/div[2]/div[3]/div/div/div[1]/ul/li[1]")
    button = context.driver.find_element(By.XPATH,
            "//*[@id='dashboard']/div[2]/div[1]/div[3]/div[3]/div/div/div[1]/ul/li[2]")
    context.driver.execute_script("arguments[0].click();", button)

    # click on arrow
    # button = context.driver.find_element_by_xpath(
    #     "//*[@id='dashboard']/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/button[1]")
    button = context.driver.find_element_by_xpath(
        "//*[@id='dashboard']/div[2]/div[1]/div[3]/div[3]/div/div/div[2]/button[1]")
    context.driver.execute_script("arguments[0].click();", button)

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
    select.select_by_visible_text("One Variable")

    time.sleep(1)
    button = context.driver.find_element(By.ID, "insert_template_to_msg")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'click on send now button of dynamic')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "confirm_send_sms")
    context.driver.execute_script("arguments[0].click();", button)

    # time.sleep(2)
    # context.driver.close()

