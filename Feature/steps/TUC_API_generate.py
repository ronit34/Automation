import time

from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

@then(u'Select Account from Account Type dropdown')
def step_impl(context):
    time.sleep(1)
    select = Select(context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[1]/div[2]/div/div/div/div[2]/div/select"))
    select.select_by_visible_text('OTP')

@then(u'click on Submit button of Generate api')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[1]/div[2]/div/div/div/div[3]/a[2]")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'Verify whether api key for same Account Type is created or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[3]").text

    if text == "otp":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

    # time.sleep(1)
    # context.driver.close()