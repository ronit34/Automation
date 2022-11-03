from behave import *
from selenium.webdriver.common.by import By
import time

import CommonUtility as CU
DLT_URLObj = CU.DLT_URL()


@then(u'Click on URL')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, "url_tab").click()


@then(u'Click on Add Short URL')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, "create_url").click()


@then(u'Check labels')
def step_impl(context):
    text1 = context.driver.find_element_by_xpath("//*[@id='myModal']/div/div/div[1]/p[1]").text
    text2 = context.driver.find_element_by_xpath("//*[@id='myModal']/div/div/div[2]/div/label").text
    if (text1 == "Add Short URL" and text2 == "URL *"):
        assert True, "Test Passed"
    else:
        assert False, "Test Failed"


@then(u'Insert data into URL fields')
def step_impl(context):
    time.sleep(1)
    for element_id in DLT_URLObj.DLT_URL_inputbox_list.keys():
        context.driver.find_element(By.ID, element_id).send_keys(
            DLT_URLObj.DLT_URL_inputbox_list[element_id])
        print(f"{element_id}")


@then(u'click on add button to add URL')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, "add_url").click()


@then(u'Check URL is created or not')
def step_impl(context):
    time.sleep(1)
    entity = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[2]").text
    if (entity == "google.com"):
        assert True, f"{entity} found"
    else:
        assert False, f"{entity} not found"

    # time.sleep(2)
    # context.driver.close()
