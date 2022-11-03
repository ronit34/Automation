from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
import time

import CommonUtility as CU

option_vendor_editobj = CU.Option_Vendor_edit()

# @then(u'click on Vendor tab')
# def step_impl(context):
#     time.sleep(1)
#     button = context.driver.find_element_by_id("option_vendor")
#     context.driver.execute_script("arguments[0].click();", button)

@then(u'check edit button of second Vendor is present')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[2]/table/tbody/tr[3]/td[4]/a[1]").is_displayed()


@then(u'check edit icon mouse hover text - vendor')
def check_edit_button(context):
    time.sleep(2)
    action = ActionChains(context.driver);
    parent_level_menu = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[4]/a[1]")
    action.move_to_element(parent_level_menu).perform()

    hover_title = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[4]/a[1]").get_attribute('title')
    if hover_title == "Edit":
        print(f"{hover_title} --> is present")
        print(f"{hover_title} --> is present")
    else:
        assert False, f"{hover_title}--->is not present"


@then(u'enter data to add vendor')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element_by_id("vendor_name").send_keys("vendor_TEST")
    context.driver.find_element_by_id("vendor_telemar").send_keys("12345678")
    context.driver.find_element_by_id("vendor_desc").send_keys("Test Vendor")

@then(u'click on edit button of first Vendor is present')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[2]/table/tbody/tr[3]/td[4]/a[1]/img")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check elements are present in Edit Vendor')
def step_impl(context):
    time.sleep(3)
    for x in option_vendor_editobj.Option_Vendor_edit_inputbox_list:
        try:
            status = context.driver.find_element(By.ID, x).is_displayed()
            print(f"{x} --> is {status} ")
        except NameError:
            print(NameError)

@then(u'Enter the details into edit Vendor')
def step_impl(context):
    time.sleep(1)
    for element_id in option_vendor_editobj.Option_Vendor_edit_inputbox_list.keys():
        time.sleep(1)
        context.driver.find_element(By.ID, element_id).clear()
        context.driver.find_element(By.ID, element_id).send_keys(
            option_vendor_editobj.Option_Vendor_edit_inputbox_list[element_id])
        print(f"{element_id}")

@then(u'click on update button of edit Vendor')
def step_impl(context):
    time.sleep(5)
    button = context.driver.find_element_by_id("update_option")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check if Telemar contain error label or not')
def step_impl(context):
    time.sleep(1)
    a = context.driver.find_element_by_xpath("//span[text()='Telemar ID can not contain Special Characters']").is_displayed()
    if a:
        time.sleep(1)
        context.driver.find_element_by_id("vendor_telemar").clear()
        context.driver.find_element_by_id("vendor_telemar").send_keys("BSNLTelecom")
        time.sleep(3)
        button = context.driver.find_element_by_id("update_option")
        context.driver.execute_script("arguments[0].click();", button)
        assert True, f"{a} is present"
    else:
        assert False, f"{a} is not present"

@then(u'verify the updated vendor created or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr[3]/td[1]").text

    if text == "BSNL":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

    # time.sleep(1)
    # context.driver.close()