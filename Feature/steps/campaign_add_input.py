from behave import *
from selenium.webdriver.common.by import By
import time
@then(u'Enter Name "{name}"')
def step_impl(context,name):
    context.driver.implicitly_wait(20)
    context.driver.find_element(By.ID, "campaign_name").send_keys(name)

@then(u'Enter Description "{desc}"')
def step_impl(context,desc):
    context.driver.find_element(By.ID, "campaign_desc").send_keys(desc)

@then(u'click on Add Campaign button to create')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, "add_campaign").click()

    # time.sleep(1)
    # context.driver.close()
