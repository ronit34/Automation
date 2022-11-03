from behave import *
import time
from selenium.webdriver.common.by import By

import Tenant_CommomUtility as CU
options_circleObj = CU.options_circle()

@then(u'Click on Options button')
def option(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "menu_option")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'Click on Circle tab')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, "option_circle").click()

@then(u'Click on Add Circle Button')
def circle(context):
    time.sleep(2)
    context.driver.find_element(By.ID,"add_circle").click()

@then(u'Check elements are present in circle')
def check_elements(context):
    for x in options_circleObj.options_circle_list:
        try:
            status = context.driver.find_element(By.ID, x).is_displayed()
            print(f"{x} --> is {status} ")
        except NameError:
            print(NameError)

@then(u'enter data into circle')
def enter_Data(context):
    time.sleep(2)
    for element_id in options_circleObj.options_circle_list.keys():
        context.driver.find_element(By.ID, element_id).send_keys(options_circleObj.options_circle_list[element_id])
        print(f"{element_id}")

@then(u'click on add button of Options to add entered data')
def click_add(context):
    time.sleep(2)
    context.driver.find_element(By.ID, "add_option").click()

@then(u'Verify Circle is added or not')
def check_circle_add(context):
    circle = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[1]").text
    if circle=="Haryana":
        assert True,f"Circle {circle} Is Added Succesfully"
    else:
        assert False,f"Circle {circle} Unable To Add"

    # time.sleep(1)
    # context.driver.close()
