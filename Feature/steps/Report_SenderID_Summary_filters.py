import math

from selenium.webdriver.support.select import Select
from behave import *
from selenium.webdriver.common.by import By
import time


@then(u'click on senderID summary tab in report')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "pills-daily-summary-tab")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'fill wrong sender ID in filters')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_id("sender_id").send_keys("12345678")
    time.sleep(1)
    button = context.driver.find_element(By.ID, "search")
    context.driver.execute_script("arguments[0].click();", button)
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-daily-summary']/div[3]/div").text
    if text == "No report data avaialable":
        time.sleep(1)
        context.driver.find_element_by_id("sender_id").clear()
        context.driver.find_element_by_id("sender_id").send_keys("123456")
        time.sleep(1)
        button = context.driver.find_element(By.ID, "search")
        context.driver.execute_script("arguments[0].click();", button)

@then(u'set limit and check pagination in senderID summary')
def step_impl(context):
    time.sleep(2)
    rows_len = len(context.driver.find_elements_by_xpath("//*[@id='senderid-summary-table']/tbody/tr")) - 1
    # print(f"{rows_len} --> is present")
    # print(f"{rows_len} --> is present")

    length = rows_len / 5
    # print(f"{length} --> is present")
    # print(f"{length} --> is present")

    final_length = math.ceil(length)
    # print(f"{final_length} --> is present")
    # print(f"{final_length} --> is present")

    ############# Set Limit ###########################
    time.sleep(2)
    select = Select(context.driver.find_element_by_xpath('//*[@id="pills-daily-summary"]/div[2]/div/div[2]/select'))
    select.select_by_value('5')
    time.sleep(1)
    button = context.driver.find_element(By.ID, "search")
    context.driver.execute_script("arguments[0].click();", button)

    #############VERIFY NO OF RECORDS AFTER LIMIT #################

    time.sleep(1)
    limit_len = len(context.driver.find_elements_by_xpath("//*[@id='senderid-summary-table']/tbody/tr")) - 1

    if limit_len == 5:
        assert True, "no of record  verified"
    elif 5 > limit_len > 0:
        print("Less than 5 records")
    else:
        assert False, f"{limit_len} is the length of records after limit"

    ############ VERIFY NO OF PAGINATION #################

    time.sleep(1)
    str_le = str(final_length)
    page = context.driver.find_element_by_xpath("//*[@id='pills-daily-summary']/div[3]/div/nav/a").text
    if page == "Page 1 of " + str_le:
        assert True, f"{page} is present"
    else:
        assert False, f"{page} not present"


