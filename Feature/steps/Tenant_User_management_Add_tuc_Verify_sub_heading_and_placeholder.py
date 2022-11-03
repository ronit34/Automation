from behave import *
from selenium.webdriver.common.by import By
import time


@then(u'Click on Add_TUC')
def step_impl(context):
    button = context.driver.find_element(By.ID, "create_tuc")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Verify Sub-heading and Placeholder')
def step_impl(context):
    sub_head_txt = context.driver.find_element(By.ID, "current_date").text
    # print(sub_head_txt)
    if sub_head_txt == "Monday 10 October 2022":
        assert True, f"{sub_head_txt}"
    else:
        assert False, f"{sub_head_txt}"

    name = context.driver.find_element(By.ID, "name").get_attribute('placeholder')
    print(name)
    if name == " Enter Your Name":
        assert True, f"{name}"
    else:
        assert False, f"{name}"

    validity = context.driver.find_element(By.ID, "validity").get_attribute('placeholder')
    print(validity)
    if validity == "No. of Days":
        assert True, f"{validity}"
    else:
        assert False, f"{validity}"

    child_tuc = context.driver.find_element(By.ID, "childtuc").get_attribute('placeholder')
    print(child_tuc)
    if child_tuc == "Enter Child TUC":
        assert True, f"{child_tuc}"
    else:
        assert False, f"{child_tuc}"