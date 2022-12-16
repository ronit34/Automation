import time
from behave import *
from selenium.webdriver.common.by import By
from Feature.steps.login import driver


@given(u'launch chrome browser--')
def ChromeBrowserLaunch(context):
    try:
        context.driver = driver
    except NameError:
        print("Chrome browser did not open")
    else:
        print("Chrome browser open successfully")


@when(u'open Onextel Homepage "{homepage}"--')
def OpenHomepage(context, homepage):
    time.sleep(1)
    context.driver.maximize_window()
    try:
        context.driver.get(homepage)
    except NameError:
        print(f"{homepage} unable to load")
    else:
        print(f"{homepage} loaded successfully")


@then(u'Enter Username "{user}" and password "{pwd}"--')
def step_impl(context, user, pwd):
    time.sleep(1)
    context.driver.maximize_window()
    # context.driver.implicitly_wait(10)

    context.driver.find_element(By.ID, "email").send_keys(user)
    context.driver.find_element(By.ID, "password").send_keys(pwd)


@then(u'Check Terms And Conditions Check Box is preselected--')
def step_impl(context):
    time.sleep(1)
    checkbox = context.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[3]/label/input").is_selected()
    if checkbox:
        assert True, f"Check box is selected"
    else:
        assert False, f"Check box is not selected"


@then(u'Click on Sign in Button--')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element( By.ID, "login_button")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Verify date is present or not--')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.driver.find_element(By.ID, "current_date").is_displayed()


@then(u'Close window driver--')
def step_impl(context):
    time.sleep(2)
    context.driver.close()