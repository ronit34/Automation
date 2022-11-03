from behave import *
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

@then(u'select new group for campaign')
def step_impl(context):
    time.sleep(1)
    select = Select(context.driver.find_element(By.ID, "groupDropdownCamp"))
    select.select_by_visible_text('test (19)')

@then(u'click on send now button of campaign sms')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "confirm_send_sms")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check the scheduled sms is present or not in campaign')
def step_impl(context):
    time.sleep(2)
    schedule = context.driver.find_element(By.XPATH,
                 "//*[@id='pills-campaign']/div/table/tbody/tr[2]/td[1]").text
    if schedule == '123456':
        assert True, f"Scheduled sms is present"
    else:
        assert False, f"Scheduled sms is not present"

    # time.sleep(1)
    # context.driver.close()