from behave import *
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@then(u'click on View Schedule button')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.XPATH, "//*[@id='pills-tab']/li[2]")
    context.driver.execute_script("arguments[0].click();", button)

    # scroll to top
    context.driver.execute_script("window.scrollTo(0, 0)")

@then(u'check for mobile no mask')
def step_impl(context):
    time.sleep(1)
    # text = context.driver.find_element_by_xpath(
    #     "/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div/div[3]/table/tbody/tr[2]/td[3]").text
    text = context.driver.find_element_by_xpath(
          "/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div/div[3]/table/tbody/tr[2]/td[5]").text

    if text == "923456XXXX":
        print(f"{text} --> Mobile Number is masked")
        print(f"{text} --> Mobile Number is masked")
    else:
        assert False, f"{text}---> Mobile Number is not masked"

    # time.sleep(1)
    # context.driver.close()




