from behave import *
import time


@then(u'fill the category name')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_id("spam-cat-name").send_keys("promotes violence")


@then(u'click on add to add this category')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("add")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'check if the category is added or not')
def step_impl(context):
    time.sleep(3)
    text = context.driver.find_element_by_xpath("//*[@id='tab_content']/table/tbody/tr[2]/td[1]").text
    if text == "promotes violence [4008]":
        assert True, "Text Passed"
    else:
        assert False, f" {text} ----> Not Found , category not created"

    # time.sleep(2)
    # context.driver.close()
