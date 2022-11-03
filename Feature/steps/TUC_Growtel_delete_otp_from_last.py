import time
from behave import *
from selenium.webdriver.common.by import By


@then(u'Enter OTP')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.ID, "first").send_keys("1")
    time.sleep(2)
    context.driver.find_element(By.ID, "second").send_keys("2")
    time.sleep(2)
    context.driver.find_element(By.ID, "third").send_keys("3")
    time.sleep(2)
    context.driver.find_element(By.ID, "fourth").send_keys("3")
    time.sleep(2)
    context.driver.find_element(By.ID, "fifth").send_keys("4")
    time.sleep(2)
    context.driver.find_element(By.ID, "sixth").send_keys("5")
    time.sleep(2)


@then(u'Delete OTP from last')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.ID, "sixth").clear()
    time.sleep(2)
    context.driver.find_element(By.ID, "fifth").clear()
    time.sleep(2)
    context.driver.find_element(By.ID, "fourth").clear()
    time.sleep(2)
    context.driver.find_element(By.ID, "third").clear()
    time.sleep(2)
    context.driver.find_element(By.ID, "second").clear()
    time.sleep(2)
    context.driver.find_element(By.ID, "first").clear()
    time.sleep(2)
