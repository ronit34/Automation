import math

from selenium.webdriver.support.select import Select
from behave import *
from selenium.webdriver.common.by import By
import time


@then(u'select TUC from dropdown')
def step_impl(context):
    time.sleep(2)
    select = Select(context.driver.find_element_by_id('tuc-report'))
    select.select_by_value('2000')
    time.sleep(1)
    button = context.driver.find_element(By.ID, "search")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'select campaign name')
def step_impl(context):
    time.sleep(2)
    select = Select(context.driver.find_element_by_id('camp-report'))
    select.select_by_value('all')


@then(u'set limit and check pagination in campaign summary')
def step_impl(context):
    time.sleep(2)   ## finding rows on 1st page
    rows_len1 = len(context.driver.find_elements_by_xpath(
        "//*[@id='campaign-summary-table']/tbody/tr")) - 1
    # print(f"{rows_len1} --> is present")
    # print(f"{rows_len1} --> is present")

    time.sleep(1)   ## clicking on Next to go to other page
    button = context.driver.find_element(By.XPATH, "//*[@id='search_label']/nav/a[2]")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)  ## finding rows on 2nd page
    rows_len2 = len(context.driver.find_elements_by_xpath(
        "//*[@id='campaign-summary-table']/tbody/tr")) - 1
    # # print(f"{rows_len2} --> is present")
    # # print(f"{rows_len2} --> is present")

    rows_len = rows_len1 + rows_len2  ## finding total rows of page 1 & page 2
    # # print(f"{rows_len} --> is present")
    # # print(f"{rows_len} --> is present")

    length = rows_len / 5
    final_length = math.ceil(length)
    # print(f"{final_length} --> is present")
    # print(f"{final_length} --> is present")

    ############# Set Limit ###########################
    time.sleep(2)
    select = Select(context.driver.find_element_by_xpath(
        '//*[@id="pills-campaign-summary"]/div[2]/div/div[2]/select'))
    select.select_by_value('5')
    time.sleep(1)
    button = context.driver.find_element(By.ID, "search")
    context.driver.execute_script("arguments[0].click();", button)

    #############VERIFY NO OF RECORDS AFTER LIMIT #################

    time.sleep(1)
    limit_len = len(context.driver.find_elements_by_xpath(
        "//*[@id='campaign-summary-table']/tbody/tr")) - 1

    if limit_len == 5:
        assert True, "no of record  verified"
    elif 5 > limit_len > 0:
        print("Less than 5 records")
    else:
        assert False, f"{limit_len} is the length of records after limit"

    ############ VERIFY NO OF PAGINATION #################

    time.sleep(1)
    str_le = str(final_length)
    page = context.driver.find_element_by_xpath("//*[@id='search_label']/nav/a[1]").text
    # print(f"{page} --> is present")
    # print(f"{page} --> is present")

    # print(f"{str_le} --> is present")
    # print(f"{str_le} --> is present")

    if page == "Page 1 of " + str_le:
        assert True, f"{page} is present"
    else:
        assert False, f"{page} not present"
