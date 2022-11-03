from behave import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

@then(u'Enter Right username "{username}" and password "{password}"')
def enter_credentials(context, username, password):
    context.driver.maximize_window()
    context.driver.find_element(By.ID, "email").send_keys(username)
    context.driver.find_element(By.ID, "password").send_keys(password)

@then(u'Check Terms And Conditions Check Box is preselected')
def step_impl(context):
    checkbox = context.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[3]/label/input").is_selected()
    if checkbox:
        assert True, f"Check box is selected"
    else:
        assert False, f"Check box is not selected"

@when(u'Click on Sign in Button')
def click_sign_in(context):
    button = context.driver.find_element(By.ID, "login_button")
    context.driver.execute_script("arguments[0].click();", button)
    # context.driver.find_element(By.ID, "login_button").click()

@then(u'Check if the message invalid login then close the browser')
def step_impl(context):
    time.sleep(3)
    try:
        if (context.driver.find_element(By.ID, "errormsg").text == "Invalid UserName or Password"):
            print("Unable to Sign In")
            print("Unable to Sign In")
            context.driver.close()
        else:
            print("Sign in Successfully")
    except NoSuchElementException:
        print("Sign in Successfully")
        print("Sign in Successfully")

@then(u'Check the message valid login')
def check_valid_login(context):
    time.sleep(1)
    status = context.driver.find_element(By.ID, "current_date").is_displayed()
    assert status is True
    print("Successfull Logged In")

    # time.sleep(1)
    # context.driver.close()


