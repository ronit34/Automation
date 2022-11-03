from behave import *
import time

from selenium.webdriver.support.select import Select


@then(u'select the Tucs from the tuc list')
def step_impl(context):
    time.sleep(2)
    select = Select(context.driver.find_element_by_id('multiple_tucs'))
    select.select_by_visible_text('ICICI(2000)')


@then(u'Click On Search and check assigned category')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("search")
    context.driver.execute_script("arguments[0].click();", button)
    time.sleep(2)
    text = context.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[3]/table/tbody/tr[2]/td[1]").text
    if text == "ICICI(2000)":
        assert True, "Text Passed"
    else:
        assert False, f" {text} ----> Not Found"



