from behave import *
from selenium.webdriver.common.by import By
import time

@then(u'click on Delete')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.XPATH,"//*[@id='pills-campaign']/div[2]/table[2]/tbody/tr[2]/td[5]/a[2]/img")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'click on Delete Button to delete')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID,"delete")
    context.driver.execute_script("arguments[0].click();", button)