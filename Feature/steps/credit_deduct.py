from behave import *
from selenium.webdriver.common.by import By

@then(u'Select DEDUCT-Credit')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='deduct_credit_div']/label").click()



