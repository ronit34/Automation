import time
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then(u'Click on credits')
def step_impl(context):
    button = context.driver.find_element(By.XPATH, "//*[@id='menu_credit_allocation']/p")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Click on limit')
def step_impl(context):
    select = Select(context.driver.find_element(By.ID, "record_limit"))
    select.select_by_visible_text('5')


@then(u'Click on i button')
def step_impl(context):
    button = context.driver.find_element(By.XPATH, "//*[@id='campaign-table']/tbody/tr[2]/td[7]/a/img")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Verify the text')
def step_impl(context):
    text = context.driver.find_element(By.XPATH, "//*[@id='bd-example-modal-lg']/div/div/div[2]/p")
    print(text)
    if text:
        assert True, "Text is available"
    else:
        assert False, "Text isn't available"
