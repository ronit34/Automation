from behave import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

@when(u'Enter Username "" and password ""')
def step_impl(context):
    context.driver.find_element(By.ID, "email").send_keys()
    context.driver.find_element(By.ID, "password").send_keys()
    time.sleep(1)

@when(u'Enter Username "{username}" and password ""')
def step_impl(context, username):
    context.driver.find_element(By.ID, "email").send_keys(username)
    context.driver.find_element(By.ID, "password").send_keys()
    time.sleep(1)

@when(u'Enter Username "" and password "{password}"')
def step_impl(context, password):
    context.driver.find_element(By.ID, "email").send_keys()
    context.driver.find_element(By.ID, "password").send_keys(password)
    time.sleep(1)

@when(u'Enter Username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.driver.find_element(By.ID, "email").send_keys(username)
    context.driver.find_element(By.ID, "password").send_keys(password)
    time.sleep(1)

@when(u'Click on Sign in Button for multiple')
def step_impl(context):
    button = context.driver.find_element(By.ID, "login_button")
    context.driver.execute_script("arguments[0].click();", button)
    time.sleep(1)
    text = context.driver.find_element_by_id("errormsg").text
    if (text == "Invalid UserName or Password"):
        assert True, "Test Passed"
    else:
         assert False, "Test Failed"

    time.sleep(1)
    context.driver.close()
