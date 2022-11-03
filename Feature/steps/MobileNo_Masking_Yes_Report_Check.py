from behave import *
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@then(u'Click on Send Button of quick sms')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "send")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(7)
    button = context.driver.find_element(By.ID, "confirm_send_sms")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'click on cancel of pop up')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "close_modal")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'click on mis web detail button')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.XPATH, "//*[@id='customers']/tbody/tr[2]/td[14]/a/img")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'Check mobile number is masked or not')
def step_impl(context):
    time.sleep(2)
    txt = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div/div[3]/table/tbody/tr[2]/td[5]").text
    if txt == "923456XXXX":
        print(f"{txt} --> Mobile Number is masked")
        print(f"{txt} --> Mobile Number is masked")
    else:
        assert False, f"{txt} ---> Mobile Number is not masked"

@then(u'Copy UUID and enter it in Report Search')
def step_impl(context):
    text = context.driver.find_element_by_xpath("//*[@id='customers']/tbody/tr[2]/td[3]").text

    time.sleep(2)
    button = context.driver.find_element(By.ID, "pills-search-tab")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    context.driver.find_element_by_id("uuid").send_keys(text)

@then(u'check mobile number masking')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='search-table']/tbody/tr[2]/td[7]").text
    if text == "923456XXXX":
        print(f"{text} --> Mobile Number is masked")
        print(f"{text} --> Mobile Number is masked")
    else:
        assert False, f"{text}---> Mobile Number is not masked"

    # time.sleep(1)
    # context.driver.close()
