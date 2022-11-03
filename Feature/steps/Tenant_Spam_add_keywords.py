from behave import *
import time

from selenium.webdriver.support.select import Select


@then(u'Select Category from Dropdown')
def step_impl(context):
    time.sleep(2)
    select = Select(context.driver.find_element_by_id('spam-cat-select'))
    select.select_by_visible_text('promotes violence(4008)')


@then(u'enter first spam keyword')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[3]/div/input").send_keys("kill")


@then(u'click on add keyword button')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("split_more")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'enter second spam keyword')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[4]/div/input").send_keys("attack")

@then(u'Click Add')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("add")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'check if the keyword is added or not')
def step_impl(context):
    time.sleep(2)
    select = Select(context.driver.find_element_by_id('spam-cat-select'))
    select.select_by_visible_text('promotes violence(4008)')

    time.sleep(2)
    button = context.driver.find_element_by_id("search")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(3)
    text1 = context.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[3]/table/tbody/tr[2]/td[1]").text
    text2 = context.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[3]/table/tbody/tr[3]/td[1]").text
    if text1 == "kill" and text2 == "attack":
        assert True, "Text Passed"
    else:
        assert False, f" {text1} ----> Not Found"


    # time.sleep(2)
    # context.driver.close()







