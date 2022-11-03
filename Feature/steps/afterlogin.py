from behave import *
import time
from selenium.webdriver.common.by import By

@then(u'Enter Username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.find_element(By.ID,"email").send_keys(user)
    context.driver.find_element(By.ID,"password").send_keys(pwd)

@then(u'Click on login button')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[3]/label/input").click()
    button = context.driver.find_element(By.ID, "login_button")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'Check Dashboard should present')
def step_impl(context):
    context.driver.find_element_by_link_text("Dashboard")

@then(u'Check Admin should present')
def step_impl(context):
    status = context.driver.find_element_by_xpath("//*[@id='profile']/div/p[1]").is_displayed()
    assert status is True
    print(f"{status}:successfull Login")

@then(u'click on dropdown of super admin onextel')
def step_impl(context):
    button = context.driver.find_element(By.ID, "dropdown-caret")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check present My Account')
def step_impl(context):
    context.driver.find_element(By.ID,"user-account").is_displayed()

@then(u'check present alert')
def step_impl(context):
    context.driver.find_element(By.ID,"user-alerts").is_displayed()

@then(u'check present change password')
def step_impl(context):
    context.driver.find_element(By.ID,"change-password").is_displayed()

@then(u'check present log out')
def step_impl(context):
    context.driver.find_element(By.ID,"log-out").is_displayed()

@then(u'check left Margin Dashboard present')
def step_impl(context):
    context.driver.find_element_by_id("menu_dashboard").is_displayed()

@then(u'check left Margin User Management present')
def step_impl(context):
    context.driver.find_element_by_id("menu_users").is_displayed()

@then(u'check check credit allocation is present')
def step_impl(context):
    context.driver.find_element_by_id("menu_credit_allocation").is_displayed()

@then(u'check master balance is present')
def step_impl(context):
    context.driver.find_element_by_id("menu_master_balance").is_displayed()

@then(u'check master license is present')
def step_impl(context):
    context.driver.find_element_by_id("menu_master_license").is_displayed()

    # time.sleep(1)
    # context.driver.close()
