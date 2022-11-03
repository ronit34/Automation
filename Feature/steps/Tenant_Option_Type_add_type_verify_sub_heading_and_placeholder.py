from behave import *
from selenium.webdriver.common.by import By
import time


@then(u'Click on Add Type in tenant')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "add_type")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Verify Sub-heading and Placeholder_Option Type')
def step_impl(context):
    time.sleep(2)
    txt = context.driver.find_element(By.XPATH, "//*[@id='myModal']/div/div/div[1]/p[2]").text

    if txt == "Add a new Type by filling the details below":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"

    type_name = context.driver.find_element(By.ID, "type_name").get_attribute('placeholder')
    print(type_name)
    if type_name == "Enter Type Name":
        assert True, f"{type_name}"
    else:
        assert False, f"{type_name}"

    desc = context.driver.find_element(By.ID, "type_desc").get_attribute('placeholder')
    print(desc)
    if desc == "Enter Description":
        assert True, f"{desc}"
    else:
        assert False, f"{desc}"
