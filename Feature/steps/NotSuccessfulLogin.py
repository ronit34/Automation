from behave import *
from selenium.webdriver.common.by import By
import time

@when(u'Enter wrong Username "{user}" and {password} "admin123"')
def step_impl(context, user, password):
    context.driver.maximize_window()
    context.driver.find_element_by_id("email").send_keys(user)
    context.driver.find_element_by_id("password").send_keys(password)

@then(u'Check the message invalid login')
def step_impl(context):
    time.sleep(1)
    elabel = context.driver.find_element(By.XPATH,"//*[@id='errormsg']/span").text
    if (elabel == "Invalid UserName or Password"):
        assert True, f"{elabel} found"
    else:
        assert False, f"{elabel} not found"

    # time.sleep(1)
    # context.driver.close()

