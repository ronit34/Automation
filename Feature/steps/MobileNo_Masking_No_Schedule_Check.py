from behave import *
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@then(u'check for mobile no masking')
def step_impl(context):
    time.sleep(1)
    # text = context.driver.find_element_by_xpath(
    #     "/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div/div[3]/table/tbody/tr[2]/td[3]").text
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div/div[3]/table/tbody/tr[2]/td[5]").text

    if text == "9234567890":
        print(f"{text} --> Mobile Number is masked")
        print(f"{text} --> Mobile Number is masked")
    else:
        assert False, f"{text}---> Mobile Number is not masked"

    # time.sleep(1)
    # context.driver.close()