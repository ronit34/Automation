from behave import *
import time
from selenium.webdriver.common.by import By


@then(u'Check username field is present or not')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, "username").is_displayed()

@then(u'Enter wrong username')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, "username").send_keys("ICICI")

@then(u'Click on Reset password button')
def step_impl(context):
    button = context.driver.find_element(By.ID, "send_email")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'Check for error message appeared')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.ID, "errormsg").text
    if text == "Invalid UserName":
        assert True, "Text Passed"
    else:
        assert False, f" {text} ----> Not Found"
