from behave import *
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
@then(u'Check TUC select dropdown is present')
def step_impl(context):
    time.sleep(1)
    time.sleep(1)
    button = context.driver.find_element_by_id("filter_link")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'Select tuc for showing records')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_xpath("//*[@id='filter_dropdown']/div/div/input")
    context.driver.execute_script("arguments[0].click();", button)
    time.sleep(1)
    button = context.driver.find_element_by_xpath("//*[@id='filter_dropdown']/div/ul/li[1]/a")
    context.driver.execute_script("arguments[0].click();", button)
    time.sleep(1)
    button = context.driver.find_element_by_xpath("//*[@id='filter_dropdown']/div/ul/li[2]/a")
    context.driver.execute_script("arguments[0].click();", button)
    # time.sleep(1)
    # button = context.driver.find_element(By.ID, "multiselectTag")
    # context.driver.execute_script("arguments[0].click();", button)
    # select = Select(button)
    # select.select_by_visible_text("ICICI")
    #
    # time.sleep(5)
    # button = context.driver.find_element(By.ID, "multiselectTag")
    # context.driver.execute_script("arguments[0].click();", button)
    # select = Select(button)
    # select.select_by_visible_text("HDFC")

    # time.sleep(1)
    # context.driver.close()
