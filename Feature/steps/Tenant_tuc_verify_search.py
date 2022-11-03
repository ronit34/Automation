from behave import *
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
import time
import re


@then(u'type username "{search}" and verify search results in tuc tab')
def step_impl(context, search):
    time.sleep(2)
    context.driver.find_element(By.ID, "tuc_input").send_keys(search)
    time.sleep(2)
    button = context.driver.find_element_by_id("user_search")
    context.driver.execute_script("arguments[0].click();", button)
    time.sleep(2)
    rows = context.driver.find_elements_by_xpath("//*[@id='pills-campaign']/div[2]/div/table[2]/tbody/tr")
    x = len(rows) - 1
    for td in context.driver.find_elements_by_xpath("//*[@id='pills-campaign']/div[2]/div/table[2]/tbody"):
        if search.lower() in td.text.lower():
            time.sleep(2)
            assert True, f" {x} ----> rows present"
        else:
            assert False, f" {x} ----> rows present"

    # context.driver.find_element(By.ID, "user_input").clear()


@then(u'check for invalid input in tuc "{invalid}"')
def step_impl(context, invalid):
    context.driver.find_element(By.ID, "tuc_input").clear()
    time.sleep(2)
    context.driver.find_element(By.ID, "tuc_input").send_keys(invalid)
    time.sleep(2)
    button = context.driver.find_element_by_id("user_search")
    context.driver.execute_script("arguments[0].click();", button)
    time.sleep(2)
    a = context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/div/span").text
    if a == "No Record found":
        assert True, f"{a} is present"
    else:
        assert False, f"{a} is not present"
