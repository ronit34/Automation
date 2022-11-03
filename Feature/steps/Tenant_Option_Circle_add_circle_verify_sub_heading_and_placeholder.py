from behave import *
from selenium.webdriver.common.by import By
import time


@then(u'Click on Circle')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "option_circle")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Click on Add Circle')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "add_circle")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Verify Sub-heading and Placeholder_Option Circle')
def step_impl(context):
    time.sleep(2)
    txt = context.driver.find_element(By.XPATH, "//*[@id='myModal']/div/div/div[1]/p[2]").text

    if txt == "Add a new Circle by filling the details below":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"

    circle_name = context.driver.find_element(By.ID, "circle_name").get_attribute('placeholder')
    print(circle_name)
    if circle_name == "Enter Circle Name":
        assert True, f"{circle_name}"
    else:
        assert False, f"{circle_name}"

    desc = context.driver.find_element(By.ID, "circle_desc").get_attribute('placeholder')
    print(desc)
    if desc == "Enter Description":
        assert True, f"{desc}"
    else:
        assert False, f"{desc}"
