from behave import *
import time
from selenium.webdriver.common.by import By

import Tenant_CommomUtility as CU
options_VendorObj = CU.options_Vendor()

@then(u'Click on vendor tab')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, "option_vendor").click()

@then(u'Click on Add vendor')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, "add_vendor").click()

@then(u'Check elements are present in vendor')
def step_impl(context):
    for x in options_VendorObj.options_Vendor_list:
        try:
            status = context.driver.find_element(By.ID, x).is_displayed()
            print(f"{x} --> is {status} ")
        except NameError:
            print(NameError)

@then(u'enter data into vendor')
def step_impl(context):
    for element_id in options_VendorObj.options_Vendor_list.keys():
        context.driver.find_element(By.ID, element_id).send_keys(options_VendorObj.options_Vendor_list[element_id])
        print(f"{element_id}")

@then(u'Verify vendor is added or not')
def vendor(context):
    vendor = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[1]").text
    if vendor == "vendor_AIRTEL":
        assert True, f"Circle {vendor} Is Added Succesfully"
    else:
        assert False, f"Circle {vendor} Unable To Add"

    # time.sleep(1)
    # context.driver.close()
