import time
from behave import *
from selenium.webdriver.common.by import By


@then(u'Check Scrub DND')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[6]/div["
                                                   "2]/label[1]/input")
    context.driver.execute_script("arguments[0].click();", button)