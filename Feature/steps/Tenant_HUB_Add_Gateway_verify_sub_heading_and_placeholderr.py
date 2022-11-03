from behave import *
from selenium.webdriver.common.by import By
import time


@then(u'Verify Sub-heading and Placeholder_Gateway')
def step_impl(context):
    time.sleep(2)
    sub_head_txt = context.driver.find_element(By.ID, "current_date").text
    print(sub_head_txt)
    if sub_head_txt == "Monday 10 October 2022":
        assert True, f"{sub_head_txt}"
    else:
        assert False, f"{sub_head_txt}"

    gateway_name = context.driver.find_element(By.ID, "gateway_name").get_attribute('placeholder')
    print(gateway_name)
    if gateway_name == "Enter Gateway Name":
        assert True, f"{gateway_name}"
    else:
        assert False, f"{gateway_name}"

    description = context.driver.find_element(By.ID, "description").get_attribute('placeholder')
    print(description)
    if description == "Enter Description":
        assert True, f"{description}"
    else:
        assert False, f"{description}"

    remark = context.driver.find_element(By.ID, "remarks").get_attribute('placeholder')
    print(remark)
    if remark == "Enter Remark":
        assert True, f"{remark}"
    else:
        assert False, f"{remark}"

