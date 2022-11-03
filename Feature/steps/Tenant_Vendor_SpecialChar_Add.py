from behave import *
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
import time
import re

import CommonUtility as CU
option_vendor_addobj = CU.Option_Vendor_add()

@then(u'check add button of Vendor is present')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element_by_id("add_vendor").is_displayed()

@then(u'click on add button of  Vendor')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("add_vendor")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check elements are present in Add Vendor')
def step_impl(context):
    time.sleep(3)
    for x in option_vendor_addobj.Option_Type_add_inputbox_list:
        try:
            status = context.driver.find_element(By.ID, x).is_displayed()
            print(f"{x} --> is {status} ")
        except NameError:
            print(NameError)

@then(u'Enter the details into add Vendor')
def step_impl(context):
    time.sleep(1)
    for element_id in option_vendor_addobj.Option_Type_add_inputbox_list.keys():
        time.sleep(1)

        context.driver.find_element(By.ID, element_id).clear()
        context.driver.find_element(By.ID, element_id).send_keys(
            option_vendor_addobj.Option_Type_add_inputbox_list[element_id])
        print(f"{element_id}")
    # text = context.driver.find_element_by_id("vendor_telemar")
    # if(text.get_attribute('value')):
    #     s1 = re.sub("[^0-9A-Za-z]", "", text)
    #     time.sleep(1)
    #     context.driver.find_element(By.ID, "vendor_telemar").clear()
    #     time.sleep(1)
    #     context.driver.find_element(By.ID, "vendor_telemar").send_keys(s1)
    #     print(s1)

@then(u'click on Add button of add Vendor')
def step_impl(context):
    time.sleep(5)
    button = context.driver.find_element_by_id("add_option")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check if TelemarID contain error label or not')
def step_impl(context):
    time.sleep(1)
    a = context.driver.find_element_by_xpath(
        "//span[text()='Telemar ID can not contain Special Characters']").is_displayed()
    if a:
        time.sleep(1)
        context.driver.find_element_by_id("vendor_telemar").clear()
        context.driver.find_element_by_id("vendor_telemar").send_keys("AirtelTelecom")
        time.sleep(3)
        button = context.driver.find_element_by_id("add_option")
        context.driver.execute_script("arguments[0].click();", button)
        assert True, f"{a} is present"
    else:
        assert False, f"{a} is not present"

# @then(u'verify the vendor created or not')
# def step_impl(context):
#     time.sleep(1)
#     # text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[1]").text
#     text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr[19]/td[1]").text
#
#     if text == "Airtel":
#         assert True, f"{text} is present"
#     else:
#         assert False, f"{text} is not present"

    # time.sleep(1)
    # context.driver.close()