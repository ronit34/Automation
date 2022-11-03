from behave import *
from selenium.webdriver.common.by import By
import time

@then(u'click on edit of url')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[4]/a[1]/img").click()

@then(u'enter new url')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[1]/div[2]/div/div/div/div[2]/div/input").clear()
    context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[1]/div[2]/div/div/div/div[2]/div/input").send_keys("youtube.com")

@then(u'click on update to update url')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[1]/div[2]/div/div/div/div[3]/input[2]").click()

@then(u'check edited url')
def step_impl(context):
    time.sleep(1)
    entity = context.driver.find_element(By.XPATH,
                "//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[2]").text
    if (entity == "youtube.com"):
        assert True, f"{entity} found"
    else:
        assert False, f"{entity} not found"

    # time.sleep(1)
    # context.driver.close()