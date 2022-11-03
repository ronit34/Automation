import math
from selenium.webdriver.support.select import Select
from behave import *
from selenium.webdriver.common.by import By
import time


@then(u'input wrong senderID in template search')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_xpath("//*[@id='senderid-template']").send_keys("xyz")
    time.sleep(1)
    button = context.driver.find_element(By.ID, "search")
    context.driver.execute_script("arguments[0].click();", button)
    time.sleep(2)
    text = context.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[3]").text
    if text == "No Template Data Available":
        assert True, f"{text}----> found"
    else:
        assert False, f"{text} ----> not found"


@then(u'input senderID in template search')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_xpath("//*[@id='senderid-template']").clear()
    time.sleep(2)
    context.driver.find_element_by_xpath("//*[@id='senderid-template']").send_keys("123456")
    time.sleep(1)
    button = context.driver.find_element(By.ID, "search")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'set limit and check pagination in template')
def step_impl(context):
    time.sleep(2)
    rows_len = len(context.driver.find_elements_by_xpath("//*[@id='template_table']/tbody/tr")) - 1
    length = rows_len / 5
    final_length = math.ceil(length)

#   ***************     Set Limit    ***************************
    time.sleep(2)
    select = Select(context.driver.find_element_by_xpath(
        '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/div[1]/div[1]/select'))
    select.select_by_value('5')
    time.sleep(1)
    button = context.driver.find_element(By.ID, "search")
    context.driver.execute_script("arguments[0].click();", button)

#    *****************   VERIFY NO OF RECORDS AFTER LIMIT  **************

    time.sleep(1)
    limit_len = len(context.driver.find_elements_by_xpath("//*[@id='template_table']/tbody/tr")) - 1

    if limit_len == 5:
        assert True, "no of record  verified"
    elif 5 > limit_len > 0:
        print("Less than 5 records")
    else:
        assert False, f"{limit_len} is the length of records after limit"

# *******************  VERIFY NO OF PAGINATION  *********************

    time.sleep(2)
    str_le = str(final_length)
    page = context.driver.find_element_by_xpath("//*[@id='tab_content']/nav/a[1]").text
    if page == "Page 1 of " + str_le:
        assert True, f"{page} is present"
    else:
        assert False, f"{page} not present"

    # time.sleep(1)
    # context.driver.close()
