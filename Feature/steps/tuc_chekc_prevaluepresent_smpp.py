import time
from behave import *
from selenium.webdriver.common.by import By

@then(u'check smpp assign to zero')
def step_impl(context):
    text=context.driver.find_element(By.ID,"smpps").get_attribute('value')
    print(f"{text} Value found")

@then(u'check SMS API assign to zero')
def step_impl(context):
    text1 = context.driver.find_element(By.ID, "smsapi").get_attribute('value')
    print(f"{text1} Value found")

@then(u'clear SMPP value')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID,"smpps").clear()

@then(u'clear SMS API Value')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, "smsapi").clear()

    # time.sleep(1)
    # context.driver.close()
