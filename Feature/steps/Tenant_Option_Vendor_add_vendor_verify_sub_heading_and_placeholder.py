from behave import *
from selenium.webdriver.common.by import By
import time


@then(u'Click on Vendor')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "option_vendor")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Verify Sub-heading and Placeholder_Option Vendor')
def step_impl(context):
    time.sleep(2)
    txt = context.driver.find_element(By.XPATH, "//*[@id='myModal']/div/div/div[1]/p[2]").text

    if txt == "Add a new Vendor by filling the details below":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"

    vendor_name = context.driver.find_element(By.ID, "vendor_name").get_attribute('placeholder')
    print(vendor_name)
    if vendor_name == "Enter Vendor Name":
        assert True, f"{vendor_name}"
    else:
        assert False, f"{vendor_name}"

    telemar_id = context.driver.find_element(By.ID, "vendor_telemar").get_attribute('placeholder')
    print(telemar_id)
    if telemar_id == "Enter Telemar ID":
        assert True, f"{telemar_id}"
    else:
        assert False, f"{telemar_id}"

    desc = context.driver.find_element(By.ID, "vendor_desc").get_attribute('placeholder')
    print(desc)
    if desc == "Enter Description":
        assert True, f"{desc}"
    else:
        assert False, f"{desc}"
