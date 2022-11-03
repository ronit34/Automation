import time

from behave import *
from selenium.webdriver.common.by import By

# @then(u'Enter Username "Telspiel" and password "Telspiel"')
# def step_impl(context):
#     context.driver.find_element_by_id("email").send_keys("Telspiel")
#     context.driver.find_element_by_id("password").send_keys("Telspiel")

@then(u'Select logo')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.NAME,"file").send_keys("/home/onexadmin/Downloads/ICICIlogo.png")

@then(u'Select icon')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[2]/div/div/div[2]/div/div/div[1]/div[3]/div[2]/form/div[2]/input[2]").send_keys("/home/onexadmin/Downloads/iciciIcon.png")

@then(u'Select login page logo')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div[4]/div/form/div[2]/input[2]").send_keys("/home/onexadmin/Downloads/download.svg")
    time.sleep(1)

@then(u'click on save changes button')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "save-changes")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'click on ok button')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "ok_modal")
    context.driver.execute_script("arguments[0].click();", button)

    # time.sleep(1)
    # context.driver.close()
