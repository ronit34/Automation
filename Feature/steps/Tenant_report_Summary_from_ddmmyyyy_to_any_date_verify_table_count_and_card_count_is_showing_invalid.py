import time
from behave import *
from selenium.webdriver.common.by import By


@then(u'Click on Summary')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "pills-summary-tab")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Click on Summary search button')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "search")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Clear From date')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "date1")
    context.driver.execute_script("arguments[0].click();", button)
    time.sleep(2)
    context.driver.find_element(By.ID, "date1").clear()


@then(u'Verify data available')
def step_impl(context):
    text = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[3]/b").text
    print(text)
    if text == "Invalid From Date":
        assert True, f"{text}"
    else:
        assert False, f"{text}"

    card_container = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[2]/div[1]/div")
    print(card_container)
    if card_container :
        assert False, f"{card_container}"
    else:
        assert True, f"{card_container}"
