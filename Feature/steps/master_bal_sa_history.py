from behave import *
from selenium.webdriver.common.by import By
import time


@then(u'click on master bal')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.driver.find_element(By.ID, "menu_master_balance").click()


@then(u'click on super admin history')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.ID, "pills-all-alloc").click()

@then(u'click on search of history')
def step_impl(context):
    time.sleep(3)
    context.driver.find_element(By.ID, "search_alloc").click()
    # text = context.driver.find_element_by_xpath("//*[@id='campaign-table']/tbody/tr[2]/td[1]").text
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/span").text

    # if text == "1":
    if text == "No Data Available":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'select from date popup "{From}"')
def step_impl(context,From):
    context.driver.find_element(By.ID, "date1").send_keys(From)

@then(u'select to date popup "{To}"')
def step_impl(context,To):
    context.driver.find_element(By.ID, "date2").send_keys(To)

@then(u'click on search butn')
def step_impl(context):
    context.driver.find_element(By.ID, "search_alloc").click()
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/span").text
    if text == "No Data Available":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

    # time.sleep(1)
    # context.driver.close()