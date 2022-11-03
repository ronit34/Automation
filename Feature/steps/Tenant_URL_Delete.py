from behave import *
from selenium.webdriver.common.by import By
import time

@then(u'click on delete icon of URl')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[4]/a[2]/img").click()

@then(u'click on Delete button to delete url')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[1]/div[2]/div/div/div/div[3]/a[2]").click()

    # time.sleep(1)
    # context.driver.close()