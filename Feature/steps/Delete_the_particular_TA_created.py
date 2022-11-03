import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then(u'Delete the perticular TA')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[4]/a[2]/img")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Click on delete in User_Management')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "delete_save")
    context.driver.execute_script("arguments[0].click();", button)


