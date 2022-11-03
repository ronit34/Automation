from behave import *
from selenium.webdriver.common.by import By
import time


@then(u'Verify Sub-heading and Placeholder_Option Carrier')
def step_impl(context):
    time.sleep(2)
    txt = context.driver.find_element(By.XPATH, "//*[@id='myModal']/div/div/div[1]/p[2]").text

    if txt == "Add a new Carrier by filling the details below":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"

    carrier_name = context.driver.find_element(By.ID, "carrier_name").get_attribute('placeholder')
    print(carrier_name)
    if carrier_name == "Enter Carrier Name":
        assert True, f"{carrier_name}"
    else:
        assert False, f"{carrier_name}"

    desc = context.driver.find_element(By.ID, "carrier_desc").get_attribute('placeholder')
    print(desc)
    if desc == "Enter Description":
        assert True, f"{desc}"
    else:
        assert False, f"{desc}"
